#Jour 1 à 7 : Introduction à la Biologie cellulaire et bases Python
#Ce script modélis les composants d'une cellule et utilise les structures de contrôle de base.

#Modélisation des organites (Utilisation de variables et types)
cellule_nom = "Eucaryote"
a_un_noyau = True
organites = ["Mitochondrie", "Appareil de Golgi", "Réticulum Endoplasmique", "Ribosome"]

# Parcours des organites (Utilisation de boucles for)
print(f"Analyse d'une cellule {cellule_nom}:")
for organite in organites:
    print(f" - Organite présent : {organite}")

#Focus sur le cytosquelette (Utilisation de conditions if)
composants_cytosquelette = ["microfilaments", "microtubules"]
proteine_motrice = "myosine"

if proteine_motrice == "myosine" and "microfilaments" in composants_cytosquelette:
    print("Action : Contraction musculaire possible via filaments d'actine et myosine.")

#Simulation production énergie (Mitochondrie -> ATP)
atp_produit = 0
while atp_produit < 3:
    atp_produit += 1
    print(f"Production d'adénosine triphosphate... Total : {atp_produit} ATP")