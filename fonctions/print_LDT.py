from classes.ninjatodola_objects import *
from variables.themes import *
from time import sleep

def print_LDT(list_of_tuple):
    """Allow the representation of the main_list from the list of object_tuple."""
    # print(list_of_tuple)
    representation = ""
    for item in list_of_tuple:
        if item[0] == "ListeDeTaches":
            if item[2] is not None: # if the object is not the main list
                position = int(item[2]) + 1
                representation += color("   "*item[1] + "|->  {}.".format(str(position)), couleur_indenteur) #add indentation
            else:
                pass
            individual_repr = item[4]
            if item[5]:
                pass
            else:
                individual_repr += " ..."

            if item[3]: # add hightlight if necessary
                representation += color(individual_repr, hightlight_LDT)
            else:
                representation += color(individual_repr, police_standard)

            representation += "\n"

        if item[0] == "Application":
            position = int(item[2]) + 1
            representation += color("   "*item[1] + "|->  {}.".format(str(position)), couleur_indenteur) #add indentation
            individual_repr = item[4]
            if item[5]:
                pass
            else:
                individual_repr += " ..."
            if item[3]: # add hightlight if necessary
                representation += color(individual_repr, hightlight_APP)
            else:
                representation += color(individual_repr, couleur_APP)

            representation += "\n"
    
        if item[0] == "Commande":
            position = int(item[2]) + 1
            representation += color("   "*item[1] + "    {}.> ".format(str(position)), couleur_indenteur) #add indentation

            if item[3]: # add hightlight if necessary
                representation += color(item[4], hightlight_COM)
            else:
                representation += color(item[4], couleur_COM)

            representation += "\n"

        if item[0] == "Separateur":
            position = int(item[2]) + 1
            representation += color("   "*item[1] + "|->  {}.".format(str(position)), couleur_indenteur) #add indentation

            if item[3]: # add hightlight if necessary
                representation += color("    __________\n", hightlight_SEP)
            else:
                representation += color("    __________\n", couleur_SEP)
            
            representation += "\n"

        if item[0] == "Dossier":
            position = int(item[2]) + 1
            representation += color("   "*item[1] + "|->  {}.".format(str(position)), couleur_indenteur) #add indentation
            individual_repr = item[4]
            if item[5]:
                pass
            else:
                individual_repr += " ..."
            if item[3]: # add hightlight if necessary
                representation += color(individual_repr, hightlight_DOS)
            else:
                representation += color(individual_repr, couleur_DOS)

            representation += "\n"

        if item[0] == "Fichier":
            position = int(item[2])
            representation += color("   "*item[1] + "    {}> ".format(str(position)), couleur_indenteur) #add indentation

            if item[3]: # add hightlight if necessary
                representation += color(item[4], hightlight_FIC)
            else:
                representation += color(item[4], couleur_FIC)

            representation += "\n"

        if item[0] == "ListLink":
            position = int(item[2])
            representation += color("   "*item[1] + "|->  {}".format(str(position + 1)), couleur_indenteur) #add indentation
            Link_repr = " **~ " + item[4] + "~**"
            if item[3]: # add hightlight if necessary
                representation += color(Link_repr, hightlight_LK)
            else:
                representation += color(Link_repr, couleur_LK)

            representation += "\n"

    return representation