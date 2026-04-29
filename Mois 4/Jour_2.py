{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "212ab45d",
   "metadata": {},
   "source": [
    "Sujet : Calcul distance 3D"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a33b9e75",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "#Chaque sou-liste est [X, Y, Z]\n",
    "atomes = [\n",
    "    [0.5, 1.2, 3.4],  # Oxygène 1\n",
    "    [2.8, 1.5, 4.1]   # Oxygène 2\n",
    "]\n",
    "\n",
    "a1 = atomes[0]\n",
    "a2 = atomes[1]\n",
    "\n",
    "#Formule : racine( (x2-x1)² + (y2-y1)² + (z2-z1)² )\n",
    "dist_3d = math.sqrt((a2[0]-a1[0])**2 + (a2[1]-a1[1])**2 + (a2[2]-a1[2])**2)\n",
    "\n",
    "print(f\"Position O1 : {a1}\")\n",
    "print(f\"Position O2 : {a2}\")\n",
    "print(f\"Distance 3D : {round(dist_3d, 3)} Å\")"
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
