#Jour 1 : Masses atomiques des éléments CHNOPS
MASSES = {"C": 12.01, "H": 1.008, "N": 14.01, "O": 16.00, "P": 30.97, "S": 32.06}

def calculer_masse(composition):
    return sum(MASSES[el] * qte for el, qte in composition.items())

glycine = {"C": 2, "H": 5, "N": 1, "O": 2}
print(f"Masse de la Glycine : {calculer_masse(glycine)} g/mol")