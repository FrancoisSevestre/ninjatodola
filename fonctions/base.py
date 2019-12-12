#ce script contient des fonctions d'utilisation courantes uniquement

#dépendances
import os
from subprocess import getoutput

#fonctions
def clear():
    """permet d'effacer l'écran"""
    os.system("clear")

def attendre():
    """attendre que l'utilisateur presse Entrer"""
    input("Presser \"Entrer\" pour continuer")

def bash(commande):
    """permet l'execution d'une commande en bash"""
    os.system(commande)

def input_nombre(message, vtype):
    """ Verification de l'input: vtype = int or float"""
    ok = False
    while (ok != True):
        try:
                nombre = vtype(input(message))
                ok = True
        except:
                print("Entrée incorrecte (nécessite un chiffre)")
    return nombre

def input_minimum(message):
    ok = False
    while ok != True:
        entree = input(message)
        if entree != "":
            ok = True
    return entree

def input_unique():
    variable = getoutput("read -N 1 -t 30 variable  && echo $variable")
    print("\n")
    return variable

def remplacer_les_espaces(phrase, sep):
    """fonction qui permet de remplacer les espaces dans
        la phrase par le separateur"""
    phrase_sans_espaces = ""
    for lettre in phrase:
        if lettre is not " ":
            phrase_sans_espaces += lettre
        else:
            phrase_sans_espaces += sep
    return phrase_sans_espaces

#zone de test
if __name__ == "__main__":
    a = input_unique()
    print(a)