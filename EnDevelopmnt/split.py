from time import sleep
from get_terminal_size import get_terminal_size

terminal_width = get_terminal_size()[1]

with open("output1.txt", "r") as fichier:
    a = fichier.read()
with open("output2.txt", "r") as fichier:
    b = fichier.read()

a = a.split("\n")
b = b.split("\n")


def compose_output(output_left, output_right, right_space):
    pos = 0
    while True:
        try:
            part1 = output_left[pos]
            part3 = output_right[pos]
            part1_space = len(part1)
            part_supp_space = right_space
            remaining_space = int(terminal_width) - int(part1_space) - part_supp_space
            part2 = " "*remaining_space
            comp = part1 + part2 + part3

            #verifier la taille de la ligne
            if remaining_space <= 0:
                comp = part1 + "\n" + " "*(int(terminal_width) - part_supp_space) + part3 #sauter une ligne avant la part2

            print(comp)
            pos += 1
        except IndexError:
            break

if __name__ == "__main__":
    compose_output(a, b, 35)