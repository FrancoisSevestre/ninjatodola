from fonctions.pickle import recuperer_donnees, deposer_donnees
from classes.ninjatodola_objects import ListeDeTaches


def launch(CONFIG_SAUVEGARDE, EMPLACEMENT_SAUVEGARDE):
    """Looking for existing config files and LDT save and returning the save_file, main_list and current_object."""

    #Try to open the .save file in the config directory
    try:
        save_file = recuperer_donnees(CONFIG_SAUVEGARDE)
    except FileNotFoundError:
        save_file = EMPLACEMENT_SAUVEGARDE + "main_list"
        deposer_donnees(save_file, CONFIG_SAUVEGARDE, "wb")
    save_file = recuperer_donnees(CONFIG_SAUVEGARDE)

    #Loading the save or creation of a new one 
    try:
        main_list = recuperer_donnees(save_file)    
    except FileNotFoundError:
        main_list = ListeDeTaches("NinjaTODOla", None, None, 0) #creation of a new tree
        deposer_donnees(main_list, save_file, "wb")

    main_list = recuperer_donnees(save_file)
    current_object = main_list

    start_tuple = (save_file, main_list, current_object)
    return start_tuple