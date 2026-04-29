#Jour 1 à 6 : Création d'outils de calcul biologique
#Ce script regroupe des fonctions utilitaires pour la datation et la simulation aléatoire.

import random # Jour 4
from datetime import datetime # Jour 6

def calculer_activite_c14(age_os, demi_vie=5730):
    """Calcule la décroissance radioactive pour la datation (Jour 2)"""
    #N(t) = N0 * e^(-lambda * t) simplifié pour l'exemple
    unites_restantes = round(100 * (0.5 ** (age_os / demi_vie)), 2)
    return unites_restantes

def simuler_derive_aleatoire(frequence_p, effectif):
    """Modélise le hasard dans l'évolution (Jour 4)"""
    tirages = [random.random() < frequence_p for _ in range(effectif)]
    nouvelle_freq = sum(tirages) / effectif
    return round(nouvelle_freq, 3)

#Test des outils
print(f"Activité C14 restante après 10 000 ans : {calculer_activite_c14(10000)}%")
print(f"Nouvelle fréquence après dérive (pop=100) : {simuler_derive_aleatoire(0.5, 100)}")
print(f"Rapport génér le : {datetime.now().strftime('%d/%m/%Y')}")