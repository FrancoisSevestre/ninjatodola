#dépendances
from fonctions.menu import *
from fonctions.pickle import *

#paramètres de verbose
liste_possibilite_verbose = ["verbose", "reminder", "zero"]
verbose_status = liste_possibilite_verbose[0]

def param_verbose():
    verbose = menu("Choisir un mode: ", "normal", verif=True, items=liste_possibilite_verbose)
    return verbose

#paramètres de theme
liste_possibilite_theme = ["Normal", "Dark", "Superman", "Rainbow"]
theme_status = liste_possibilite_theme[0]

def param_theme():
    theme = menu("Choisir un mode: ", "normal", verif=True, items=liste_possibilite_theme)
    return theme
#paramètres de theme
liste_possibilite_console = ["zsh", "bash", "fish"]
console_status = liste_possibilite_console[0]

def param_console():
    console = menu("Choisir un mode: ", "normal", verif=True, items=liste_possibilite_console)
    return console


#chargement de la config
fichier_sauvegarde_params = "config/.config"
try:
    params = recuperer_donnees(fichier_sauvegarde_params)   
except FileNotFoundError:
    params = (verbose_status, theme_status, console_status)
    deposer_donnees(params, fichier_sauvegarde_params, "wb")

verbose_status = params[0]
theme_status = params[1]
console_status = params[2]