#dépendances
from fonctions.base import bash, remplacer_les_espaces
from os import chdir
#main

def creation_script(nom_fichier):
    """Permet la création d'un script dans le repertoire scripts"""
    chdir("scripts")
    print("Ecriture du script...")
    script = ""
    continuer = "O"
    while continuer != "N":
        ligne = input("Entrer une commande:\n")
        script += ligne + "\n"
        continuer = input("Ajouter une ligne? (N)").upper()
    with open(nom_fichier, "w") as fichier:
        fichier.write(script)
    print("Le script est modifiable depuis le dossier \"script\".")
    bash("sleep 1s")
    chdir("..")

#zone de test
if __name__ == "__main__":
    creation_script("superapp")