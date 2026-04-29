#Jour 5 : Géométrie de la liaison peptidique
#Utilisation de math pour calculer des angles de liaisons simples.
import math

class Liaison:
    def __init__(self, nom, longueur):
        self.nom = nom
        self.longueur = longueur

    def calculer_angle_degres(self, oppose, adjacent):
        """Calcule l'angle d'une liaison via l'arctangente"""
        angle_rad = math.atan2(oppose, adjacent)
        return round(math.degrees(angle_rad), 2)

liaison_nc = Liaison("N-C", 1.45) # Longueur moyenne en Angströms
print(f"Liaison : {liaison_nc.nom} | Longueur : {liaison_nc.longueur} Å")
print(f"Angle théorique calculé : {liaison_nc.calculer_angle_degres(1, 1)}°")