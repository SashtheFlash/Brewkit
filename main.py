
# main.py
from Brewkit.logic import brew, list_allowed_extras, normalize_extras

def print_result(res: dict):
    print(f"\n=== Ergebnis ===")
    print(f"Modus:            {res['mode']}")
    print(f"Basis:            {res['basis']}")
    print(f"Extras:           {res['extras']}")
    print(f"SG:               {res['sg']}")
    print(f"Wurf (d20):       {res['roll_d20']}  (Rolls: {res['rolls']})")
    print(f"Gesamter Check:   {res['total_check']}")
    print(f"Erfolg?:          {res['success']}")
    print(f"Qualität:         {res['quality']}")
    print(f"Name:             {res['name']}")
    print(f"Effekt:           {res['effect']}")
    print(f"Nebenwirkung:     {res['side_effect']}")
    for n in res.get("notes", []):
        print(f"Note:             {n}")
    if res.get("inspiration"):
        print("Bonus:            Inspiration erhalten!")

def ask_mode() -> str:
    print("Braumodus wählen:")
    print("  [1] Präzises Brauen (leichter, SG-Basis 12)")
    print("  [2] Improvisiertes Brauen (schwerer, SG-Basis 15, Nachteil)")
    while True:
        choice = input("Eingabe (1/2): ").strip()
        if choice == "1":
            return "precise"
        if choice == "2":
            return "improv"
        print("Bitte 1 oder 2 eingeben.")

def ask_extras() -> set[str]:
    allowed = list_allowed_extras()
    print("\nExtras eingeben (leer für nur Basisbier).")
    print("Erlaubt:", ", ".join(allowed))
    print("Beispiele:  pilze kraeuter    oder    pilze, kraeuter")
    while True:
        s = input("Zutaten: ").strip()
        picked, unknown = normalize_extras(s)
        if unknown:
            print("Unbekannte Zutaten:", ", ".join(unknown))
            continue
        return picked

def ask_int(prompt: str, default: int) -> int:
    s = input(f"{prompt} (Standard {default}): ").strip()
    if not s:
        return default
    try:
        return int(s)
    except ValueError:
        print("Bitte eine Zahl eingeben.")
        return ask_int(prompt, default)

if __name__ == "__main__":
    print("=== Brewkit – interaktiver Start ===")
    mode = ask_mode()
    extras = ask_extras()
    ability = ask_int("\nAttributsmodifikator (z. B. INT/DEX)", 2)
    prof = ask_int("Proficiency-Bonus (Werkzeugkenntnis)", 2)

    res = brew(
        extras=extras,
        mode=mode,
        ability_mod=ability,
        proficiency_bonus=prof,
        seed=None  # bei Bedarf eine Zahl setzen, um reproduzierbare Tests zu haben
    )
    print_result(res)
