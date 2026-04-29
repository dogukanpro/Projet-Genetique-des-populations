#Jour 16 à 24 : Programmation orientée objet et analyse de séquences
#Modélisation d'individus et recherche de motifs génétiques (Regex).

import re # Jour 18

class Individu: # Jour 20
    def __init__(self, id_bio, genome):
        self.id_bio = id_bio
        self.__genome = genome #Variable privée (Jour 3)

    def chercher_motif(self, motif):
        """Recherche une TATA box ou autre motif (Jour 18)"""
        return re.findall(motif, self.__genome)

class Descendant(Individu): #Héritage (Jour 22)
    def transmettre_heritage(self):
        return "Transmission des caractère ancestraux activée."

# Test des classes
sujet_1 = Individu("IND-001", "ATATATGCGTATA")
print(f"Motifs TATA trouvés : {sujet_1.chercher_motif('TATA')}")

#Utilisation de zip() pour comparer (Jour 17)
seq1, seq2 = "ATGC", "ATGG"
differences = sum(1 for a, b in zip(seq1, seq2) if a != b)
print(f"Différences d'alignement : {differences}")
