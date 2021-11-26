import random

items1 = [
    "Human capital",
    "De factor mens",
    "Het management",
    "De communicatie",
    "De kerncompetentie",
    "De organisatie-ontwikkeling",
    "De missie",
    "Kennismanagement",
    "De eerste aanzet",
    "Human capital",
    "Globalisatie",
    "Knowledge management",
    "Management",
    "The mission",
    "New business development",
    "Process management",
    "The human factor",
    "ICT",
    "Verduurzaming",
    "Het klimaatbeleid",
]
items2 = [
    "moet meerwaarde leveren bij",
    "stelt eisen aan",
    "dient te faciliteren bij",
    "is uitgangspunt bij",
    "is onlosmakelijk verbonden met",
    "schept voorwaarden voor",
    "dient te focussen op",
    "stuurt",
    "hangt nauw samen met",
    "moet een opstap bieden voor",
    "moet een kader bieden voor",
    "zet doelstellingen voor",
    "geeft een nieuw momentum voor",
]
items3 = [
    "de implementatie van",
    "de terugkoppeling van",
    "het aftimmeren van",
    "het aansturen van",
    "de ontwikkeling van",
    "de flexibilisering van",
    "de integratie van",
    "de inventarisatie van",
    "de definitie van",
    "de insteek van",
    "de inbedding",
    "het design van",
    "de marketing van",
    "de herstructurering van",
    "de marktpenetratie van",
    "het groeiproces van",
]
items4 = [
    "optimale",
    "in elkaar grijpende",
    "eenduidige onderling afhankelijke",
    "structurele",
    "pro-actieve",
    "resultaatgerichte",
    "efficiënte",
    "self learning",
    "consistente",
    "individuele",
    "highly developped",
    "duurzame",
    "klimaatneutrale",
]
items5 = [
    "supply chain processen",
    "business architecture",
    "mijlpalen",
    "targets",
    "business units",
    "organisatie-onderdelen",
    "scenario's",
    "best practices",
    "business models",
    "conceptplannen",
    "organizational units",
    "milestones",
    "supply chain",
    "systems",
    "product concepts",
    "human resource",
]
items6 = [
    "waarbij het belang van",
    "waarbij de feedback van",
    "waarbij het kader voor",
    "waarbij afstemming met",
    "waarbij de structuur van",
    "waarbij de synergie met",
    "waarbij de interface met",
    "waarbij input van",
    "waarbij commitment van",
    "waarbij klankborden met",
    "waarbij inbedding van",
]
items7 = [
    "strategisch beleid",
    "de taskforce",
    "de communicatie",
    "de werkgroepen",
    "new business",
    "development",
    "de systeemintegratie",
    "de markt",
    "de stakeholders",
    "het management",
    "de projectorganisatie",
    "management",
    "core business",
    "task force",
    "feedback",
    "niche marketing",
    "strategic partnership",
    "cutting edge solutions",
    "de holding",
    "de aandeelhouders",
    "de commisarissen",
    "de directie",
    "duurzame ontwikkeling",
    "persoonljke ontwikkeling",
    "klimaatneutraal beleid",
    "de vermindering van CO2-uitstoot",
    "de vermindering van stiksofuitstoot",
    "eye-openers",
]
items8 = [
    "moet uitkristalliseren",
    "voorop staat",
    "centraal staat",
    "wordt aangestuurd",
    "leading is",
    "toegevoegde waarde levert",
    "win-win situaties creëert",
    "moet worden gemanaged",
    "voldoende draagvlak heeft",
    "doorslaggevend is",
    "essentieel is",
    "gewaarborgd is",
    "cruciaal is",
    "nieuwe mogelijkheden biedt",
    "een nieuwe standaard zet",
    "vanzelfsprekend is",
    "een blijvende voorsprong geeft",
    "in het bedrijf wordt ingebed",
]


def random_item(items):
    random.seed()
    return items[random.randint(0, len(items)-1)]


def report_adviesjargon(reply_to):
    reply = (
        "cc @" + reply_to + "\n\n" +
        random_item(items1) + " " +
        random_item(items2) + " " +
        random_item(items3) + " " +
        random_item(items4) + " " +
        random_item(items5) + " " +
        random_item(items6) + " " +
        random_item(items7) + " " +
        random_item(items8) + "." +
        " #adviesjargon"
    )

    return reply
