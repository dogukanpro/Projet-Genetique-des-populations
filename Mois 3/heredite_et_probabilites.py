#Jour 16 à 24 : Logique Mendélienne et probabilités
# Simulation de la transmission des allèles et arbres de division.

#1. Données immuables et logique de sélection (Jour 16 & 18)
paires_base = (("A", "T"), ("G", "C")) # Tuple (Jour 16)
check_validite = [True, True, False]
if any(check_validite): #any/all (Jour 18)
    print("Au moins une séquence est valide.")

#2. Récursivité : Arbre de division cellulaire (Jour 23)
def division_cellulaire(n):
    if n == 0: return 1
    return 2 * division_cellulaire(n - 1)

#3. Simulation Carré de Punnett (Jour 17 & 24)
def simuler_mendel(parent1, parent2):
    import random
    gamete1 = random.choice(parent1)
    gamete2 = random.choice(parent2)
    return gamete1 + gamete2

print(f"Nombre de cellules après 5 divisions : {division_cellulaire(5)}")
print(f"Résultat croisement aléatoire (Aa x Aa) : {simuler_mendel('Aa', 'Aa')}")