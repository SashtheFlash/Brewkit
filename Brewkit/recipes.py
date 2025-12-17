
# brewkit/recipes.py
# Definiert verfügbares Extra-Zeug (über Basisbier hinaus) und konkrete Rezept-Mappings.

from dataclasses import dataclass
from typing import Set, List, Dict

# Basisbier ist immer vorhanden: Malz + Hopfen + Wasser
BASE_BEER_NAME = "Normales Bier"

# Zutaten mit Modifikator
EXTRAS: Dict[str, Dict] = {
    "pilze":          {"label": "Pilze",            "dc_mod": 2},
    "kraeuter":       {"label": "Kräutermischung",  "dc_mod": 2},
    "mimikzungen":    {"label": "Mimikzungen",      "dc_mod": 4},
    "honig":          {"label": "Honig",            "dc_mod": 1},
    "chili":          {"label": "Chili",            "dc_mod": 2},
    "scharfewurzeln": {"label": "Scharfe Wurzel",   "dc_mod": 2},
    "eiswasser":      {"label": "Eiswasser",        "dc_mod": 2},
    "minze":          {"label": "Minze",            "dc_mod": 1},
    "mondwasser":     {"label": "Mondwasser",       "dc_mod": 3},
    "fruechte":       {"label": "Früchte",          "dc_mod": 1},
    "zucker":         {"label": "Zucker",           "dc_mod": 1},
    "zitrone":        {"label": "Zitrone",          "dc_mod": 1},
    "knoblauch":      {"label": "Knoblauch",        "dc_mod": 2},
    "trauben":        {"label": "Trauben",          "dc_mod": 1},
    "essig":          {"label": "Essig",            "dc_mod": 1},
    "kamille":        {"label": "Kamille",          "dc_mod": 1},
    "kartoffeln":     {"label": "Kartoffeln",       "dc_mod": 1},
    "beeren":         {"label": "Beeren",           "dc_mod": 1},
    "milch":          {"label": "Milch",            "dc_mod": 1},
    "ingwer":         {"label": "Ingwer",           "dc_mod": 1},
    "salz":           {"label": "Salz",             "dc_mod": 0},
}

@dataclass(frozen=True)
class Recipe:
    name: str
    ingredients: Set[str]        # Set der Extras (Basisbier ist implizit)
    effect: str                  # positiver Effekt bei Erfolg
    side_effect: str             # typische Nebenwirkung bei Fehlschlag/Improv
    sg: int                      # empfohlener SG für dieses Rezept

# Rezepte beliebig erweiterbar
RECIPES: List[Recipe] = [
    Recipe("Pilzbräu des Mutigen", {"pilze"},
           "Vorteil auf Rettungswürfe gegen Angst für 1 Stunde",
           "Grüne Zunge, riecht nach Wald", 12),

    Recipe("Schimmerbier", {"pilze","kraeuter"},
           "Leuchtet leicht im Dunkeln für 10 Min",
           "Übelkeit; Nachteil auf Heimlichkeit", 14),

    Recipe("Halluzinogenes Hopfenbier", {"pilze"},
           "Trinker sieht Illusionen (nur Flavour/Roleplay)",
           "Nachteil auf Wahrnehmung für 1 Stunde", 15),

    Recipe("Pilzstarkbier", {"pilze"},
           "+1 auf Stärke für 10 Min",
           "Extremer Hunger", 13),

    Recipe("Grüntrunk der Klarheit", {"kraeuter"},
           "Vorteil auf Weisheitswürfe für 10 Min",
           "Spricht in Reimen", 14),

    Recipe("Pilz-Kräuter-Elixier", {"pilze","kraeuter"},
           "Gewährt Dunkelsicht für 1 Stunde",
           "Alles erscheint psychedelisch bunt", 16),

    Recipe("Hopfen & Halluzination", {"pilze","kraeuter"},
           "Illusionen wirken realer (nur für den Trinker)",
           "Nachteil auf Investigation", 15),

    Recipe("Mutmacher-Mischung", {"kraeuter"},
           "Vorteil auf Angriffswürfe in der ersten Kampfrunde",
           "Sehr laut (Nachteil auf Heimlichkeit)", 17),

    Recipe("Mimik-Malztrunk", {"mimikzungen","pilze"},
           "Für 10 Min Objekte imitieren (Tarnung, einfache Formen)",
           "Klebt 1 Min an Oberflächen", 17),

    Recipe("Gestaltwandler-Gebräu", {"mimikzungen","kraeuter"},
           "Für 5 Min kleine Formänderungen (Haut-/Haarfarbe)",
           "Kurzzeitige Mimik-Merkmale (z. B. lange Zunge)", 18),

    # Alternative Zutaten
    Recipe("Hopfenbier der Heilung", {"honig"},
           "Heilt 1W4 Trefferpunkte (einmalig)",
           "Nachteil auf Initiative für 10 Min (entspannt)", 12),

    Recipe("Gluttrunk", {"chili"},
           "+1 auf Nahkampfschaden für 1 Min",
           "KON-RW gegen Husten, sonst lautes Husten (Nachteil auf Heimlichkeit)", 13),

    Recipe("Gluttrunk", {"scharfewurzel"},
           "+1 auf Nahkampfschaden für 1 Min",
           "KON-RW gegen Husten, sonst lautes Husten (Nachteil auf Heimlichkeit)", 13),

    Recipe("Frostbier", {"eiswasser","minze"},
           "Resistenz gegen Feuer für 10 Min",
           "Blaue Lippen, spricht sehr langsam", 14),

    Recipe("Sternenlicht-Schnaps", {"mondwasser","zucker","fruechte"},
           "Vorteil auf Wahrnehmung für 10 Min",
           "Leicht leuchtende Haut (Nachteil auf Heimlichkeit)", 14),

    Recipe("Knobisaft", {"knoblauch","salz"},
           "Vorteil auf Rettungswürfe gegen Gift für 10 Min",
           "Übler Atem → Umkreis 3 m: Nachteil auf Heimlichkeit", 13),

    Recipe("Witzbold-Wein", {"trauben","zucker"},
           "Vorteil auf nächsten Charisma-Wurf (außer Einschüchtern)",
           "Alle 2 Min ein schlechter Witz", 12),

    Recipe("Donnerbräu", {"essig"},
           "Nächster Nahkampfangriff: +1 Blitzschaden",
           "Rülpser hörbar auf 30 m", 14),

    Recipe("Schlafmütze-Sud", {"kamille","honig"},
           "Vorteil auf nächsten Rettungswurf gegen Furcht",
           "Sehr schläfrig (Nachteil auf Initiative) für 10 Min", 12),

    Recipe("Eisenfaust-Eintopf", {"kartoffeln","salz"},
           "+1 auf Stärke-Würfe für 1 Min",
           "Schwerfällig: Nachteil auf Geschick für 10 Min", 13),

    Recipe("Lachtrunk", {"beeren","zucker"},
           "Vorteil auf nächsten RW gegen geistige Effekte",
           "Unkontrolliertes Lachen für 1 Min (Nachteil auf Heimlichkeit)", 12),

    Recipe("Nebeltrunk", {"milch","minze"},
           "Vorteil auf Heimlichkeitswürfe für 10 Min",
           "Verschwommene Sicht: Nachteil auf Wahrnehmung", 14),

    Recipe("Flinkfuß-Bier", {"ingwer","zitrone"},
           "+3 m Bewegung für 1 Min",
           "Stolpern beim ersten Sprint (Nachteil auf erste Bewegungsprobe)", 13),

    Recipe("Brüllbräu", {"chili","salz"},
           "Nächster Einschüchterungswurf hat Vorteil",
           "Muss beim nächsten Satz brüllen (Nachteil auf Heimlichkeit)", 12),
]
