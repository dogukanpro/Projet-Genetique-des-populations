#Jour 7 à 15 : Manipulation de données de populations
#Ce script gère des structure de données complexes pour classer les peuples.

# Données imbriquées (Jour 7)
base_populations = {
    "Basques": {"ancetre_A": 0.85, "ancetre_B": 0.15, "distance": 0.02},
    "Celtes": {"ancetre_A": 0.70, "ancetre_B": 0.30, "distance": 0.05}
}

#Filtrage et Tri (Jour 8 & 9)
def filtrer_proximite(seuil):
    return [nom for nom, data in base_populations.items() if data['distance'] < seuil]

#Simulation de matrice de distance génétique (Jour 15)
matrice_fst = [
    [0.0, 0.02, 0.08],
    [0.02, 0.0, 0.07],
    [0.08, 0.07, 0.0]
]

print(f"Populations proches (seuil 0.03) : {filtrer_proximite(0.03)}")
print(f"Indice de fixation Fst (Pop 0 vs Pop 2) : {matrice_fst[0][2]}")