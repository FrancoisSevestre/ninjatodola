"""
Module Comprenant les différents objets qui dérivent tous de NinjatodolaObject
"""
#dependencies
from datetime import date
from time import sleep
from subprocess import getoutput
from os import path

#dependances variables
from variables.themes import *

#dépendances fonctions
from fonctions.base import *
from fonctions.menu import *
from fonctions.print_liste import *
from fonctions.scanner_dossier import scanner_dossier, choix_fichier
from fonctions.input_script import *
from fonctions.ChoixFichier import *
from fonctions.list_dir_dirs_files import list_dir_dirs_files
from fonctions.dirname import dirname


class NinjatodolaObject():
    """Classe mere de toutes les classes d'objet de NinjaTODOla """

    def __init__(self, nom, liste_mere, position_liste_mere, rang_indentation, is_a_list=True, is_executable=False):
        self.nom = nom #nom de l'objet
        self.liste_mere = liste_mere #nom de la liste contenant l'objet
        self.position_liste_mere = position_liste_mere #Position de l'objet dans la liste mère
        self.rang_indentation = rang_indentation #rang de l'objet/ indentation dans la representation
        self.liste_contenu = [] #objets contenus dans l'objet
        self.date_de_creation = date.today() #enregistrement de la date de création
        self.hightlight = False #surlignage par defaut de l'objet
        self.theme = False #modification de la representation de l'objet
        self.show = True #attr valant False si l'objet est caché
        self.is_a_list = is_a_list #attribut valant True si l'objet peut contenir d'autres objets parcourables
        self.is_executable = is_executable #attribut valant True si l'objet est executable
        self.nom_classe = "NinjaTODOlaObject"


  #Méthodes de représentation de l'objet:
    def __str__(self):
        """Méthode spéciale appelée quand on utilise la fonction print"""
        output = "{} est un(e) {} contenant {} objets".format(str(self.nom), self.nom_classe, str(len(self.liste_contenu)))
        return output

    def __repr__(self):
        """Méthode appelée quand on utiliser objet.repr()"""
        return None

    def switch_hightlight(self, turn_on=False):
        """Change le status du surlignage"""
        if turn_on:
            self.hightlight = True
        else:
            self.hightlight = False

    def switch_show(self):
        """Change le status de show"""
        if self.show:
            self.show = False
        else:
            self.show = True

  #Méthodes de modification d'attributs:
    def rename(self):
        """Permet de renommer l'objet"""
        nouveau_nom = input("Entrer un nouveau nom: ")
        self.nom = nouveau_nom

    def __getitem__(self, index):
        """Méthode appelée quand on utilise: objet[index]."""
        return self.liste_contenu[index]

    def __setitem__(self, index, valeur):
        """Méthode appelée quand on utilise: objet[index] = valeur."""
        self.liste_contenu[index] = valeur

    def ajout_objet(self, objet, position):
        """Méthode d'ajout d'un objet à une position précise"""
        self.liste_contenu.insert(int(position - 1), objet)

    def __delitem__(self, index):
        """Méthode appelée quand on utilise: del objet[index]."""
        del self.liste_contenu[index]

    def __contains__(self, objet):
        """Renvoi True si l'objet recherché est dans l'objet"""
        if objet in self.liste_contenu:
            return True
        else:
            return False

    def update(self):
        """Méthode permettant de mettre à jour la liste_mere et le rang des objets contenus"""
        for item in self.liste_contenu: #pour chaque item contenu dans l'objet
            item.liste_mere = self #identifier l'objet comme liste_mere de l'item
            item.rang_indentation = self.rang_indentation + 1 #permet une indentation correcte
            item.position_liste_mere = self.find_contenu(item) #se trouver dans la liste mere
            item.switch_hightlight(turn_on=False)
            item.update() #demander la même action à tous les objets contenus

  #Autres méthodes:
    def find_contenu(self, contenu):
        """Méthode renvoyant l'index de l'objet recherché dans la liste"""
        index = 0
        while index != len(self.liste_contenu):
            if self[index] == contenu:
                return index
            index += 1

    def self_destruct(self):
        """Permet de supprimer l'objet en cours"""
        self.liste_mere.update()
        del self.liste_mere[self.position_liste_mere]
        self.liste_mere.update()

    def can_go_further(self):
        """Renvoi True si l'objet contient un objet dans self.objets"""
        if self.is_a_list and len(self.liste_contenu) != 0: #Si l'objet est une liste non vide
            return True
        else:
            return False

    def self_execut(self):
        """Méthode renvoyant un message si l'objet n'est pas executable"""
        if self.is_executable:
            print("L'objet n'a pas encore de fonction executable!")
        else:  
            print("L'objet n'est pas executable!")

class ListeDeTaches(NinjatodolaObject):
    """Liste contenant des objets ordonnés affichables"""
    def __init__(self, nom, liste_mere, position_liste_mere, rang_indentation):
        NinjatodolaObject.__init__(self, nom, liste_mere, position_liste_mere, rang_indentation) #Reprendre la base des attributs et fonction de la classe mere
        self.nom_classe = "ListeDeTaches" #Changer le nom de la classe pour __str__
        self.choix_objet = ["+", "-", "/", "$", "!", "X", "V", "m", "r", "e", "k"] #Liste des choix possibles
        self.choix_objet_str = ["\nMenu d'objet:", "- Ajouter une tâche (+)", "- Supprimer une tâche (-)", "- Placer une tâche (/)", "- Ajouter un objet spécial ($)", "- Développer/Réduire (!)", "- Couper (X)", "- Coller (V)", "- Menu module (m)", "- Renommer la liste (r)", "- Executer une app de la liste (e)", "- Supprimer la liste (k)"] #Liste des str correspondantes

    def __repr__(self):
        representation = ""
        if self.hightlight: #Si l'objet est séléctionné
            # representation += "\b"*4 #effacer le numero
            # representation += color("~~ ", hightlighting) #effacement du numero quand sélectionné
            representation += color(self.nom, hightlighting) #le surligner
        else: #sinon
             representation += color(self.nom, police_standard) #appliquer le theme de base
        if self.show: #Si la liste n'est pas cachée
            position = 0
            for item in self.liste_contenu: #Pour chaque item de la liste
                position += 1
                representation += "\n" #Aller à la ligne
                representation += color("     " * item.rang_indentation + "|-> ", couleur_indenteur)#indenter
                representation += color(str(position)+ ".", couleur_numero_position)#ecrire la position dans la liste
                representation += color(repr(item), police_standard) #ecrire le nom de l'objet
        else: #Si la liste est cachée
            representation += color(" ...", couleur_indenteur) #Ne rien montrer
        return representation

    def repr_object(self):
        """returns a tuple containing a string representating the object type, its rank, its hightlight status, its representation, list_of_contend_object"""

        object_tuple = (self.nom_classe, self.rang_indentation, self.position_liste_mere, self.hightlight, self.nom, self.show)
        liste_de_tuple = []
        liste_de_tuple.append(object_tuple)

        if self.show:
            for item in self.liste_contenu: #pour chaque objet dans la liste
                repr_object_from_list_contenu = item.repr_object() #generate a liste of repr_object
                for r in repr_object_from_list_contenu: # add each tuple in the liste
                    liste_de_tuple.append(r)
        return liste_de_tuple


    def creation_sous_liste(self, nom, position):
        """Permet la création et l'ajout d'une sous-liste à la position donnée"""
        if nom == "SEP":
            objet = Separateur(self, position, self.rang_indentation + 1)
        else:
            objet = ListeDeTaches(nom, self, position, self.rang_indentation + 1)
        self.ajout_objet(objet, position)
    
    def supprimer_tache(self, position):
        """supprime une tâche à la position précisée"""
        try:
            del self[position - 1]
        except IndexError:
            print("La position n'existe pas!")
            sleep(1)

    def self_execut(self):
        """L'execution d'une liste renvoi des infos sur la liste"""
        message = "Pas d'execution possible..."
        print(message)
        sleep(1)
    
    def lancer(self, position):
        """Execute un élément de la liste"""
        self.liste_contenu[position - 1].self_execut()
    
    def action_objet(self, choix_retour):
        """Traite un choix d'action spécifique à l'objet venant du menu principal"""

        #variables
        message_nom_tache = "Nom de la tâche: "
        message_position_tache = "Position: "

        if choix_retour == "+": #ajouter une tache à la suite dans la liste
            tache_a_ajouter = menu(message_nom_tache, "minimum")
            self.creation_sous_liste(tache_a_ajouter, int(len(self.liste_contenu) + 1))

        if choix_retour == "-": #supprimer une tâche présente dans la liste ==> supprimer la tache en cours (amélioration)
            position = menu(message_position_tache, type_input="nombre")
            self.supprimer_tache(position)

        if choix_retour == "/": #ajouter une tâche placée ==> placer avant la tache en cours (placer au dessus)
            position = menu(message_position_tache, type_input="nombre")
            tache_a_ajouter = menu(message_nom_tache, "minimum")
            self.creation_sous_liste(tache_a_ajouter, position)

        if choix_retour == "$": # ajouter un objet dans la LDT
            #Liste des différents objets stockables dans une LDT
            choix_objets_dispo = ["A", "D"]
            choix_objets_dispo_str = ["Quel type d'objet?: ", "- Application (A)", "- Dossier (D)"]
            type_objet = menu(print_liste(choix_objets_dispo_str), "unique", verif=True, items=choix_objets_dispo)

            if type_objet == "A": #application liste de commande
                position_app = menu(message_position_tache, type_input="nombre") #demander la position
                objet = Application(self, position_app, self.rang_indentation + 1)
                self.ajout_objet(objet, position_app)

            if type_objet == "D": #afficher le contenu d'un dossier (bugé)
                position = menu(message_position_tache, type_input="nombre")
                targeted_directory = input("Entrer un chemin: ")
                nom_dossier = dirname(targeted_directory)
                nouveau_dossier = Dossier(nom_dossier, targeted_directory, self, position, self.rang_indentation + 1)
                self.ajout_objet(nouveau_dossier, position) #ajouter l'objet à la liste

        if choix_retour == "!": # afficher/cacher le contenu de la LDT
            self.switch_show()

        if choix_retour == "m": # acces au menu module
            #sous menu
            choix_menu_module_str = ["- Sauvegarder un module (s)", "- Charger un module existant (c)", "- Annuler (a)"]
            choix_menu_module = ["s", "c", "a"]
            choix = menu(print_liste(choix_menu_module_str), "normal", verif=True, items=choix_menu_module)

            if choix == "s": #sauvegarder
                nom_module = input("Nom du fichier: ")#nommer le module
                fichier_sauvegarde_module = "sauvegardes/" + nom_module
                self.switch_hightlight() #éteindre la liste avant de l'enregistrer
                deposer_donnees(self, fichier_sauvegarde_module, "wb") #enregistrer le module
                print("Le module à été sauvegardé! il reste disponible dans le dossier \"sauvegardes\".")
                sleep(2)

            if choix == "c": #charger
                position_module = menu(message_position_tache, type_input="nombre") #demander la position
                nom_fichier = choix_fichier("sauvegardes")
                module = recuperer_donnees("sauvegardes/" + nom_fichier)
                self.ajout_objet(module, position_module) #ajouter l'objet à la liste

            if choix == "a":
                print("Annulé...")

        if choix_retour == "r": # Renommer la liste
            self.rename()

        if choix_retour == "e": #executer une app de la liste
            position_app = menu(message_position_tache, type_input="nombre") #demander la position
            try:
                self.lancer(position_app)
            except IndexError:
                print("Impossible d'executer!")

        if choix_retour == "k": #suppression de a liste
            if self.rang_indentation == 0:
                suppr_list_principale = input("Supprimer la liste Principale? (O/n)")
                if suppr_list_principale == "O":
                    self.liste_contenu = []
                    self.nom = "NinjaTODOla"
                    # supprimer le fichier correspondant
            else:
                self.self_destruct()
                return "GoListeMere"

        if choix_retour == "X": #si l'utilisateur veut couper l'objet
            if self.rang_indentation == 0:
                print("Impossible de couper la liste principale!")
                sleep(1)
            else:
                self.self_destruct()
                return self

        if choix_retour == "V": #si l'utilisateur veut coller un objet en cache
            return "coller"

class Commande(NinjatodolaObject):
    """Créé l'objet commande, utilisable dans les applications. """

    def __init__(self, liste_mere, position_liste_mere, commande=None):
        NinjatodolaObject.__init__(self, None, liste_mere, position_liste_mere, None, is_a_list=False, is_executable=False)
        self.nom_classe = "Commande" #Changer le nom de la classe pour __str__
        self.choix_objet = ["r", "e", "k"] #Liste des choix possibles
        self.choix_objet_str = ["Menu d'objet:", "- Réecrire la commande (r)", "- Executer la commande (e)", "- Supprimer la liste (k)"] #Liste des str correspondantes
        if commande:
            self.code = commande
        else:
            self.code = self.entrer_une_commande()

    def __repr__(self):
        if self.hightlight: #si le sous-lignale est actif
            return color(self.code, hightlight_COM)
        else:
            return color(self.code, couleur_COM)

    def repr_object(self):
        """returns a tuple containing a string representating the object type, its rank, its hightlight status, its representation, list_of_contend_object"""

        object_tuple = (self.nom_classe, self.rang_indentation, self.position_liste_mere, self.hightlight, self.code)
        # liste_de_tuple = []
        # liste_de_tuple.append(object_tuple)
        # return liste_de_tuple
        return object_tuple

    def entrer_une_commande(self):
        """Permet d'entrer une commande"""
        commande = input("Entrer une commande:\n> ")
        return commande

    def reecrire(self):
        """Permet de reecrire la commande"""
        self.code = input("Nouvelle commande:\n> ")

    def action_objet(self, choix_retour):
        """Traite un choix d'action spécifique à l'objet venant du menu principal"""

        if choix_retour == "r": # Renommer la liste
            self.reecrire()
        
        if choix_retour == "e":
            clear()
            print("Resultat d'execution de la commande de la commande:\n==========")
            bash(self.code)
            print("==========")
            sleep(3)

        if choix_retour == "k": #suppression de a liste
            self.self_destruct()
            return "GoListeMere"

class Application(NinjatodolaObject):
    """Objet executable contenant une liste de commandes"""
    def __init__(self, liste_mere, position_liste_mere, rang_indentation):
        clear()
        nom = menu("Entrer le nom de l'application: ", "minimum")
        NinjatodolaObject.__init__(self, nom, liste_mere, position_liste_mere, rang_indentation, is_a_list=True, is_executable=True) #Reprendre la base des attributs et fonction de la classe mere
        self.nom_classe = "Application" #Changer le nom de la classe pour __str__
        self.choix_objet = ["+", "-", "/", "!", "§", "$", "X", "r", "e", "k"] #Liste des choix possibles
        self.choix_objet_str = ["Menu d'objet:", "- Ajouter une commande (+)", "- Supprimer une commande (-)", "- Placer une commande (/)", "- Afficher/Cacher le script (!)", "- Afficher/Cacher le résultat de l'execution (§)", "- Executer une commande ($)", "- Couper (X)", "- Renommer la liste (r)", "- Executer une app de la liste (e)", "- Supprimer la liste (k)"] #Liste des str correspondantes
        self.aff = False
        #Choix du language:
        language = menu("Quel language utiliser?\n1- Bash\n2- Python3", "unique", verif=True, items=["1", "2"])
        if language == "1":
            self.lang = "bash"
        if language == "2":
            self.lang = "python3"
        #Choix nouvelle ou charger une liste
        choix = menu("Que faire? \n-Nouvelle App (N)\n- Charger depuis un script (C)\n- Stop (s))", "unique", verif=True, items=["N", "C", "s"])
        if choix == "N":
            liste_commande = input_script_list()
        elif choix == "C":
            liste_commande = input_script_from_file_list()
        else:
            liste_commande = []
            print("Aucune commandes ajoutées...")
            sleep(1)

        self.liste_contenu = []
        position = 1
        for commande in liste_commande: #transformer la liste de commande en script
            new_command = Commande(self, position, commande=commande)
            self.ajout_objet(new_command, position)
            position += 1

    def __repr__(self):
        representation = "" #initialization
        if self.aff: #Si le resultat de la liste doit etre affiché
            script_complet = "" # reconstitution du script
            for ligne in self.liste_contenu:
                script_complet = script_complet + "\n" + str(ligne.code)
            output = self.execution_output(script_complet) #recuperation du resultat de l'execution
        else:
            output = self.nom

        if self.hightlight: #Si l'objet est séléctionné
            representation += color(output, hightlight_APP) #le surligner
        else: #sinon
            if self.aff:
                representation += color(output, couleur_APP_AFF)
            else:
                representation += color(output, couleur_APP) #appliquer le theme de base
        if self.show: #Si la liste n'est pas cachée
            position = 1
            for item in self.liste_contenu: #Pour chaque item de la liste
                representation += "\n" #Aller à la ligne
                representation += color("     " * self.rang_indentation + "  {} > ".format(str(position)), couleur_indenteur)#indenter
                representation += color(repr(item), police_standard) #ecrire le nom de l'objet
                position += 1
        return representation

    def repr_object(self):
        """returns a tuple containing a string representating the object type, its rank, its hightlight status, its representation, list_of_contend_object"""
        if self.aff: #Si le resultat de la liste doit etre affiché
            script_complet = "" # reconstitution du script
            for ligne in self.liste_contenu:
                script_complet = script_complet + "\n" + str(ligne.code)
            output = self.execution_output(script_complet) #recuperation du resultat de l'execution
            object_tuple = (self.nom_classe, self.rang_indentation, self.position_liste_mere, self.hightlight, output, True)
        else:
            object_tuple = (self.nom_classe, self.rang_indentation, self.position_liste_mere, self.hightlight, self.nom, self.show)
        liste_de_tuple = []
        liste_de_tuple.append(object_tuple)

        if self.show:
            for item in self.liste_contenu: #pour chaque objet dans la liste
                repr_object_from_list_contenu = item.repr_object() #generate a liste of repr_object
                # for r in repr_object_from_list_contenu: # add each tuple in the liste
                #     liste_de_tuple.append(r)
                liste_de_tuple.append(repr_object_from_list_contenu)
        
        return liste_de_tuple

    def update(self):
        """Méthode permettant de mettre à jour la liste_mere et le rang des objets contenus"""
        for item in self.liste_contenu: #pour chaque item contenu dans l'objet
            item.liste_mere = self #identifier l'objet comme liste_mere de l'item
            item.rang_indentation = self.rang_indentation + 1 #permet une indentation correcte
            item.position_liste_mere = self.find_contenu(item) #se trouver dans la liste mere
            item.switch_hightlight(turn_on=False)

    def self_execut(self):
        """executer la commande"""
        script_complet = "" #str contenant toutes les commandes séparées par des \n
        for ligne in self.liste_contenu:
            script_complet = script_complet + "\n" + str(ligne.code)
        print("="*30 + "\n")
        if self.lang == "bash":
            bash(script_complet)
        elif self.lang == "python3":
            exec(script_complet)
        else:
            print("Erreur, le language {} n'est pas pris en charge".format(self.lang))
            sleep(1)

    def execution_output(self, script):
        """Renvoi l'output du script en fonction du language"""
        if self.lang == "bash":
            output = getoutput(script)
        elif self.lang == "python3":
            output = "Impossible d'afficher le résultat d'execution en python..." # A implémenter
            # utiliser bash(python3 script)
        else:
            output = "Erreur, le language {} n'est pas pris en charge".format(self.lang)
        return output

    def switch_aff(self):
        """Permet de controler l'affichage du resultat de l'execution"""
        if self.aff:
            self.aff = False
        else:
            self.aff = True

    def inserer_commande(self, position, new_commande=None):
        """Permet la création et l'ajout d'une sous-liste à la position donnée"""
        objet = Commande(self, position, commande=new_commande)
        self.ajout_objet(objet, position)
        return objet

    def supprimer_commande(self, position):
        """supprime une tâche à la position précisée"""
        try:
            del self[position - 1]
        except IndexError:
            print("La position n'existe pas!")
            sleep(1)

    def action_objet(self, choix_retour):
        """Traite un choix d'action spécifique à l'objet venant du menu principal"""

        if choix_retour == "r": # Renommer la liste
            self.rename()

        if choix_retour == "e": #executer une app de la liste
            self.self_execut()

        if choix_retour == "k": #suppression de a liste
            self.self_destruct()
            return "GoListeMere"

        if choix_retour == "X": #si l'utilisateur veut couper l'objet
            self.self_destruct()

            return self

        elif choix_retour == "+":
            self.inserer_commande(len(self.liste_contenu) + 1)

        elif choix_retour == "-":
            position = menu("Entrer la position: ", type_input="nombre")
            self.supprimer_commande(position)

        elif choix_retour == "/":
            position = menu("Entrer la position: ", type_input="nombre")
            self.inserer_commande(position)

        elif choix_retour == "$":
            print("pas encore implémenté")

        elif choix_retour == "!":
            self.switch_show()

        elif choix_retour == "§":
            self.switch_aff()

class Separateur(NinjatodolaObject):
    """En cours de fabrication..."""
    def __init__(self, liste_mere, position_liste_mere, rang_indentation):
        NinjatodolaObject.__init__(self, "None", liste_mere, position_liste_mere, rang_indentation, is_a_list=False, is_executable=False)
        self.nom_classe = "Separateur"
        self.choix_objet = ["k", "X"]
        self.choix_objet_str = ["\nMenu d'objet:", "- Supprimer le séparateur (k)", "- Couper (X)"]

    def __repr__(self):
        motif = "    __________\n"
        representation = ""
        if self.hightlight == True:
            representation += color(motif, hightlight_SEP)
        else:
            representation += color(motif, couleur_SEP)
        return representation

    def repr_object(self):
        """returns a tuple containing a string representating the object type, its rank, its hightlight status, its representation, list_of_contend_object"""

        object_tuple = (self.nom_classe, self.rang_indentation, self.position_liste_mere, self.hightlight, "")
        liste_de_tuple = []
        liste_de_tuple.append(object_tuple)

        return liste_de_tuple

    def action_objet(self, choix_retour):
        """Traite un choix d'action spécifique à l'objet venant du menu principal"""

        if choix_retour == "k": # Supprimer le séparateur
            self.self_destruct()
            return "GoListeMere"

        if choix_retour == "X": #si l'utilisateur veut couper l'objet
            self.self_destruct()
            return self

class Dossier(NinjatodolaObject):
    """Objet dossier."""
    def __init__(self, nom, loc_dossier, liste_mere, position_liste_mere, rang_indentation):
        NinjatodolaObject.__init__(self, nom, liste_mere, position_liste_mere, rang_indentation, is_a_list=True, is_executable=False)
        self.nom_classe = "Dossier" #Changer le nom de la classe pour __str__
        self.choix_objet = ["!", "r", "j", "-", "d", "f", "X", "V"] #Liste des choix possibles
        self.choix_objet_str = ["\nMenu d'objet:", "- Montrer/Cacher (!)", "- Renommer (r)", "- Créer un nouveau dossier (d)", "- Créer un nouveau fichier (f)", "- Mettre à jour le dossier (j)", "- Supprimer le dossier (-)", "- Copier le Dossier (X)", "- Coller le Dossier/Fichier (V)"] #Liste des str correspondantes
        if not isinstance(self.liste_mere, Dossier):
            self.choix_objet_str.insert(7, "- Supprimer l'objet dossier (k)")
            self.choix_objet.append("k")
        self.loc_dossier = loc_dossier
        # self.remplir_objet()
        self.show = False
        self.existe = True

    def __repr__(self):
        representation = ""
        if self.existe:
            if self.hightlight: #Si l'objet est séléctionné
                representation += color(self.nom, hightlight_DOS) #le surligner
                self.update_dossier() # Mettre le dossier à jour quand il est sélectionné
            else: #sinon
                representation += color(self.nom, couleur_DOS) #appliquer le theme de base
            if self.show: #Si la liste n'est pas cachée
                position = 0
                for item in self.liste_contenu: #Pour chaque item de la liste
                    position += 1
                    representation += "\n" #Aller à la ligne
                    representation += color("     " * (self.rang_indentation + 1) + "|-> ", couleur_indenteur)#indenter
                    representation += color(str(position)+ ".", couleur_numero_position)#ecrire la position dans la liste
                    representation += repr(item) #ecrire le nom de l'objet
            else: #Si la liste est cachée
                representation += color(" ...", couleur_indenteur) #Ne rien montrer
        else:
            if self.hightlight: #Si l'objet est séléctionné
                representation += color(self.nom, hightlight_DOS) #le surligner
            else: #sinon
                representation += color(self.nom, couleur_DOS) #appliquer le theme de base
            self.nom = color("Le dossier n'existe plus...", couleur_rouge)
        return representation

    def repr_object(self):
        """returns a tuple containing a string representating the object type, its rank, its hightlight status, its representation, list_of_contend_object"""
        if self.existe:
            # self.update_dossier()
            pass
        else:
            self.nom = "Le dossier n'existe plus"
        object_tuple = (self.nom_classe, self.rang_indentation, self.position_liste_mere, self.hightlight, self.nom, self.show)
        liste_de_tuple = []
        liste_de_tuple.append(object_tuple)

        if self.show:
            for item in self.liste_contenu: #pour chaque objet dans la liste
                repr_object_from_list_contenu = item.repr_object() #generate a liste of repr_object
                for r in repr_object_from_list_contenu: # add each tuple in the liste
                    liste_de_tuple.append(r)
        return liste_de_tuple

    def switch_hightlight(self, turn_on=False):
        """Change le status du surlignage"""
        if turn_on:
            self.hightlight = True
            self.update_dossier()
        else:
            self.hightlight = False

    def update(self):
        """Void"""
        self.existe = path.exists(self.loc_dossier)#verifier que le fichier existe toujour (sous ce nom)
        if self.existe:
            pass
        else:
            self.nom = "Le dossier n'existe plus"

        if not isinstance(self.liste_mere, Dossier):
            str_supprimer_objet = "- Supprimer l'objet dossier (k)"
            item_supprimer_objet = "k"
            if item_supprimer_objet not in self.choix_objet:
                self.choix_objet_str.insert(7, str_supprimer_objet)
                self.choix_objet.append(item_supprimer_objet)

    def update_dossier(self):
        """Mettre à jour le dossier"""
        self.liste_contenu = []
        self.remplir_objet()

    def remplir_objet(self):
        """Remplissage du Dossier avec les sous-dossier et les fichiers"""
        contenu = list_dir_dirs_files(self.loc_dossier)
        list_dirs = contenu[0]
        list_files = contenu[1]
        position = 1
        for item in list_dirs:
            loc_sous_dossier = self.loc_dossier + item + "/"
            objet_a_ajouter = Dossier(item, loc_sous_dossier, self, position, self.rang_indentation + 1)
            self.ajout_objet(objet_a_ajouter, position)
            position += 1
        for item in list_files:
            loc_fichier = self.loc_dossier + str(item)
            objet_a_ajouter = Fichier(item, self, position, loc_fichier)
            self.ajout_objet(objet_a_ajouter, position)
            position += 1

    def action_objet(self, action_retour):
        """Actions possibles sur l'objet"""
        if action_retour == "!":
            self.switch_show()
        
        if action_retour == "j":
            self.update_dossier()

        if action_retour == "-":
            supprimer = input("Confirmer la suppression? (O/n)\n")
            if supprimer == "O":
                bash("rm -r \"" + self.loc_dossier + "/\"")
                print("Suppression en cours...")
                return "GoListeMere"
            else:
                print("Annulé...")
        
        if action_retour == "r":
            if isinstance(self.liste_mere, Dossier):
                nouveau_nom = input("Nouveau nom: ")
                self.liste_mere.update_dossier()
                bash("mv " + self.loc_dossier + " " + self.liste_mere.loc_dossier + "/" + nouveau_nom)
            else:
                self.rename()
            return "GoListeMere"
        
        if action_retour == "d":
            nom_dossier = input("Nom du dossier: ")
            bash("mkdir " + self.loc_dossier + nom_dossier)
            self.update_dossier()

        if action_retour == "f":
            nom_fichier = input("Nom du fichier: ")
            bash("touch " + self.loc_dossier + nom_fichier)
            self.update_dossier()

        if action_retour == "X":
            return self
        
        if not isinstance(self.liste_mere, Dossier):
            if action_retour == "k":
                self.self_destruct()
                return "GoListeMere"
        
        if action_retour == "V": #si l'utilisateur veut coller un objet en cache
            return "coller"

class Fichier(NinjatodolaObject):
    """Créé l'objet commande, utilisable dans les applications. """

    def __init__(self, nom, liste_mere, position_liste_mere, loc_fichier):
        NinjatodolaObject.__init__(self, nom, liste_mere, position_liste_mere, liste_mere.rang_indentation, is_a_list=False, is_executable=False)
        self.nom_classe = "Fichier" #Changer le nom de la classe pour __str__
        self.choix_objet = ["e", "r", "m", "i", "l", "k"] #Liste des choix possibles
        self.choix_objet_str = ["\nMenu d'objet:", "- Executer le fichier (e)", "- Renommer le fichier (r)", "- Modifier le fichier (m)", "- Infos sur le fichier (i)", "- Lire le fichier (l)", "- Supprimer le fichier (k)"] #Liste des str correspondantes
        self.loc_fichier = loc_fichier
        self.loc_dir_conteneur = dirname(loc_fichier, True)
        self.existe = True

    def __repr__(self):
        if self.hightlight: #si le sous-lignale est actif
            self.update()
            if self.existe:
                return color(self.nom, hightlight_FIC)
            else:
                self.nom = "Le fichier n'existe plus"
                return color(self.nom, hightlight_FIC)
        else:
            return color(self.nom, couleur_FIC)

    def repr_object(self):
        """returns a tuple containing a string representating the object type, its rank, its hightlight status, its representation, list_of_contend_object"""

        object_tuple = (self.nom_classe, self.rang_indentation, self.position_liste_mere, self.hightlight, self.nom)
        liste_de_tuple = []
        liste_de_tuple.append(object_tuple)

        return liste_de_tuple

    def update(self):
        existe = path.exists(self.loc_fichier)#verifier que le fichier existe toujour (sous ce nom)
        if existe:
            pass
        else:
            self.nom = "Le fichier n'existe plus"

    def action_objet(self, choix_retour):
        """Traite un choix d'action spécifique à l'objet venant du menu principal"""
        if choix_retour == "e":
            print("="*30)
            bash("exec \"" + self.loc_fichier + "\"") #executer le fichier
        
        if choix_retour == "m":
            print("="*30)
            bash("vim \"" + self.loc_fichier + "\"") #executer le fichier
        
        if choix_retour == "i":
            print("Pas encore implémenté...") #infos sur le fichier
        
        if choix_retour == "l":
            bash("less \"" + self.loc_fichier + "\"")
        
        if choix_retour == "r":
            nouveau_nom = input("Nouveau nom: ")
            #### bug si la liste mere est une LDT ###
            bash("mv \"" + self.loc_fichier + "\"" + " \"" + self.loc_dir_conteneur + nouveau_nom + "\"")
            self.nom = nouveau_nom
            return "GoListeMere"

        if choix_retour == "k":
            if self.existe:
                supprimer = input("Confirmer la suppression? (O/n)\n")
                if supprimer == "O":
                    bash("rm \"" + self.loc_fichier + "\"")
                    print("Suppression en cours...")
                    return "GoListeMere"
                else:
                    print("Annulé...")

        if choix_retour == "X":
            return self

class LienLDT():
    """..."""

class ListeParametre(NinjatodolaObject):
    """Contient des objets Parametre"""

class Parametre():
    """Contient un ensemble d'attr parametre avec une methode de modification propre à chaque attr et une methode d'exportation des parametres"""

class TacheSequentielle(ListeDeTaches):
    """En cours de fabrication..."""

class TacheProgrammable(ListeDeTaches):
    """En cours de fabrication..."""