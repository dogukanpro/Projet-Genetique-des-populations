#Jour 4 : Modélisation objet d'un atome
class Atome:
    def __init__(self, symbole, coords):
        self.symbole = symbole
        self.x, self.y, self.z = coords

    def afficher(self):
        print(f"Atome {self.symbole} en position ({self.x}, {self.y}, {self.z})")

ca = Atome("CA", (12.5, 45.1, 10.2))
ca.afficher()