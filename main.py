import os
from bcolor import bcolors


def print_menu():
    os.system("clear")
    print(f"{bcolors.OKBLUE}Seleccione opción{bcolors.NORMAL}")
    print(f"\t{bcolors.OKGREEN}1 -{bcolors.NORMAL} Ver movimientos pendientes")
    print(f"\t{bcolors.OKGREEN}2 -{bcolors.NORMAL} segunda opción")
    print(f"\t{bcolors.OKGREEN}3 -{bcolors.NORMAL} tercera opción")
    print(f"\t{bcolors.OKGREEN}9 -{bcolors.NORMAL} salir")


if __name__ == "__main__":
    exit = False

    while not exit:
        print_menu()
        menu_option = input(
            f"\n{bcolors.OKBLUE}{bcolors.UNDERLINE}Opción{bcolors.NORMAL}{bcolors.OKBLUE} >> {bcolors.NORMAL}"
        )

        if menu_option == "9":
            print(f"\n{bcolors.RED}Fin programa.{bcolors.NORMAL}")
            exit = True
