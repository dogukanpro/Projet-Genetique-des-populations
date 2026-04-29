#Jour 8 : Détection de collisions atomiques
# Vérifie si deux atomes sont trop proches (Rayon de Van der Waals).

def detecter_collision(dist, seuil=1.2):
    """Si la distance est inférieure au seuil, il y a choc stérique."""
    if dist < seuil:
        return True
    return False

#Test entre deux atomes
distance_mesuree = 0.95 # Å
if detecter_collision(distance_mesuree):
    print(f"Alerte : Collision détectée ({distance_mesuree} Å) ! Encombrement stérique.")
else:
    print("Stabilité : Pas de collision.")