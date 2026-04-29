#Jour 3 : Modélisation des molécules d'eau
# Manipulation de listes de coordonnées pour simuler des liaisons hydrogène.

#Coordonnées (x, y, z) de deux molécules d'eau
molecule_h2o_1 = [
    ("O", 0.000, 0.000, 0.000),
    ("H", 0.757, 0.586, 0.000),
    ("H", -0.757, 0.586, 0.000)
]

molecule_h2o_2 = [
    ("O", 0.000, 0.000, 2.800), # Située à distance de liaison H
    ("H", 0.757, 0.586, 2.800),
    ("H", -0.757, 0.586, 2.800)
]

#Affichage des coordonnées du deuxième oxygène
oxy_2 = molecule_h2o_2[0]
print(f"Atome : {oxy_2[0]} | Position : X={oxy_2[1]}, Y={oxy_2[2]}, Z={oxy_2[3]}")