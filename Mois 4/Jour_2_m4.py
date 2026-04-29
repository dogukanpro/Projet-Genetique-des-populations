#Jour 2 : Calcul de distances via Pythagore
import math

def distance_3d(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)

atome_a = (12.5, 45.2, 10.1)
atome_b = (14.2, 43.8, 11.5)
print(f"Distance : {distance_3d(atome_a, atome_b):.2f} Angströms")