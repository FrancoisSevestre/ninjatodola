#initialization
from os import chdir, getlogin, path
FILE_DIRECTORY = path.dirname(path.realpath(__file__)) #déterminer l'emplacement du fichier
chdir(FILE_DIRECTORY) #se deplacer dans ce dossier

from time import sleep

#dépendences:
from fonctions.pickle import *
from fonctions.menu import *
from fonctions.scanner_dossier import scanner_dossier, choix_fichier
from fonctions.config import *
from fonctions.input_script import *
from variables.choix import *
from fonctions.print_liste import *
from classes.ninjatodola_objects import *
from classes.thread import RepresentateurLDT
from fonctions.compose_output import *
from fonctions.launch_fonction import launch

#Recherche de sauvegarde
objet_en_cours = launch()

#variables:
cache = True

while True:
    clear() #effacer l'écran
    liste_principale.update() #option pour regler le problème d'indentation
    objet_en_cours.switch_hightlight(turn_on=True)

    #enregistrer la liste mere de l'objet en cours
    if objet_en_cours != liste_principale:
        liste_mere_objet = objet_en_cours.liste_mere
    else:
        liste_mere_objet = liste_principale

    #importation des choix possibles en fonctions de l'objet en cours
    choix_objet = objet_en_cours.choix_objet
    choix_menu_principal = print_liste(items_menu_principal + choix_objet)

    #importation des str associés
    choix_objet_str = objet_en_cours.choix_objet_str
    choix_menu_principal_str = print_liste(items_menu_principal_str + choix_objet_str)

    print(repr(liste_principale))

    # comp = compose_output2(repr(liste_principale), choix_menu_principal_str, 70)
    # print(comp)

    choix = menu(choix_menu_principal_str, type_input="unique", verif=True, items=choix_menu_principal, verbose="verbose_status")


    if choix == "4": #se déplacer vers la gauche
        try:
            objet_en_cours.switch_hightlight()
            objet_en_cours = objet_en_cours.liste_mere
            objet_en_cours.switch_hightlight(turn_on=True)
        except AttributeError:
            objet_en_cours = liste_principale
            objet_en_cours.switch_hightlight(turn_on=True)

    if choix == "6": #se déplacer vers la droitescanner_dossier.
        objet_en_cours.show = "on" #dé-cacher la liste (le cas échéant)
        if objet_en_cours.can_go_further():
            objet_en_cours.switch_hightlight()
            objet_en_cours = objet_en_cours.liste_contenu[0]
            objet_en_cours.switch_hightlight(turn_on=True)
        else:
            pass

    if choix == "8" or choix == "2": #aller vers le haut ou le bas
        #trouver la position de la liste en cours dans la liste mere
        position_liste_mere = 0
        position_objet_en_cours = 1
        try:
            for objet in objet_en_cours.liste_mere.liste_contenu:
                if objet == objet_en_cours: #s'identifier en position
                    position_objet_en_cours = position_liste_mere #position de la liste dans la liste mere
                    continue
                else:
                    position_liste_mere += 1
        except AttributeError:
            objet_en_cours = liste_principale

        if choix == "8": #se déplacer vers le haut
            try:
                objet_en_cours.switch_hightlight()
                objet_en_cours = objet_en_cours.liste_mere.liste_contenu[position_objet_en_cours - 1]
                objet_en_cours.switch_hightlight(turn_on=True)
            except IndexError:
                objet_en_cours.switch_hightlight(turn_on=True)
            except AttributeError:
                objet_en_cours.switch_hightlight(turn_on=True)
        if choix == "2": #se déplacer vers le bas
            try:
                objet_en_cours.switch_hightlight()
                objet_en_cours = objet_en_cours.liste_mere.liste_contenu[position_objet_en_cours + 1]
                objet_en_cours.switch_hightlight(turn_on=True)
            except IndexError:
                objet_en_cours.switch_hightlight(turn_on=True)
            except AttributeError:
                objet_en_cours.switch_hightlight(turn_on=True)

    if choix == "o": #options
        #menu option
        menu_option_message = "\n- Changer le mode verbose (v) \n- Changer le theme (t) \n- Changer la console (c) \n- Réinitialiser (ATTENTION!) (R) \n- Annuler (a) \n"
        menu_option_items = ["v", "t", "c", "R", "a"]
        choix = menu(menu_option_message, "normal", verif=True, items=menu_option_items)

        if choix == menu_option_items[3]: #reinitialisation
            print("Pas encore implémenté...")
            
        if choix == menu_option_items[0]: #mode verbose
            verbose_status = param_verbose()
            params = (verbose_status, theme_status, console_status)
            deposer_donnees(params, fichier_sauvegarde_params, "wb")

        if choix == menu_option_items[1]: #selection du theme
            theme_status = param_theme()
            params = (verbose_status, theme_status, console_status)
            deposer_donnees(params, fichier_sauvegarde_params, "wb")

        if choix == menu_option_items[2]: #choix de la console
            console_status = param_console()
            params = (verbose_status, theme_status, console_status)
            deposer_donnees(params, fichier_sauvegarde_params, "wb")
            choix = "null" #car choix = c ==> console

    if choix == "L": #Menu de choix de liste principale
        choix_liste_principale_str = "\n- Charger une autre liste (C)\n- Créer une nouvelle liste (N)\n- Annuler (a)"
        choix_liste_principale = ["C", "N", "a"]
        choix = menu(choix_liste_principale_str, type_input="unique", verif=True, items=choix_liste_principale)

        if choix == "C":
            deposer_donnees(liste_principale, fichier_sauvegarde, "wb") #sauvegarde
            nom_fichier_liste_principale = choix_fichier(EMPLACEMENT_SAUVEGARDE) #demander le nom du fihcier à charger
            fichier_sauvegarde = EMPLACEMENT_SAUVEGARDE + nom_fichier_liste_principale #changer le nom de l'emplacement de sauvegarde
            deposer_donnees(fichier_sauvegarde, CONFIG_SAUVEGARDE, "wb") #sauvegarder le nom de l'emplacement dans save
            liste_principale = recuperer_donnees(fichier_sauvegarde) #charger la nouvelle liste principale
            objet_en_cours = liste_principale #Remettre la liste à 0


        if choix == "N":
            deposer_donnees(liste_principale, fichier_sauvegarde, "wb") #sauvegarde
            nom_liste_principale = menu("Nom de la nouvelle liste: ", "minimum") #demander le nom de la nouvelle liste
            fichier_sauvegarde = EMPLACEMENT_SAUVEGARDE + nom_liste_principale #changer le nom de l'emplacement de sauvegarde
            deposer_donnees(fichier_sauvegarde, CONFIG_SAUVEGARDE, "wb") #changer le fichier save contenant le nom
            liste_principale = ListeDeTaches(nom_liste_principale, None, None, 0) #creation d'un nouvelle arbre
            deposer_donnees(liste_principale, fichier_sauvegarde, "wb")# Sauvegarder la liste nouvellement crée
            objet_en_cours = liste_principale #Remettre la liste à 0

        if choix != "a":
            pass

    if choix == "q": #quitter
        objet_en_cours.switch_hightlight()
        objet_en_cours = liste_principale
        deposer_donnees(liste_principale, fichier_sauvegarde, "wb")
        exit()

    if choix == "c": #mode console
        bash(console_status)
    
    else: # si le choix n'est pas dans le menu principal
        retour = objet_en_cours.action_objet(choix) #envoyer le choix à l'objet en cours, et savoir quoi faire en consequence
        if retour == "GoListeMere":
            objet_en_cours.switch_hightlight()
            objet_en_cours = liste_mere_objet
            objet_en_cours.switch_hightlight(turn_on=True)
        
        if retour == objet_en_cours:
            cache = retour
            objet_en_cours.switch_hightlight()
            objet_en_cours = liste_mere_objet
            objet_en_cours.switch_hightlight(turn_on=True)
        
        if retour == "coller":
            if isinstance(objet_en_cours, ListeDeTaches):
                position = menu("Position: ", type_input="nombre") #choix de la position de l'objet à coller
                cache.liste_mere = objet_en_cours
                objet_en_cours.ajout_objet(cache, position) #coller l'objet dans la liste

            if isinstance(objet_en_cours, Dossier):
                if not isinstance(cache, Dossier) and not isinstance(cache, Fichier):
                    print("Impossible de coller ici...")
                    sleep(1)

        deposer_donnees(liste_principale, fichier_sauvegarde, "wb") #sauvegarde

