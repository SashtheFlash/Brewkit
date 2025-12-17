
# brewkit/logic.py
# Kernlogik: Basisbier + optionale Extras → SG berechnen, würfeln, Effekte/Nebenwirkungen bestimmen.

import random
from typing import Dict, List, Optional, Set, Tuple
from .recipes import BASE_BEER_NAME, EXTRAS, RECIPES, Recipe

def _find_recipe(extras: Set[str]) -> Optional[Recipe]:
    """Suche ein Rezept, dessen Zutaten exakt dem Set entsprechen."""
    for r in RECIPES:
        if r.ingredients == extras:
            return r
    return None

def _compute_base_sg(mode: str) -> int:
    """
    Modus:
    - 'precise' (präzises Brauen): leicht → SG 12
    - 'improv'  (improvisiert): schwieriger → SG 15 (und Nachteil auf den Wurf)
    """
    return 12 if mode == "precise" else 15

def _extras_dc_mod(extras: Set[str]) -> int:
    """Summe der DC-Modifikatoren aller Extras (Basisbier ist implizit vorhanden)."""
    return sum(EXTRAS[x]["dc_mod"] for x in extras if x in EXTRAS)

def _roll_d20(disadvantage: bool = False) -> Tuple[int, List[int]]:
    """Würfle 1W20; bei Nachteil: zwei würfeln, den niedrigeren nehmen. Liefert (Ergebnis, [Würfe])."""
    if disadvantage:
        r1, r2 = random.randint(1,20), random.randint(1,20)
        return (min(r1, r2), [r1, r2])
    else:
        r = random.randint(1,20)
        return (r, [r])

def _format_extras(extras: Set[str]) -> str:
    return ", ".join(EXTRAS[x]["label"] for x in sorted(extras))

def brew(
    extras: Set[str],
    mode: str = "precise",          # 'precise' oder 'improv'
    ability_mod: int = 0,           # INT/DEX/… Modifikator
    proficiency_bonus: int = 0,     # Tool/Skill-Proficiency
    seed: Optional[int] = None
) -> Dict:
    """
    Führt einen Brauvorgang aus:
    - Basisbier (Malz/Hopfen/Wasser) ist implizit vorhanden.
    - Extras erhöhen SG und geben besondere Effekte (per Rezept).
    - Kritische Regeln:
        * Nat 20: Legendär → Dauer doppelt, keine Nebenwirkung.
        * Nat 1 : Katastrophe → Explosion, 1W6 Feuerschaden im 5ft-Radius (Flavour-Text).
        * Sehr hoch (>= SG+5): Inspiration zusätzlich.
        * Sehr niedrig (<= SG-5): Nebenwirkung verdoppelt + zufälliger Extraeffekt aus anderem Rezept.
    """
    if seed is not None:
        random.seed(seed)

    # 1) Rezept finden (falls genau passend)
    extras = set(extras)
    recipe = _find_recipe(extras)

    # 2) SG bestimmen
    base_sg = _compute_base_sg(mode)
    disadvantage = (mode == "improv")
    sg_calc = base_sg + _extras_dc_mod(extras)
    if recipe:
        # Nimm den höheren Wert aus berechnetem SG und empfohlenem Rezept-SG
        sg = max(sg_calc, recipe.sg)
    else:
        sg = sg_calc

    # 3) Wurf
    d20, rolls = _roll_d20(disadvantage=disadvantage)
    total = d20 + ability_mod + proficiency_bonus

    # 4) Kritische Sonderfälle
    crit_legend = (d20 == 20)
    crit_catastrophe = (d20 == 1)

    result: Dict = {
        "basis": BASE_BEER_NAME,
        "extras": _format_extras(extras) if extras else "—",
        "mode": ("Präzises Brauen" if mode == "precise" else "Improvisiertes Brauen"),
        "sg": sg,
        "roll_d20": d20,
        "rolls": rolls,
        "total_check": total,
        "success": False,
        "quality": "",
        "name": "",
        "effect": "",
        "side_effect": "",
        "notes": [],
        "inspiration": False,
    }

    # 5) Ergebnislogik
    if crit_catastrophe:
        result["quality"] = "Totaler Fehlschlag (natürliche 1)"
        result["name"] = "Explosiver Kessel"
        result["effect"] = "—"
        result["side_effect"] = "Explosion im Kessel: alle in 1,5 m Radius erleiden 1W6 Feuerschaden; bunte Pilze als Flavour für 1 Stunde."
        return result

    if total >= sg:
        # Erfolg
        result["success"] = True
        result["quality"] = "Erfolg"
        if recipe:
            result["name"] = recipe.name
            # Krit 20 → Dauer doppelt, Nebenwirkung entfällt
            if crit_legend:
                result["effect"] = f"{recipe.effect} (LEGENDÄR: Dauer doppelt, keine Nebenwirkung)"
                result["side_effect"] = "—"
            else:
                result["effect"] = recipe.effect
                result["side_effect"] = "—"  # bei Erfolg i. d. R. keine Nebenwirkung
        else:
            # Kein spezielles Rezept → normales Bier mit Flavour-Bonus
            result["name"] = BASE_BEER_NAME
            result["effect"] = "Leichtes, wohlschmeckendes Bier: +1 auf den nächsten sozialen Wurf (Flavour)."
            result["side_effect"] = "—"

        # Sehr hoher Wurf: Zusatzbonus
        if total >= (sg + 5):
            result["notes"].append("Zusatzbonus: Der Trinker erhält Inspiration.")
            result["inspiration"] = True
        return result

    # Fehlschlag (nicht kritisch)
    result["quality"] = "Fehlschlag"
    if recipe:
        result["name"] = recipe.name
        result["effect"] = "—"
        result["side_effect"] = recipe.side_effect
    else:
        result["name"] = BASE_BEER_NAME
        result["effect"] = "—"
        result["side_effect"] = "Verunglücktes Gebräu: leichter Magenrumor (Flavour)."

    # Sehr niedriger Wurf: Nebenwirkung verstärkt + zufälliger Extraeffekt
    if total <= (sg - 5):
        result["notes"].append("Sehr niedriger Wurf: Nebenwirkung verdoppelt sich.")
        # zufälliger Effekt aus einem anderen Rezept
        other = random.choice([r for r in RECIPES if r.ingredients != extras])
        result["notes"].append(f"Zusätzlicher Nebeneffekt ausgelöst: {other.name} → {other.effect} (instabil).")

    # Krit 20 bei Fehlschlag ist per obiger Logik unmöglich; 1 wurde oben behandelt.
    return result
