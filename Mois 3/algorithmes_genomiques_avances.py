#Jour 8 à 15 : Algorithmique avancée et optimisation
#Gestion de fichiers lourds (générateurs) et fonctions à paramètres variables.

#1. Générateur pour gros fichiers de génomes (Jour 11)
def lire_genome_neandertal(lignes):
    for ligne in lignes:
        # yield permet de ne pas charger tout le fichier en mémoire (Jour 8)
        yield ligne.strip().upper()

#2. Fonctions flexibles pour modèles de mutation (Jour 12 & 13)
def configurer_mutation(*lignees, **parametres):
    """Utilisation de *args et **kwargs pour paramétrer le modèle"""
    taux = parametres.get("taux", 0.001)
    print(f"Analyse des lignées : {lignees} avec un taux de {taux}")

#3. Vérification de type et Tri (Jour 9 & 10)
class Cellule: pass
class Neurone(Cellule): pass

test_cell = Neurone()
if isinstance(test_cell, Cellule): #Vérification (Jour 10)
    print("Type validé : Le neurone est bien une cellule.")

lignees_dates = [("Homo", 300000), ("Neandertal", 400000), ("Erectus", 2000000)]
#Tri personnalisé par date (Jour 9)
lignees_triees = sorted(lignees_dates, key=lambda x: x[1])
print(f"Lignées classées par ancienneté : {lignees_triees}")