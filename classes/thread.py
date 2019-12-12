from threading import Thread
from time import sleep
from fonctions.base import clear

class RepresentateurLDT(Thread):
    """Thread chargé d'enregistrer la repr LDT dans un fichier."""
    def __init__(self, nom_fichier, rafraichissement):
        Thread.__init__(self)
        self.nom_fichier = nom_fichier
        self.rafraichissement = float(rafraichissement)

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        while True:
            with open(self.nom_fichier, "r") as fichier:
                output_LDT = fichier.read()
            clear()
            print(output_LDT)
            sleep(self.rafraichissement)