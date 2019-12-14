#cette fonction mérite d'etre réécrite
#dépendances
from fonctions.base import *


#fonction
def menu(message, type_input, verif=False, items=[], verbose=True, compose=False):
    """Donne le choix entre different item et renvoi leur valeur. type_input = "normal" ou "unique" ou "nombre" ou "minimum". """
    continuer = False
    choix = ""
    while continuer != True:
        message_menu = message
        message_items = "\n" + str(items)# + "\n"
        if verbose == "verbose":
            message_items = ""

        if verbose == "reminder" or verbose == "zero": #turn off the verbose mode
            message_menu = ""

        if verbose == "zero":
            message_items = ""

        if verif and compose: #si l'option verification est activée
            message = message_menu + message_items # ajouter la liste des choix

        if type_input == "normal":
            choix = input(message)

        if type_input == "unique": # si on demande un caractere
            print(message, "\n")
            choix = input_unique()
            return choix

        if type_input == "nombre":
            choix = input_nombre(message, int)

        if type_input == "minimum":
            choix = input_minimum(message)

        if verif:
            if choix in items:
                continuer = True
            else:
                continuer = False
        else:
            continuer = True
    return choix