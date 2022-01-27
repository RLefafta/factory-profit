from IPython.display import display
from rich import print
import pandas as pd
from pulp import *
import parameters


class OptimisationProduction:
    def __init__(self):
        self.model = LpProblem(name="planning_usine", sense=LpMaximize)
        self.mois = parameters.mois
        self.produits = parameters.produits
        self.machines = parameters.machines
        self.profit = parameters.profit
        self.ventes_max = parameters.ventes_max
        self.temps_utilisation = parameters.temps_utilisation
        self.maintenance = parameters.maintenance
        self.machines_dispo = parameters.machines_dispo
        self.cout_stockage = parameters.cout_stockage
        self.invente_max = parameters.invente_max
        self.objectif_stock = parameters.objectif_stock
        self.heures_travaille = parameters.heures_travaille

    def _creation_variable_decision(self):
        self.variable_production = LpVariable.dicts(
            "production", (self.mois, self.produits), 0, cat="Integer"
        )

        self.variable_vendu = LpVariable.dicts(
            "vendu", (self.mois, self.produits), 0, cat="Integer"
        )

        self.variable_stock = LpVariable.dicts(
            "stock", (self.mois, self.produits), 0, self.invente_max, cat="Integer"
        )
