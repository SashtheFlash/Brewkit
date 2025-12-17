
# brewkit/recipes.py
# Definiert verfügbares Extra-Zeug (über Basisbier hinaus) und konkrete Rezept-Mappings.

from dataclasses import dataclass
from typing import Set, List, Dict

# Basisbier ist immer vorhanden: Malz + Hopfen + Wasser
BASE_BEER_NAME = "Normales Bier"

# Zutaten mit Modifikator
EXTRAS: Dict[str, Dict] = {
    #gewöhnliche Zutaten
    "pilze":          {"label": "Pilze",            "dc_mod": 2},
    "kraeuter":       {"label": "Kräutermischung",  "dc_mod": 2},
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

    # Monsterzutaten
    "mimikzunge":                  {"label": "Mimikzunge",                "dc_mod": 4},
    "basiliskenauge":              {"label": "Basiliskenauge",            "dc_mod": 4},
    "taeuschbestien_tentakelhaar": {"label": "Täuschbestien-Tentakelhaar","dc_mod": 5},
    "hydraschuppe":                {"label": "Hydraschuppe",              "dc_mod": 5},
    "mantikorstachel":             {"label": "Mantikor-Stachel",          "dc_mod": 5},
    "eulenbaerenfellfasern":       {"label": "Eulenbären-Fellfasern",     "dc_mod": 3},
    "zombiemark":                  {"label": "Zombie-Mark",               "dc_mod": 3},
    "geisteressenz":               {"label": "Geisteressenz",             "dc_mod": 5},
    "teufelsblut":                 {"label": "Teufelsblut",               "dc_mod": 6},
    "feenstaub":                   {"label": "Feenstaub",                 "dc_mod": 4},
    "drachenherzsplitter":         {"label": "Drachenherz-Splitter",      "dc_mod": 7},
    "schleimkern":                 {"label": "Schleimkern",               "dc_mod": 3},
    "greifenfeder":                {"label": "Greifenfeder",              "dc_mod": 4},
    "worgzahn":                    {"label": "Worgzahn",                  "dc_mod": 3},
    "kraken_tentakel":             {"label": "Kraken-Tentakel",           "dc_mod": 5},
    "mykoniden_sporen":            {"label": "Mykoniden-Sporen",          "dc_mod": 3},
    "behir_schuppe":               {"label": "Behir-Schuppe",             "dc_mod": 5},
    "chimaerenhorn":               {"label": "Chimärenhorn",              "dc_mod": 6},
    "ghoul_hautprobe":             {"label": "Ghoul-Hautprobe",           "dc_mod": 3},
    "werwolf_haar":                {"label": "Werwolf-Haar",              "dc_mod": 4},
    "harpyien_stimmharz":          {"label": "Harpyien-Stimmharz",        "dc_mod": 4},
    "medusen_sekret":              {"label": "Medusen-Sekret",            "dc_mod": 5},
    "ettercap_giftdruesen":        {"label": "Ettercap-Giftdrüsen",       "dc_mod": 4},
    "ettercap_spinenseide":        {"label": "Ettercap-Spinnenseide",     "dc_mod": 3},
    "mantis_monk_chitinpuder":     {"label": "Mantis-Chitinpuder",        "dc_mod": 3},
    "ankheg_saurextrakt":          {"label": "Ankheg-Saurextrakt",        "dc_mod": 4},
    "roper_tentakel":              {"label": "Roper-Tentakel",            "dc_mod": 4},
    "roper_auge":                  {"label": "Roper-Auge",                "dc_mod": 5},
    "goblin_ohr":                  {"label": "Goblin-Ohr        ",        "dc_mod": 2},
    "ork_knochensplitter":         {"label": "Ork-Knochensplitter",       "dc_mod": 3},
    "troll_galle":                 {"label": "Troll-Galle",               "dc_mod": 5},
    "troll_regenblut":             {"label": "Troll-Regensblut",          "dc_mod": 5},
    "ogre_zahnstaub":              {"label": "Oger-Zahnstaub",            "dc_mod": 3},
    "gnoll_reisszahn":             {"label": "Gnoll-Reißzahn",            "dc_mod": 3},
    "kobaldfunken":                {"label": "Kobald-Funkenstaub",        "dc_mod": 2},
    "quasit_teer":                 {"label": "Quasit-Teer",               "dc_mod": 4},
    "imp_stachelsekret":           {"label": "Imp-Stachelsekret",         "dc_mod": 4},
    "mephit_asche":                {"label": "Mephit-Asche",              "dc_mod": 3},
    "mephit_frostsplitter":        {"label": "Mephit-Frostsplitter",      "dc_mod": 3},
    "gelatinous_cube_essenz":      {"label": "Gelwürfel-Essenz",          "dc_mod": 4},
    "schattenessenz":              {"label": "Schattenessenz",            "dc_mod": 5},
    "wight_herzasche":             {"label": "Wight-Herz-Asche",          "dc_mod": 5},
    "sporen_der_vertilger":        {"label": "Vernichtersporen (Otyugh)", "dc_mod": 4},
    "ettercap_harz":               {"label": "Ettercap-Harz",             "dc_mod": 3},
    "phase_spinne_silk":           {"label": "Phasenspinnen-Seide",       "dc_mod": 5},
    "displacer_tentakelhaar":      {"label": "Displacer-Tentakelhaar",    "dc_mod": 5},
    "blinkhund_zunge":             {"label": "Blinkhund-Zunge",           "dc_mod": 4},
    "wyvern_gift":                 {"label": "Wyvern-Gift",               "dc_mod": 6},
    "chimera_feuerdruesen":        {"label": "Chimära-Feuerdrüsen",       "dc_mod": 6},
    "minotaurus_hornmehl":         {"label": "Minotaurus-Hornmehl",       "dc_mod": 4},
    "harpyien_federflaum":         {"label": "Harpyien-Federflaum",       "dc_mod": 3},
    "naga_schuppe":                {"label": "Naga-Schuppe",              "dc_mod": 5},
    "yuan_ti_giftextrakt":         {"label": "Yuan-Ti-Giftextrakt",       "dc_mod": 5},
    "pixie_glitzer":               {"label": "Pixie-Glitzer",             "dc_mod": 3},
    "dryaden_blattsaft":           {"label": "Dryaden-Blattsaft",         "dc_mod": 3},
    "satyr_hornpulver":            {"label": "Satyr-Hornpulver",          "dc_mod": 3},
    "elementar_splitter_feuer":    {"label": "Elementar-Splitter (Feuer)","dc_mod": 5},
    "elementar_splitter_eis":      {"label": "Elementar-Splitter (Eis)",  "dc_mod": 5},
    "elementar_splitter_blitz":    {"label": "Elementar-Splitter (Blitz)","dc_mod": 5},
    "pseudodrachen_schuppe":       {"label": "Pseudodrachen-Schuppe",     "dc_mod": 4},
    "schreckenswolf_pelzfasern":   {"label": "Schreckenswolf-Pelzfasern", "dc_mod": 3},
    "augen_des_fliegersaft":       {"label": "Fliegeraugen-Saft",         "dc_mod": 3},
    "geistberuehrter_tau":         {"label": "Geistberührter Tau",        "dc_mod": 4},
    "kuo_toa_schuppentee":         {"label": "Kuo-Toa-Schuppen-Tee",      "dc_mod": 4},
    "quaggoth_chitinflakes":       {"label": "Quaggoth-Chitinflakes",     "dc_mod": 4},
    "rustmonster_antenne":         {"label": "Rostmonster-Antenne",       "dc_mod": 5},
    "gargoyle_splitt":             {"label": "Gargoyle-Splitt",           "dc_mod": 4},
    "banshee_wail_essenz":         {"label": "Banshee-Schrei-Essenz",     "dc_mod": 6},
    "will_o_wisp_funke":           {"label": "Irrlicht-Funke",            "dc_mod": 4},
    "blinkhund_fell":              {"label": "Blinkhund-Fellfasern",      "dc_mod": 3}

}

@dataclass(frozen=True)
class Recipe:
    name: str
    ingredients: Set[str]        # Set der Extras (Basisbier ist implizit)
    effect: str                  # positiver Effekt bei Erfolg
    side_effect: str             # typische Nebenwirkung bei Fehlschlag/Improv
    sg: int                      # empfohlener SG für dieses Rezept

# Rezepte
RECIPES: List[Recipe] = [
    #gewöhnliche Zutaten
    Recipe("Pilzbräu des Mutigen", {"pilze"},
           "Vorteil auf Rettungswürfe gegen Angst für 1 Stunde",
           "Grüne Zunge, riecht nach Wald", 12),

    Recipe("Schimmerbier", {"pilze","kraeuter"},
           "Leuchtet leicht im Dunkeln für 10 Min",
           "Übelkeit; Nachteil auf Heimlichkeit", 14),

    Recipe("Halluzinogenes Hopfenbier", {"pilze"},
           "Trinker sieht Illusionen (nur Flavour/Roleplay)",
           "Nachteil auf Wahrnehmung für 1 Stunde", 15),

    Recipe("Schwammerlkraftbier", {"pilze"},
           "+1 auf Stärke für 10 Min",
           "Extremer Hunger", 13),

    Recipe("Grüntrunk der Klarheit", {"kraeuter"},
           "Vorteil auf Weisheitswürfe für 10 Min",
           "Spricht in Reimen", 14),

    Recipe("Allesfarbenschnaps", {"pilze","kraeuter"},
           "Gewährt Dunkelsicht für 1 Stunde",
           "Alles erscheint psychedelisch bunt, Nachteil auf Investigation", 16),

    Recipe("Mutmacher-Mische", {"kraeuter", "zirtone", "mondwasser"},
           "Vorteil auf Angriffswürfe in der ersten Kampfrunde",
           "Sehr laut (Nachteil auf Heimlichkeit)", 17),

    Recipe("Goldener Met", {"honig", "milch"},
           "Heilt 1W4 Trefferpunkte (einmalig)",
           "Nachteil auf Initiative für 10 Min (entspannt)", 12),

    Recipe("Gluttrunk", {"chili"},
           "+1 auf Nahkampfschaden für 30 Sekunden",
           "KON-RW gegen Husten, sonst lautes Husten (Nachteil auf Heimlichkeit)", 13),

    Recipe("Gluttrunk", {"scharfewurzel"},
           "+1 auf Nahkampfschaden für 30 Sekunden",
           "KON-RW gegen Husten, sonst lautes Husten (Nachteil auf Heimlichkeit)", 13),

    Recipe("Frostbier", {"eiswasser","minze"},
           "Resistenz gegen Feuer für 1 Min",
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

    Recipe("Donnerbräu", {"zitrone", "minze", "eiswasser"},
           "Nächster Nahkampfangriff: +1 Blitzschaden",
           "Rülpser hörbar auf 30 m", 15),

    Recipe("Schlafmütze-Sud", {"kamille","honig"},
           "Vorteil auf nächsten Rettungswurf gegen Furcht",
           "Sehr schläfrig (Nachteil auf Initiative) für 10 Min", 12),

    Recipe("Gorbatschowtopf", {"kartoffeln","salz"},
           "+1 auf Stärke-Würfe für 30 Sekunden",
           "Schwerfällig: Nachteil auf Geschick für 5 Min", 13),

    Recipe("Lachtrunk", {"beeren","zucker"},
           "Vorteil auf nächsten RW gegen geistige Effekte",
           "Unkontrolliertes Lachen für 1 Min (Nachteil auf Heimlichkeit)", 12),

    Recipe("Nebeltrunk", {"milch","minze"},
           "Vorteil auf Heimlichkeitswürfe für 10 Min",
           "Verschwommene Sicht: Nachteil auf Wahrnehmung", 14),

    Recipe("Flinkfuß-Bier", {"ingwer","zitrone"},
           "+3 m Bewegung für 1 Min",
           "Stolpern beim ersten Schritt (Startet mit Bewegung)", 14),

    Recipe("Brüllbräu", {"chili","salz"},
           "Nächster Einschüchterungswurf hat Vorteil",
           "Muss beim nächsten Satz brüllen (Nachteil auf Heimlichkeit)", 12),

    #Monsterzutaten       
    Recipe("Mimik-Malztrunk", {"mimikzunge","pilze"},
           "Für 10 Min Objekte imitieren (Tarnung, einfache Formen)",
           "Klebt 1 Min an Oberflächen", 17),

    Recipe("Gestaltwandler-Gebräu", {"mimikzunge","kraeuter"},
           "Für 5 Min kleine Formänderungen (Haut-/Haarfarbe)",
           "Kurzzeitige Mimik-Merkmale (z. B. lange Zunge)", 18),

    Recipe("Chamäleon-Tonic", {"mimikzunge","mondwasser","minze"},
          "Für 10 Min Vorteil auf Heimlichkeit durch Anpassung an Umgebung",
          "Haut wird kurz klebrig, -1 auf Fingerfertigkeit", 18),

    Recipe("Täusch-Schimmer", {"taeuschbestien_tentakelhaar","mondwasser","minze"},
         "Für 1 Min verschwommene Konturen (schwerer zu treffen)",
         "Schimmernde Silhouette verrät Position bei hellem Licht", 19),

    Recipe("Schattensip", {"quasit_teer","kamille"},
        "Für 10 Min leichte Schattenhülle (Benachteiligung für Beobachter auf Wahrnehmung)",
        "Misstrauen/Paranoia für wenige Minuten", 17),

    Recipe("Schattenschleier", {"schattenessenz","mondwasser","kamille"},
        "30 Min Vorteil auf Heimlichkeit in Dämmerung/Dunkelheit",
        "Kühle Aura, -1 auf Diplomatie", 18),

    Recipe("Basilisken-Bitter", {"basiliskenauge","zitrone"},
        "Für 1 Std Resistenz gegen Versteinerung",
        "Glasiger Blick, -1 auf Wahrnehmung (Sehen)", 18),

    Recipe("Hydra-Honig-Met", {"hydraschuppe","honig","milch"},
        "Regeneration: 1W4 HP/Runde für 30 Sekunden",
        "Heißhunger auf rohes Fleisch", 20),

    Recipe("Blitzlimonade", {"behir_schuppe","zitrone"},
        "Für 1 Std Resistenz gegen Blitzschaden",
        "Haare stehen statisch ab", 18),

    Recipe("Feuer-Mephit-Tonic", {"mephit_asche","chili"},
        "Für 1 Std Resistenz gegen Feuerschaden",
        "Rußspuren an Lippen", 18),

    Recipe("Frost-Mephit-Tonic", {"mephit_frostsplitter","minze"},
        "Für 1 Std Resistenz gegen Kälteschaden",
        "Kalte Atemwolken", 18),

    Recipe("Frostreif-Elixier", {"elementar_splitter_eis","eiswasser","minze"},
        "Für 30 Min Resistenz gegen Kälte",
        "Eisige Fingerspitzen, Nachteil auf Geschicklichkeitswürfe mit Händen", 20),

    Recipe("Feuerfunken-Elixier", {"elementar_splitter_feuer","chili","zucker"},
       "Für 30 Min Resistenz gegen Feuerschaden",
       "Riecht alles verbrannt, Nachteil auf Warnehmungwürfe was Geruch betrifft", 20),

    Recipe("Sturmfunken-Elixier", {"elementar_splitter_blitz","zitrone","zucker"},
        "Für 30 Min Resistenz gegen Blitz",
        "Kleine Funken beim Berühren, verursacht 1 Schaden bei Körperkontakt mit Verbündeten", 20),

    Recipe("Gelwürfel-Klärtrank", {"gelatinous_cube_essenz","essig","salz"},
        "Für 1 Std Resistenz gegen Säure/Schleim",
        "Klebrig-glänzende Haut", 18),

Recipe("Naga-Klartrank", {"naga_schuppe","kamille","mondwasser"},
       "Für 1 Std Resistenz gegen Gift + klare Gedanken",
       "Leichtes Zischeln in der Sprache", 19),

Recipe("Wight-Grabhüter", {"wight_herzasche","mondwasser","knoblauch"},
       "Für 30 Min Resistenz gegen nekrotischen Schaden",
       "Eisige Finger", 20),

Recipe("Medusen-Tonic", {"medusen_naehrsekret","zitrone","kraeuter"},
       "Für 1 Std Immunität gegen Blindheit",
       "Augen schimmern grün", 19),

Recipe("Schleimkern-Lauge", {"schleimkern","essig","salz"},
       "Für 1 Std Resistenz gegen Säure",
       "Schleimiger Speichel, erschwert klares Sprechen", 17),

# --- Offensive & Kampf-Buffs ---
Recipe("Mantikor-Feuertrunk", {"mantikorstachel","chili","scharfewurzeln"},
       "+1 Schaden auf Nahkampf für 10 Min",
       "Brennender Hals, -1 auf Überzeugung", 19),

Recipe("Teufelsblut-Kordial", {"teufelsblut","chili","zucker"},
       "Nächste 3 Angriffe +1W6 Feuerschaden",
       "Rot glühende Augen, -2 auf Heimlichkeit", 21),

Recipe("Chimären-Met", {"chimaerenhorn","trauben","honig"},
       "Zufällig +1W6 Feuer ODER Kälte (10 Min)",
       "Niesanfälle bei Temperaturwechsel", 20),

Recipe("Wyvern-Giftkordial", {"wyvern_gift","honig","knoblauch"},
       "Nächste 2 Angriffe: +1W6 Giftschaden",
       "Risiko: Kon-Rettung SG 12 gegen Übelkeit", 22),

Recipe("Imp-Stacheltrunk", {"imp_stachelsekret","chili","zitrone"},
       "Nächste 2 Angriffe +1W4 Gift",
       "Brennender Magen", 19),

Recipe("Netzweber-Gifttrunk", {"ettercap_giftdruesen","knoblauch","chili"},
       "Vorteil auf Giftangriffe für 10 Min",
       "Bitterer Speichel", 18),

Recipe("Oger-Starkbier", {"ogre_zahnstaub","milch","kartoffeln"},
       "+2 auf Konstitutionsproben/-Rettungswürfe (1 Std)",
       "Träge Glieder: -1 auf Initiative", 16),

Recipe("Hyänen-Zorntrunk", {"gnoll_reisszahn","scharfewurzeln","chili"},
       "Kampfrausch: +1 Schaden (10 Min)",
       "Unkontrolliertes Kichern", 17),

Recipe("Minotaurus-Horntrunk", {"minotaurus_hornmehl","kartoffeln","salz"},
       "Vorteil auf Stoß/Sturz-Manöver (30 Min)",
       "Kurze Kopfschmerz-Welle", 17),

# --- Bewegung & Utility ---
Recipe("Greifenfeder-Tonic", {"greifenfeder","minze","eiswasser"},
       "Für 1 Min Schweben/Levitate-ähnlich",
       "Leichter Federwuchs an Armen", 18),

Recipe("Kletterseiden-Tee", {"ettercap_spinenseide","honig","minze"},
       "Für 10 Min Wände erklimmen (Spider Climb-ähnlich)",
       "Klebige Finger", 16),

Recipe("Roper-Greiftrunk", {"roper_fasern","pilze","trauben"},
       "Greifreflex: Reichweite +1, Vorteil auf Klettern (10 Min)",
       "Steife Gelenke danach", 17),

Recipe("Roper-Kristallkordial", {"roper_kristallkern","mondwasser","zucker"},
       "Steingriff: Vorteil auf Klettern/Greifen (10 Min)",
       "Steife Gelenke für 5 Min", 19),

Recipe("Blinkhund-Sprint", {"blinkhund_zunge","zitrone","eiswasser"},
       "Einmaliger 3–6 m Blink als Bonusaktion in 1 Min",
       "Kurzzeitiger Schwindel", 19),

Recipe("Blinkhund-Brise", {"blinkhund_fell","minze","eiswasser"},
       "+2 auf Akrobatik/Reflexe (10 Min)",
       "Kalter Luftzug um den Körper", 17),

Recipe("Krakenbrack-Wasser", {"kraken_tentakel","eiswasser","salz"},
       "Für 1 Std Wasseratmung",
       "Glitschige Haut, -1 auf Akrobatik", 19),

Recipe("Rustschutz-Bräu", {"rustmonster_antenne","essig","salz"},
       "Metall am Trinker korrodiert 1 Std nicht",
       "Metallischer Nachgeschmack", 19),

# --- Wahrnehmung & Geist ---
Recipe("Traumkappen-Tee", {"mykoniden_sporen","pilze","kamille"},
       "Vorteil auf Weisheitswürfe (30 Min)",
       "Leichte Farbhalluzinationen", 16),

Recipe("Ghoul-Abwehrtrank", {"ghoul_klauenstaub","knoblauch","essig"},
       "Vorteil auf Todesrettungswürfe (1 Std)",
       "Leichter Verwesungsgeruch", 17),

Recipe("Geisterschleier-Tee", {"geisteressenz","mondwasser","kamille"},
       "Für 1 Min Unsichtbarkeit (kurz/fragil)",
       "Frösteln, -2 auf Konstitution (10 Min)", 20),

Recipe("Dryaden-Balsam", {"dryaden_blattsaft","kraeuter","honig"},
       "2W4 Heilung sofort + Vorteil auf erholsame Rast",
       "Grünlicher Hautschimmer", 18),

Recipe("Satyr-Reigen", {"satyr_hornpulver","trauben","honig"},
       "Festlaune: +2 Charisma in Geselligkeit (1 Std)",
       "Übermut, -1 auf Konzentration", 17),

Recipe("Pixie-Fizz", {"pixie_glitzer","beeren","zucker"},
       "Leichtes Leuchten & +1 Charisma (30 Min)",
       "Faszination für bunte Lichter", 16),

Recipe("Irrlicht-Glühtrank", {"will_o_wisp_funke","mondwasser","zucker"},
       "Kleines schwebendes Licht folgt 30 Min (Light-ähnlich)",
       "Zieht Insekten an", 17),

# --- Natur & Körper ---
Recipe("Eulenbären-Starkbier", {"eulenbaerenfellfasern","ingwer","kartoffeln"},
       "+2 auf Stärkeproben (30 Min)",
       "Reizbare Stimmung", 16),

Recipe("Werwolf-Wildbräu", {"werwolf_haar","fruechte","beeren"},
       "+2 auf Athletik (30 Min)",
       "Knurren bei Stress", 17),

Recipe("Worgzahn-Jagdtrunk", {"worgzahn","ingwer","beeren"},
       "+2 auf Initiative (10 Min)",
       "Gelegentliches Heulen", 16),

Recipe("Bulette-Erdtrunk", {"buletten_panzerflocken","kartoffeln","salz"},
       "Standfest: Vorteil gegen Umwerfen (30 Min)",
       "Schwere Beine", 17),

Recipe("Ankheg-Säuretrunk", {"ankheg_saurextrakt","essig","salz"},
       "Für 1 Std starke Säureresistenz",
       "Saurer Magen", 18),

Recipe("Ork-Knochenbrühe", {"ork_knochensplitter","kartoffeln","salz"},
       "+2 auf Kraftakte/Tragen (30 Min)",
       "Polternde Verdauung", 16),

Recipe("Oger-Malz", {"ogre_zahnstaub","ingwer","salz"},
       "Robustheit: +2 auf Konstitutionsproben (30 Min)",
       "Träge Bewegung", 16),

# --- Elementar-Macht (Drachen/Chimären) ---
Recipe("Drachenherz-Essenz (Feuer)", {"drachenherzsplitter","chili","mondwasser"},
       "Für 10 Min Immunität gegen Feuer",
       "Schuppenflecken für 24 Std", 24),

Recipe("Drachenherz-Essenz (Frost)", {"drachenherzsplitter","eiswasser","minze"},
       "Für 10 Min Immunität gegen Kälte",
       "Eisblaue Hautflecken für 24 Std", 24),

Recipe("Drachenherz-Essenz (Blitz)", {"drachenherzsplitter","zitrone","zucker"},
       "Für 10 Min Immunität gegen Blitz",
       "Statische Haare, leichte Zuckungen", 24),

Recipe("Chimären-Gluttrunk", {"chimera_feuerdruesen","chili","mondwasser"},
       "Für 30 Min starke Feuerresistenz",
       "Heiße Haut, -1 auf Heimlichkeit", 21),

# --- Furcht & Willen ---
Recipe("Banshee-Schweigetee", {"banshee_wail_essenz","eiswasser","kamille"},
       "Vorteil gegen Angst/Einschüchterung (30 Min)",
       "Leises Ohrensausen", 21),

# --- Exotisch & Arkana ---
Recipe("Kobold-Funkenbrause", {"kobaldfunken","zitrone","zucker"},
       "Tüftlergeist: Vorteil auf Arkana/Handwerk (30 Min)",
       "Kleine Funken aus Fingern", 15),

Recipe("Pseudodrachen-Glide", {"pseudodrachen_schuppe","minze","zitrone"},
       "Wacher Blick: +2 auf Wahrnehmung (30 Min)",
       "Züngeln wie ein kleiner Drache", 17),

Recipe("Harpyien-Federflaum", {"harpyien_federflaum","trauben","zitrone"},
       "Sängercharme: +2 auf Darbietung/Gesang (10 Min)",
       "Krächzige Stimme nach Wirkung", 17),
              
]