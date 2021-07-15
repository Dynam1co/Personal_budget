"""Used for main program tasks:
    - Show entries pending categorize
    - Categorize entries
    - Show reports"""


import os
from bcolor import bcolors
from pony.orm import db_session
from pony.orm.core import select
import entities
from prettytable import PrettyTable


def get_pending_entries():
    return select(
        e
        for e in entities.BankEntry
        if e.ownCategory is None or e.ownSubcategory is None
    )[:]


def print_pending_entries():
    entries = get_pending_entries()

    x = PrettyTable()

    x.field_names = get_colnames()

    rows = [get_row(entry) for entry in entries]

    x.add_rows(rows)

    print("")
    print(x)
    print("")


def get_colnames():
    return [
        "Id",
        "Entry date",
        "ING Category Id",
        "ING Category Name",
        "ING Subcategory Id",
        "ING Subcategory Name",
        "Own Category Id",
        "Own Subcategory Id",
        "Amount",
        "Description",
        "Expense Type",
    ]


def get_row(entry):
    fields = [
        entry.id,
        entry.entryDate,
        entry.ingCategory.id,
        entry.ingCategory.name,
        entry.ingSubcategory.id,
        entry.ingSubcategory.name,
        entry.ownCategory,
        entry.ownSubcategory,
        entry.amount,
        entry.description,
        entry.expenseType,
    ]

    return fields


def print_menu():
    print(f"{bcolors.OKBLUE}Seleccione opción{bcolors.NORMAL}")
    print(
        f"\t{bcolors.OKGREEN}1 -{bcolors.NORMAL} Ver movimientos pendientes clasificar"
    )
    print(f"\t{bcolors.OKGREEN}2 -{bcolors.NORMAL} Categorizar movimiento")
    print(f"\t{bcolors.OKGREEN}3 -{bcolors.NORMAL} Crear nuevo mapeo categorías")
    print(f"\t{bcolors.OKGREEN}4 -{bcolors.NORMAL} Dividir movimientos")
    print(f"\t{bcolors.OKGREEN}9 -{bcolors.NORMAL} Salir")


if __name__ == "__main__":
    exit = False
    os.system("clear")

    while not exit:
        print_menu()
        menu_option = input(
            f"\n{bcolors.OKBLUE}{bcolors.UNDERLINE}Opción{bcolors.NORMAL}{bcolors.OKBLUE} >> {bcolors.NORMAL}"
        )

        if menu_option == "1":
            with db_session:
                print_pending_entries()

        elif menu_option == "9":
            print(f"\n{bcolors.RED}Fin programa.{bcolors.NORMAL}")
            exit = True
