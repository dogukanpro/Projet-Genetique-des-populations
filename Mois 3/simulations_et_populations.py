#Jour 1 à 7 : Modélisation des populations et programmation fonctionnelle
#Ce script simule la croissance démographique et filtre les individus par adaptation.

#1. Croissance exponentielle (Jour 2)
def simuler_croissance(pop_initiale, taux, generations):
    pop = pop_initiale
    gen = 0
    while gen < generations: # Utilisation de while
        pop += int(pop * taux)
        gen += 1
    return pop

#2. Manipulation de données ave Sets et Filter (Jour 5 & 6)
alleles_pop_a = {"A1", "A2", "B1"}
alleles_pop_b = {"B1", "C1", "D1"}
partages = alleles_pop_a.intersection(alleles_pop_b) # Allèles partagés (Jour 5)

individus_temp = [12, 15, 8, 22, 30] # Températures de survie
# Filtrage des individus adaptés au froid (Jour 6)
survivants = list(filter(lambda x: x < 20, individus_temp))

#3. Transformation avec Map (Jour 7)
adn_list = ["atgc", "ggta", "ttaa"]
arn_list = list(map(lambda x: x.upper().replace("T", "U"), adn_list))

print(f"Population après 10 gén : {simuler_croissance(100, 0.1, 10)}")
print(f"Individus adaptés au froid : {survivants}")
print(f"Transcription en masse : {arn_list}")