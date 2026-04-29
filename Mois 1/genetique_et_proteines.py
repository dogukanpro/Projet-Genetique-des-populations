#Jour 8 à 14 : Gène à la protéine et division cellulaire
#Ce script simule la transcription/traduction et gère les erreurs de lecture de fichiers.

#Dictionnaire du code génétique simplifié (Jour 9)
code_genetique = {"AUG": "Méthionine", "UUU": "Phénylalanine", "GGC": "Glycine"}

def transcrire_adn_en_arn(sequence_adn):
    """Transforme l'ADN en ARN (Jour 8)"""
    return sequence_adn.replace("T", "U")

def traduire_arn(sequence_arn):
    """Traduction par codons (Jour 10)"""
    proteine = []
    # Découpage par 3 bases
    for i in range(0, len(sequence_arn), 3):
        codon = sequence_arn[i:i+3]
        acide_amine = code_genetique.get(codon, "Inconnu")
        proteine.append(acide_amine)
    return proteine

#Gestion des erreurs et lecture de fichiers (Jour 11 & 13)
try:
    adn_test = "ATGTTCGGC" # Exemple de séquence
    arn = transcrire_adn_en_arn(adn_test)
    resultat = traduire_arn(arn)
    print(f"Séquence protéique obtenue : {resultat}")
    
    #Simulation d'ouverture de fichier pour la Mitose (Jour 12)
    with open("division_cellulaire.txt", "w") as f:
        f.write("Phase : Métaphase - Alignement des chromosomes.")
except FileNotFoundError:
    print("Erreur : Le fichier de données génétiques est introuvable.")
except Exception as e:
    print(f"Une erreur imprévue est survenue : {e}")