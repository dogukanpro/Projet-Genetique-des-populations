#Jour 25 à 31 : Statistiques et analyse de données finales
#Calculs de variance, fréquences de codons et matrices.

import math
from collections import Counter # Jour 22

#1. Calcul de l'écart-type (Jour 4 & 25)
def calculer_ecart_type(donnees):
    moyenne = sum(donnees) / len(donnees)
    variance = sum([pow(x - moyenne, 2) for x in donnees]) / len(donnees)
    return round(math.sqrt(variance), 2)

#2. Fréquence des codons (Jour 22)
sequence = "AUGUUUGGCUUUAUGAUG"
frequences = Counter([sequence[i:i+3] for i in range(0, len(sequence), 3)])

#3. Matrice de Punnett (Jour 27)
matrice_punnett = [["AA", "Aa"], ["Aa", "aa"]] # Liste de listes

print(f"Écart-type de la taille de pop : {calculer_ecart_type([150, 160, 145, 170])}")
print(f"Compte des codons : {frequences}")