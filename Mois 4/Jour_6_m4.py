#Jour 6 : Analyse simplifiée d'un fichier PDB
def lire_pdb_simple(ligne_pdb):
    #Format PDB : les coordonnées sont à des positions fixes
    if ligne_pdb.startswith("ATOM"):
        x = float(ligne_pdb[30:38])
        y = float(ligne_pdb[38:46])
        z = float(ligne_pdb[46:54])
        return (x, y, z)

exemple_ligne = "ATOM      1  N   GLY A   1      12.268   5.210  41.725  1.00  0.00           N"
print(f"Coordonnées extraites : {lire_pdb_simple(exemple_ligne)}")