"""
Contains ListLink class.
"""

#imports
from classes.ninjatodola_objects import NinjatodolaObject
from fonctions.menu import menu
from fonctions.scanner_dossier import choix_fichier
from fonctions.pickle import recuperer_donnees

#variables
EMPLACEMENT_SAUVEGARDE = "sauvegardes/"

#main
class ListLink(NinjatodolaObject):
    """An object present in a list, that can switch the current main_list to another.\\
    The linked list is a file store in the sauvegardes directory."""

    def __init__(self, rank_indent, mother_list_position, mother_list):
        individual_repr = menu("Nommer le lien: ", "minimum")
        NinjatodolaObject.__init__(self, individual_repr, mother_list, mother_list_position, rank_indent)
        self.mother_list = mother_list
        self.nom_classe = "ListLink"
        self.choix_objet = ["r", "e", "k"] #Liste des choix possibles
        self.choix_objet_str = ["\nMenu d'objet:", "- Renommer la liste (r)", "- Executer une app de la liste (e)", "- Supprimer la liste (k)"]
        self.daughter_list_file = self.choose_list_file()
        self.infos = "No infos yet" #for further developpment

    def repr_object(self):
        """returns a tuple containing a string representating the object type, its rank, its hightlight status, its representation, list_of_contend_object"""
        object_tuple = (self.nom_classe, self.rang_indentation, self.position_liste_mere, self.hightlight, self.nom, self.show)
        return object_tuple

    def choose_list_file(self):
        """Asks the user for the file to link and return its file name."""
        list_file_name = choix_fichier(EMPLACEMENT_SAUVEGARDE) #demander le nom du fihcier à charger
        return list_file_name

    def self_execute(self):
        """returns a tuple containing a \"change liste\" message and the name of the list file"""
        execution = ("ChangeList", self.daughter_list_file)
        return execution

    def action_objet(self, choix_retour):
        """Traite un choix d'action spécifique à l'objet venant du menu principal"""
        if choix_retour == "r": # Renommer la liste
            self.rename()

        if choix_retour == "e": #executer une app de la liste
            instruction = self.self_execute()
            return instruction

        if choix_retour == "k": #suppression de a liste
            self.self_destruct()
            return "GoListeMere"
