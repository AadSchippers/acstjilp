import random

items1 = [
    "zwager",
    "lifecoach",
    "moeder",
    "zus",
    "buurvrouw",
    "dansleraar",
    "tante",
    "achternicht",
    "nicht",
    "achterneef",
    "neef",
    "therapeut",
    "minnaar",
    "schoonmoeder",
    "nagelstylist",
    "collega",
    "beste vriend",
    "hartsvriendin",
    "schoonmaakster",
    "seksslaaf",
    "vader",
    "eigenaar",
    "kapster",
    "nieuwe vlam",
    "imaan",
    "dominee",
    "pastoor",
    "yogadocent",
    "voetbaltrainer",
    "stagiaire",
    ]
items2 = [
    "overbuurvrouw",
    "stiefvader",
    "leidinggevende",
    "bewindvoerder",
    "scharrel",
    "oom",
    "zoon",
    "beste vriendin",
    "bff",
    "achterneef",
    "buurman",
    "begeleider",
    "stalker",
    "meisje",
    "aartsvijand",
    "vrouw",
    "nagelstyliste",
    "ex",
    "toyboy",
    "broer",
    "sugar daddy",
    "partner",
    "klusjesman",
    "teamgenoot",
    "hond",
    "dochter",
    "dealer",
    "man",
    "studiegenoot",
    "oma",
    "sm-meesteres",
]
items3 = [
    "opgezwollen",
    "ontstoken",
    "bloedende",
    "verstopte",
    "jeukende",
    "verkoolde",
    "lekkende",
    "gescheurde",
    "verschrompelde",
    "beschimmelde",
    "verbrijzelde",
    "vergiftigde",
    "doorbloede",
    "verkleurde",
    "afgestorven",
    "gebarsten",
]
items4 = [
    "bilspleet",
    "hartklep",
    "dunne darm",
    "voorhuid",
    "tong",
    "prostaat",
    "lever",
    "balzak",
    "hersenstam",
    "tepel",
    "plasbuis",
    "luchtpijp",
    "maagwand",
    "anus",
    "kringspier",
    "onderkaak",
    "knieholte",
    "neusvieugel",
    "vagina",
    "bovenlip",
    "oorschelp",
    "oogbol",
    "blaas",
    "keel",
    "voorhoofdholte",
    "klaplong",
    "kleine teen",
    "wijsvinger",
]
items5 = [
    "gesneuveld",
    "een autistische klopgeest",
    "influencer",
    "allergisch voor bier",
    "een familiebericht in de krant",
    "communistisch",
    "spontaan ontploft",
    "chronisch dronken",
    "ontslagen",
    "impotent",
    "onvruchtbaar",
    "mank",
    "altijd ongesteld",
    "demissionair minister",
    "schijnzwanger",
    "een stuk vlees in de vriezer",
    "rancuneuze incel",
    "van de verkeerde kant",
    "de pijp uit",
    "aan het branden in de hel",
    "Talibanleider in Afghanistan",
    "een hoop as in een urn",
    "een T-rex",
    "amateurwielrenner",
    "een bloeddorstige zombie",
    "een Golden Retreiver",
    "alcoholist met penisnijd",
    "voltooid verleden tijd",
    "Hitler",
    "sportverslaggever",
    "talk show host",
]


def random_item(items):
    random.seed()
    return items[random.randint(0, len(items)-1)]


def report_vaccinatieschade(reply_to):
    reply = (
        "De " +
        random_item(items1) + " " +
        "van mijn " +
        random_item(items2) + " " +
        "kreeg na de coronavaccinatie last van een " +
        random_item(items3) + " " +
        random_item(items4) + " " +
        "en is nu " +
        random_item(items5) + ".\n\n"
        "#VaccinatieSchade bestaat niet"
        + reply_to +
        ", #COVID19 en #LongCovid wél. " +
        "#laatjevaccineren. Voor jezelf, voor elkaar."
    )

    return reply
