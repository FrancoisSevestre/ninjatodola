#dépendances
from os import chdir
from fonctions.scanner_dossier import *
#main

def input_script():
    """Entre et renvoi un script."""
    print("Ecriture du script...")
    script = ""
    continuer = "O"
    while continuer != "N":
        ligne = input("Entrer une ligne de commande:\n")
        script += ligne + "\n"
        continuer = input("Ajouter une ligne? (N)").upper()
    return script

def input_script_from_file():
    """Charge un script depuis un fichier et le renvoi"""
    liste_scripts = scanner_dossier("scripts")
    print(liste_scripts)
    continuer = "non"
    while continuer != "oui":
        nom_fichier = input("Nom du fichier: ")
        if nom_fichier in liste_scripts:
            continuer = "oui"
    chdir("scripts")
    with open(nom_fichier, "r") as fichier:
        script = fichier.read()
    chdir("..")
    return script

def input_script_list():
    """Entre et renvoi un script sous forme de liste de commande."""
    print("Ecriture du script...")
    script = []
    continuer = "O"
    while continuer != "N":
        ligne = input("Entrer une ligne de commande:\n> ")
        script.append(ligne)
        continuer = input("Ajouter une ligne? (N)\n").upper()
    return script

def input_script_from_file_list():
    """Charge un script depuis un fichier et le renvoi"""
    choix = choix_fichier("scripts")
    with open("scripts/" + choix, "r") as fichier:
        script = fichier.read().split("\n")
    return script

#zone de test
if __name__ == "__main__":
    a = input_script()
    print(a)