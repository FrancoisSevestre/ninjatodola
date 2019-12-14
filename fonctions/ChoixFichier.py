#dépendances
from os import listdir

#main
def ChoixFichier(path):
    """Renvoi un tuple contenant la liste des fichier et leurs index, dans le chemin du dossier"""
    liste_fichier = listdir(path)
    index_fichier = []
    position_index = 1
    for fichier in liste_fichier:
        index_fichier.append(position_index)
        position_index += 1
    output = [liste_fichier, index_fichier]
    return output

def ListerFichier(tuple_Dossier):
    """Permet de sélectionner un fichier dans le dossier. Renvoi le chemin du fichier."""
    output = []
    liste_fichier = tuple_Dossier[0]
    index_fichier = tuple_Dossier[1]
    length = len(liste_fichier)
    tour = 0
    while tour != length:
        rep = str(index_fichier[tour]) + " - " + liste_fichier[tour]
        output.append(rep)
        tour += 1
    return output




if __name__ == "__main__":
    tuples = ChoixFichier("/home/francois/Documents/")
    SelectionnerFichier(tuples)