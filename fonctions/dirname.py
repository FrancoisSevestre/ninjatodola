def dirname(my_path, full_path=False):
    """Return the name of the last directory in the path: /x/y/ ==> y ; /x/y ==> x \\
    if full_path: /x/y/z ==> /x/y/ ; /x/y/ ==> /x/y/"""
    list_dir = []
    directory = ""
    for character in my_path:
        if character == "/":
            list_dir.append(directory)
            directory = ""
        else:
            directory += character
    if full_path:
        full_path = ""
        for directory in list_dir:
            full_path += directory + "/"
        return full_path
    else:
        return list_dir[-1]

if __name__ == "__main__":
    a = dirname("/home/francois/fichier")
    print(a)