from fonctions.get_terminal_size import get_terminal_size
from time import sleep
def compose_output(output_left, output_right, right_space):
    """Return a str composed of the 2 given str with space at right."""
    #implement left space
    output_left = output_left.split("\n") #split into lines
    output_right = output_right.split("\n")
    terminal_width = get_terminal_size()[1]
    general_output = ""
    pos = 0
    while True:
        try:
            part1 = output_left[pos]
            part3 = output_right[pos]
            part1_space = len(part1)
            part_supp_space = right_space
            remaining_space = int(terminal_width) - int(part1_space) - part_supp_space
            part2 = " "*remaining_space
            comp = part1 + part2 + part3 + "\n"

            #verifier la taille de la ligne
            if remaining_space <= 0:
                comp = part1 + "\n" + " "*(int(terminal_width) - part_supp_space) + part3 + "\n" #sauter une ligne avant la part2

            general_output += comp
            pos += 1
        except IndexError:
            break
    return general_output


def compose_output2(output_left, output_right, right_space):
    """Return a str composed of the 2 given str with space at right."""
    #implement left space
    output_left = output_left.split("\n") #split into lines
    output_right = output_right.split("\n")
    terminal_width = int(get_terminal_size()[1])
    general_output = ""
    pos = 0
    while True:
        try:
            output_ligne = ""
            part1 = output_left[pos]
            part2 = output_right[pos]
            output_ligne = " "*(terminal_width - right_space)
            output_ligne += part2 + "\n"
            output_ligne += "\b"*terminal_width
            output_ligne += part1




            general_output += output_ligne
            pos += 1
        except IndexError:
            break
    return general_output

