from fonctions.pickle import recuperer_donnees, deposer_donnees
from classes.ninjatodola_objects import ListeDeTaches


def launch():
    """Looking for existing config files and LDT save and returning the current_object."""

    #essai d'ouverture d'une fichier .save present dans le fichier config
    CONFIG_SAUVEGARDE = "config/save"
    EMPLACEMENT_SAUVEGARDE = "sauvegardes/"
    try:
        fichier_sauvegarde = recuperer_donnees(CONFIG_SAUVEGARDE)
    except FileNotFoundError:
        fichier_sauvegarde = EMPLACEMENT_SAUVEGARDE + "liste_principale"
        deposer_donnees(fichier_sauvegarde, CONFIG_SAUVEGARDE, "wb")
    fichier_sauvegarde = recuperer_donnees(CONFIG_SAUVEGARDE)

    #chargement de la sauvegarde ou creation d'une nouvelle 
    try:
        liste_principale = recuperer_donnees(fichier_sauvegarde)    
    except FileNotFoundError:
        liste_principale = ListeDeTaches("NinjaTODOla", None, None, 0) #creation d'un nouvelle arbre
        deposer_donnees(liste_principale, fichier_sauvegarde, "wb")

    liste_principale = recuperer_donnees(fichier_sauvegarde)
    current_object = liste_principale

    return current_object