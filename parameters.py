mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin"]

produits = ["PROD1", "PROD2", "PROD3", "PROD4", "PROD5", "PROD6", "PROD7"]

machines = [
    "broyeuse",
    "perceuse_verticale",
    "perceuse_horizontale",
    "foreuse",
    "raboteuse",
]
profit = {
    "PROD1": 10,
    "PROD2": 6,
    "PROD3": 8,
    "PROD4": 4,
    "PROD5": 11,
    "PROD6": 9,
    "PROD7": 3,
}

ventes_max = {
    ("Janvier", "PROD1"): 500,
    ("Janvier", "PROD2"): 1000,
    ("Janvier", "PROD3"): 300,
    ("Janvier", "PROD4"): 300,
    ("Janvier", "PROD5"): 800,
    ("Janvier", "PROD6"): 200,
    ("Janvier", "PROD7"): 100,
    ("Février", "PROD1"): 600,
    ("Février", "PROD2"): 500,
    ("Février", "PROD3"): 200,
    ("Février", "PROD4"): 0,
    ("Février", "PROD5"): 400,
    ("Février", "PROD6"): 300,
    ("Février", "PROD7"): 150,
    ("Mars", "PROD1"): 300,
    ("Mars", "PROD2"): 600,
    ("Mars", "PROD3"): 0,
    ("Mars", "PROD4"): 0,
    ("Mars", "PROD5"): 500,
    ("Mars", "PROD6"): 400,
    ("Mars", "PROD7"): 100,
    ("Avril", "PROD1"): 200,
    ("Avril", "PROD2"): 300,
    ("Avril", "PROD3"): 400,
    ("Avril", "PROD4"): 500,
    ("Avril", "PROD5"): 200,
    ("Avril", "PROD6"): 0,
    ("Avril", "PROD7"): 100,
    ("Mai", "PROD1"): 0,
    ("Mai", "PROD2"): 100,
    ("Mai", "PROD3"): 500,
    ("Mai", "PROD4"): 100,
    ("Mai", "PROD5"): 1000,
    ("Mai", "PROD6"): 300,
    ("Mai", "PROD7"): 0,
    ("Juin", "PROD1"): 500,
    ("Juin", "PROD2"): 500,
    ("Juin", "PROD3"): 100,
    ("Juin", "PROD4"): 300,
    ("Juin", "PROD5"): 110,
    ("Juin", "PROD6"): 500,
    ("Juin", "PROD7"): 60,
}

temps_utilisation = {
    "broyeuse": {"PROD1": 0.5, "PROD2": 0.7, "PROD5": 0.3, "PROD6": 0.2, "PROD7": 0.5},
    "perceuse_verticale": {"PROD1": 0.1, "PROD2": 0.2, "PROD4": 0.3, "PROD6": 0.6},
    "perceuse_horizontale": {"PROD1": 0.2, "PROD3": 0.8, "PROD7": 0.6},
    "foreuse": {
        "PROD1": 0.05,
        "PROD2": 0.03,
        "PROD4": 0.07,
        "PROD5": 0.1,
        "PROD7": 0.08,
    },
    "raboteuse": {"PROD3": 0.01, "PROD5": 0.05, "PROD7": 0.05},
}

maintenance = {
    ("Janvier", "broyeuse"): 1,
    ("Février", "perceuse_horizontale"): 2,
    ("Mars", "foreuse"): 1,
    ("Avril", "broyeuse"): 1,
    ("Avril", "perceuse_verticale"): 1,
    ("Mai", "raboteuse"): 1,
    ("Mai", "perceuse_horizontale"): 1,
}

machines_dispo = {
    "broyeuse": 4,
    "perceuse_verticale": 2,
    "perceuse_horizontale": 3,
    "foreuse": 1,
    "raboteuse": 1,
}

cout_stockage = 0.5
invente_max = 100
objectif_stock = 50
heures_travaille = 4 * 6 * 16
