#dépendances
from os import listdir, chdir, getcwd
from fonctions.menu import menu
#main
def scanner_dossier(path=None):
    """Renvoi la liste des fichiers présents dans le dossier spécifié"""
    currentpath = getcwd()
    chdir(path)
    liste_fichier = listdir()
    chdir(currentpath)
    return liste_fichier

def choix_fichier(path=None):
    liste_fichier = scanner_dossier(path)
    print("Fichiers disponibles:\n")
    nombre = 0
    for fichier in liste_fichier:
        print("{}- {}".format(nombre, fichier))
        nombre += 1
    choix = menu("Choisir un fichier (Entrer le nombre correspondant): ", "nombre", verif=True, items=list(range(0, len(liste_fichier))))
    return liste_fichier[int(choix)]

#zone de test
if __name__ == "__main__":
    a = choix_fichier("/home/francois")
    print(a)