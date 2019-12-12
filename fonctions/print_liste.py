#main
def print_liste(liste):
    output = ""
    for place in range(0, len(liste)):
        output += str(liste[place]) + "\n"
    return output

if __name__ == "__main__":
    items_menu_principal_str = ["- Ajouter une tâche (+)", "- Supprimer une tâche (-)", "- Placer une tâche (/)", "- Créer/Importer une application ($)", "- Executer (e)", "- Développer/Réduire (!)", "- Monter dans l'arborescence (4)", "- Descendre dans l'arborescence (6)", "- Naviguer vers le bas (2)", "- Naviguer vers le haut (8)", "- Menu module (m)", "- Options (o)", "- Renommer une liste (r)", "- Quitter (q)", "- Console ()", "- Couper (X)", "- Coller (V)", "- Dossier (D)"]
    print(print_liste(items_menu_principal_str))