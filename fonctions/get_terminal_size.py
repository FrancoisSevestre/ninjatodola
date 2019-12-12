import os

def get_terminal_size():
    """Return a tuple, number of rows, number of columns. (int, int)"""
    rows, columns = os.popen('stty size', 'r').read().split()
    return (rows, columns)

if __name__ == "__main__":
    a = get_terminal_size()
    print("Il y a {} lignes et {} colonnes".format(a[0], a[1]))