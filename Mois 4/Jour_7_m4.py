#Jour 7 : Filtrage des atomes du squelette (Backbone)
#Analyse d'une liste d'atomes pour extraire uniquement les Carbones Alpha (CA).

atomes_proteine = [
    {"type": "N", "id": 1},
    {"type": "CA", "id": 2},
    {"type": "C", "id": 3},
    {"type": "O", "id": 4},
    {"type": "CA", "id": 5}
]

#Filtrage par compréhension de liste (List Comprehension)
carbones_alpha = [atome for atome in atomes_proteine if atome["type"] == "CA"]

print(f"Nombre de résidus (via Carbones Alpha) détectés : {len(carbones_alpha)}")
for ca in carbones_alpha:
    print(f"Atome identifié : {ca}")