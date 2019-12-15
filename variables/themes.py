#dépendances
from fonctions.config import *

#fonctions
def color(string, couleur):
    """Permet de colorer le text"""
    string =  couleur.format(string)
    return string


#gestion des couleurs de text
couleur_rouge = "\033[91m {}\033[00m"
couleur_verte = "\033[92m {}\033[00m"
couleur_jaune = "\033[93m {}\033[00m"
couleur_mauve = "\033[94m {}\033[00m"
couleur_violet = "\033[95m {}\033[00m"
couleur_bleu = "\033[96m {}\033[00m"
couleur_gris = "\033[97m {}\033[00m"
couleur_noir = "\033[98m {}\033[00m"

surligne_vert = "\x1b[6;30;42m {}\x1b[0m"
surligne_bleu = "\x1b[0;30;44m {}\x1b[0m"
surligne_noir = "\x1b[0;35;40m {}\x1b[0m"
surligne_rouge = "\x1b[0;33;41m {}\x1b[0m"
surligne_jaune = "\x1b[6;34;43m {}\x1b[0m"
normal = "\x1b[0m {}\x1b[0m"

clignotant = "\33[5m {}\x1b[0m"

#association des couleurs aux themes
if theme_status == "Normal":#couleurs par defaut
    couleur_app = couleur_verte
    hightlight_LDT = surligne_vert
    police_standard = normal
    couleur_indenteur = couleur_bleu
    couleur_numero_position = couleur_verte
    couleur_output = couleur_bleu
    #theme separateur
    couleur_SEP = couleur_gris
    hightlight_SEP = couleur_verte
    #theme commande
    couleur_COM = couleur_bleu
    hightlight_COM = surligne_bleu
    #theme application
    couleur_APP = couleur_bleu
    couleur_APP_AFF = couleur_verte
    hightlight_APP = surligne_bleu
    #theme fichier
    couleur_FIC = couleur_jaune
    hightlight_FIC = surligne_jaune
    #theme dossier
    couleur_DOS = couleur_rouge
    hightlight_DOS = surligne_rouge
    #theme Link
    couleur_LK = couleur_verte
    hightlight_LK = surligne_bleu


if theme_status == "Dark":#couleurs par defaut
    couleur_app = couleur_violet
    hightlight_LDT = surligne_noir
    police_standard = couleur_gris
    couleur_indenteur = clignotant.format(couleur_noir)
    couleur_numero_position = couleur_mauve
    couleur_output = couleur_violet
    #theme separateur
    couleur_SEP = couleur_gris
    hightlight_SEP = couleur_violet
    #theme commande
    couleur_COM = couleur_bleu
    hightlight_COM = surligne_bleu
    #theme application
    couleur_APP = couleur_bleu
    couleur_APP_AFF = couleur_verte
    hightlight_APP = surligne_bleu
    #theme fichier
    couleur_FIC = couleur_jaune
    hightlight_FIC = surligne_jaune
    #theme dossier
    couleur_DOS = couleur_rouge
    hightlight_DOS = surligne_rouge
        #theme Link
    couleur_LK = couleur_verte
    hightlight_LK = surligne_bleu

if theme_status == "Superman":#couleurs par defaut
    couleur_app = couleur_jaune
    hightlight_LDT = surligne_rouge
    police_standard = couleur_bleu
    couleur_indenteur = clignotant.format(couleur_jaune)
    couleur_numero_position = couleur_rouge
    couleur_output = couleur_rouge
    #theme separateur
    couleur_SEP = couleur_gris
    hightlight_SEP = couleur_jaune
    #theme commande
    couleur_COM = couleur_bleu
    hightlight_COM = surligne_bleu
    #theme application
    couleur_APP = couleur_bleu
    couleur_APP_AFF = couleur_verte
    hightlight_APP = surligne_bleu
    #theme fichier
    couleur_FIC = couleur_jaune
    hightlight_FIC = surligne_jaune
    #theme dossier
    couleur_DOS = couleur_rouge
    hightlight_DOS = surligne_rouge
        #theme Link
    couleur_LK = couleur_verte
    hightlight_LK = surligne_bleu

if theme_status == "Rainbow":#couleurs par defaut
    couleur_app = couleur_verte
    hightlight_LDT = surligne_bleu
    police_standard = couleur_jaune
    couleur_indenteur = clignotant.format(couleur_violet)
    couleur_numero_position = couleur_rouge
    couleur_output = couleur_verte
    #theme separateur
    couleur_SEP = couleur_gris
    hightlight_SEP = couleur_verte
    #theme commande
    couleur_COM = couleur_bleu
    hightlight_COM = surligne_bleu
    #theme application
    couleur_APP = couleur_bleu
    couleur_APP_AFF = couleur_verte
    hightlight_APP = surligne_bleu
    #theme fichier
    couleur_FIC = couleur_jaune
    hightlight_FIC = surligne_jaune
    #theme dossier
    couleur_DOS = couleur_rouge
    hightlight_DOS = surligne_rouge
        #theme Link
    couleur_LK = couleur_verte
    hightlight_LK = surligne_bleu












# def clignotant(prt): print("\33[5m {}".format(prt))

#theme:
separateur_de_tache = "\n       ------- \n"
style = surligne_vert
style_normal = normal


if __name__ == "__main__":
    import os
    clignotant("Hello world")
    a = input("")