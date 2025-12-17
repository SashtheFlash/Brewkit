
# main.py
import argparse
from Brewkit.logic import brew

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

def parse_args():
    p = argparse.ArgumentParser(description="Brewkit – braue ein Gebräu mit Basisbier und Extras.")
    p.add_argument("--mode", choices=["precise","improv"], default="precise",
                   help="Braumodus: precise (leicht) oder improv (improvisiert, schwerer).")
    p.add_argument("--extras", nargs="*", default=[],
                   help="Liste von Extras (z. B. pilze kraeuter mimikzungen).")
    p.add_argument("--ability", type=int, default=0,
                   help="Attributsmodifikator (z. B. INT/DEX).")
    p.add_argument("--prof", type=int, default=0,
                   help="Proficiency-Bonus (Werkzeugkenntnis).")
    p.add_argument("--seed", type=int, default=None,
                   help="Zufalls-Seed für reproduzierbare Ergebnisse.")
    return p.parse_args()

if __name__ == "__main__":
    args = parse_args()
    res = brew(
        extras=set(args.extras),
        mode=args.mode,
        ability_mod=args.ability,
        proficiency_bonus=args.prof,
        seed=args.seed
    )
