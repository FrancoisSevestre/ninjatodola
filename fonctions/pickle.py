#dépendances
from pickle import Pickler, Unpickler

#fonctions
def deposer_donnees(objet, nom_fichier, mode): 
    """permet de sauvegarder un objet dans un fichier"""
    with open(str(nom_fichier), mode) as fichier:
        mon_pickler = Pickler(fichier)
        mon_pickler.dump(objet)
    
def recuperer_donnees(nom_fichier): 
    """permet de lire un objet depuis un fichier"""
    with open(str(nom_fichier), "rb") as fichier:
        mon_depickler = Unpickler(fichier)
        objet = mon_depickler.load()
        return objet

def sauvegarder_liste(objet, nom_fichier):
    """"""
    try:
        objet = recuperer_donnees(nom_fichier)    
    except FileNotFoundError:
        objet = []
        deposer_donnees(objet, nom_fichier, "wb")

    objet = recuperer_donnees(nom_fichier)
    return objet