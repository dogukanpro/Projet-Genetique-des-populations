#Jour 25 à 31 : Finalisation et nettoyage de données
#Préparation des séquences (strip, split) et visualisation simple.

def nettoyer_sequence(brute):
    """Retrait des impuretés de séquençage (Jour 28)"""
    return brute.strip().upper().replace(" ", "")

def tracer_croissance_pop(valeurs):
    """Graphique texte simple (Jour 27)"""
    for v in valeurs:
        print("|" + "#" * v + f" {v}")

#Exemple final
adn_sale = "  atg cgt acg  "
adn_propre = nettoyer_sequence(adn_sale)
print(f"ADN nettoyé : {adn_propre}")

print("\nVisualisation de la croissance démographique :")
tracer_croissance_pop([2, 5, 8, 12, 10])