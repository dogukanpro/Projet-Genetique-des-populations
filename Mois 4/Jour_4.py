{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a9e70f1b",
   "metadata": {},
   "source": [
    "Sujet : POO création et utlisation de méthode (exemple liaison peptidique)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d5ec71e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "class Atome:\n",
    "    def __init__(self, nom, x, y, z):\n",
    "        self.nom = nom\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "        self.z = z\n",
    "\n",
    "    #Exemple de méthode\n",
    "    def calculer_distance(self, autre):\n",
    "        dx = self.x - autre.x\n",
    "        dy = self.y - autre.y\n",
    "        dz = self.z - autre.z\n",
    "        return round(math.sqrt(dx**2 + dy**2 + dz**2), 2)\n",
    "\n",
    "\n",
    "carbone_C = Atome(\"C\", 1.2, 0.5, 0.0)\n",
    "azote_N = Atome(\"N\", 2.5, 0.7, 0.1)\n",
    "\n",
    "#Utilisation de la méthode\n",
    "distance_cn = carbone_C.calculer_distance(azote_N)\n",
    "\n",
    "print(f\"Liaison entre {carbone_C.nom} et {azote_N.nom}\")\n",
    "print(f\"Distance mesurée : {distance_cn} Å\")\n",
    "\n",
    "# Une liaison peptidique\n",
    "if 1.30 <= distance_cn <= 1.40:\n",
    "    print(\"Distance cohérente avec une liaison peptidique.\")\n",
    "else:\n",
    "    print(\"Distance anormale pour une liaison peptidique.\")"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
