#Jour 15 à 31 : Génétique des populations et évolution
#Ce script calcule les fréquences alléliques et analyse les distances génétiques.

import math # Jour 15

def calculer_hardy_weinberg(p):
    """Calcule p^2 + 2pq + q^2 = 1"""
    q = 1 - p
    f_homozygote_dom = p**2
    f_heterozygote = 2 * p * q
    f_homozygote_rec = q**2
    return f_homozygote_dom, f_heterozygote, f_homozygote_rec

#Test Hardy-Weinberg 
p_freq = 0.6
homo_dom, heter, homo_rec = calculer_hardy_weinberg(p_freq)
print(f"Fréquences : Dominant={homo_dom:.2f}, Hétéro={heter:.2f}, Récessif={homo_rec:.2f}")

#Analyse de séquences (Slicing & Phylogénie - Jour 16 & 20)
sequence_ancetre = "ATGCGTACGTTAGC"
sequence_derivee = "ATGCGTACGTTAGA" #Mutation finale

def comparer_sequences(seq1, seq2):
    differences = 0
    for b1, b2 in zip(seq1, seq2):
        if b1 != b2:
            differences += 1
    return differences

dist = comparer_sequences(sequence_ancetre, sequence_derivee)
print(f"Distance génétique (nombre de mutations) : {dist}")

#Taxonomie (Utilisation de dictionnaires complexes
classification = {
    "Genre": "Homo",
    "Espèce": "Sapiens",
    "Famille": "Hominidae"
}
print(f"Classification : {classification['Genre']} {classification['Espèce']}")