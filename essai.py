from pulp import *
import parameters


class Model:
    def __init__(self):
        self.model = LpProblem(name="planning_usine", sense=LpMaximize)

    def _creation_variable_decision(self, mois: list, produits: list, invente_max: int):
        self.variable_production = LpVariable.dicts(
            "production", (mois, produits), 0, cat="Integer"
        )

        self.variable_vendu = LpVariable.dicts(
            "vendu", (mois, produits), 0, cat="Integer"
        )

        self.variable_stock = LpVariable.dicts(
            "stock", (mois, produits), 0, invente_max, cat="Integer"
        )

    def _fonction_objectif(
        self, profit: dict, produits: list, mois: list, cout_stockage: int
    ):
        self.model += lpSum(
            [
                profit[produit] * self.variable_vendu[m][produit]
                - self.variable_stock[m][produit] * cout_stockage
                for produit in produits
                for m in mois
            ]
        )
        return self.model

    def _vente_max_mois(self, ventes_max: dict, mois: list, produits: list):
        """
        Vente maximum par mois pour chaques produits
        """
        itr = iter(ventes_max.values())
        for m in mois:
            for produit in produits:
                self.model += self.variable_vendu[m][produit] <= next(itr)

    def _balance_initial(self, produits: list, mois: list):
        """
        Balance pour le premier mois
        """
        for produit in produits:
            self.model += (
                self.variable_production[mois[0]][produit]
                == self.variable_vendu[mois[0]][produit]
                + self.variable_stock[mois[0]][produit]
            )
