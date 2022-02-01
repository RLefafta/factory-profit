from pulp import *
import parameters
import pandas as pd
from IPython.display import display


class Model:
    """
    Une classe permettant de résoudre le problème de maximisation de profit

    ...

    Methods
    -------
    _creation_variable_decision()
        Crée les variables production, vente et stock

    _fonction_objectif()
        Crée la fonction objectif

    _vente_max_mois()
        Vente maximum par mois pour chaques produits

    _balance_initial()
        Balance pour le premier mois

    _balance()
        Balance pour les autres mois

    _objectif_stock()
        Objectif de stock pour la fin de l'exercice

    _contrainte_machines()
        Contrainte d'utilisation des machines

    _creation_contrainte()
        Ajout des différentes contraintes à notre modèle

    _resolve()
        Résous le problème d'optimisation

    gain()
        Indique le profit réalisé sur l'exercice

    affichage()
        Affichage profit + tableaux affichant pour chaque mois et chaque produits la production, la vente et le stock.


    """

    def __init__(self):
        self.model = LpProblem(name="planning_usine", sense=LpMaximize)
        self.mois = parameters.mois
        self.produits = parameters.produits

    def _creation_variable_decision(self, invente_max: int = parameters.invente_max):
        self.variable_production = LpVariable.dicts(
            "production", (self.mois, self.produits), 0, cat="Integer"
        )

        self.variable_vendu = LpVariable.dicts(
            "vendu", (self.mois, self.produits), 0, cat="Integer"
        )

        self.variable_stock = LpVariable.dicts(
            "stock", (self.mois, self.produits), 0, invente_max, cat="Integer"
        )

    def _fonction_objectif(
        self,
        profit: dict = parameters.profit,
        cout_stockage: int = parameters.cout_stockage,
    ):
        self.model += lpSum(
            [
                profit[produit] * self.variable_vendu[m][produit]
                - self.variable_stock[m][produit] * cout_stockage
                for produit in self.produits
                for m in self.mois
            ]
        )

    def _vente_max_mois(self, ventes_max: dict = parameters.ventes_max):
        """
        Vente maximum par mois pour chaques produits
        """
        itr = iter(ventes_max.values())
        for m in self.mois:
            for produit in self.produits:
                self.model += self.variable_vendu[m][produit] <= next(itr)

    def _balance_initial(self):
        """
        Balance pour le premier mois
        """
        for produit in self.produits:
            self.model += (
                self.variable_production[self.mois[0]][produit]
                == self.variable_vendu[self.mois[0]][produit]
                + self.variable_stock[self.mois[0]][produit]
            )

    def _balance(self):
        """
        Balance pour les autres mois
        """
        for m in self.mois:
            if m != self.mois[0]:
                for produit in self.produits:
                    self.model += (
                        self.variable_production[m][produit]
                        + self.variable_stock[self.mois[self.mois.index(m) - 1]][
                            produit
                        ]
                        == self.variable_vendu[m][produit]
                        + self.variable_stock[m][produit]
                    )

    def _objectif_stock(self, objectif_stock: int = parameters.objectif_stock):
        """
        Objectif de stock pour la fin de l'exercice
        """
        for produit in self.produits:
            self.model += self.variable_stock[self.mois[-1]][produit] == objectif_stock

    def _contrainte_machines(
        self,
        machines: list = parameters.machines,
        temps_utilisation: dict = parameters.temps_utilisation,
        heures_travaille: str = parameters.heures_travaille,
        machines_dispo: dict = parameters.machines_dispo,
        maintenance: dict = parameters.maintenance,
    ):
        """
        Contrainte d'utilisation des machines
        """
        for m in self.mois:
            for machine in machines:
                self.model += lpSum(
                    [
                        self.variable_production[m][temp]
                        * temps_utilisation[machine][temp]
                        for temp in temps_utilisation[machine]
                    ]
                ) <= heures_travaille * (
                    machines_dispo[machine] - maintenance.get((m, machine), 0)
                )

    def _creation_contrainte(self):
        """
        Ajout des différentes contraintes à notre modèle
        """
        self._vente_max_mois()
        self._balance_initial()
        self._balance()
        self._objectif_stock()
        self._contrainte_machines()

    def _resolve(self):
        """
        Résous le problème d'optimisation
        """
        self.model.solve()

    def gain(self):
        """
        Indique le profit réalisé sur l'exercice
        """
        self._resolve()
        if self.model.status == LpStatusOptimal:
            print("Le profit total est de {}".format(value(self.model.objective)))
        else:
            print("Erreur")

    def affichage(self):
        """
        Affichage profit + tableaux affichant pour chaque mois et chaque produits la production, la vente et le stock.
        """
        self.gain()
        ligne = self.mois.copy()
        colonne = self.produits.copy()
        production_plan = pd.DataFrame(columns=colonne, index=ligne, data=0.0)
        vendu_plan = pd.DataFrame(columns=colonne, index=ligne, data=0.0)
        stock_plan = pd.DataFrame(columns=colonne, index=ligne, data=0.0)
        for m in self.mois:
            for produit in self.produits:
                production_plan.loc[m][produit] = self.variable_production[m][
                    produit
                ].varValue
                vendu_plan.loc[m][produit] = self.variable_vendu[m][produit].varValue
                stock_plan.loc[m][produit] = self.variable_stock[m][produit].varValue
        production_plan.style.set_table_attributes(
            "style='display:inline'"
        ).set_caption("Plan de production")
        vendu_plan.style.set_table_attributes("style='display:inline'").set_caption(
            "Plan de vente"
        )
        stock_plan.style.set_table_attributes("style='display:inline'").set_caption(
            "Plan de stock"
        )
        display(production_plan)
        display(vendu_plan)
        display(stock_plan)
