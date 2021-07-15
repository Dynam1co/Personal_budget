"""Used for main program tasks:
    - Show entries pending categorize
    - Categorize entries
    - Show reports"""


import os
from bcolor import bcolors
from pony.orm import db_session
from pony.orm.core import ObjectNotFound, select
import entities
from prettytable import PrettyTable


def get_pending_entries():
    return select(
        e
        for e in entities.BankEntry
        if e.ownCategory is None or e.ownSubcategory is None
    )[:]


def print_pending_entries():
    """Print table for pending entries"""
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
    """Return tablerow from entry"""
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


def start_entry_categorization():
    """Init categorization process"""
    entry_id = input(
        f"\n{bcolors.OKBLUE}Movimiento a categorizar (0 para salir){bcolors.OKBLUE} >> {bcolors.NORMAL}"
    )

    if entry_id == "0":
        return

    if not entry_exists(entry_id):
        print(f"\n{bcolors.RED}Movimiento no encontrado{bcolors.NORMAL}")
        return start_entry_categorization()

    if not entry_is_pending(entry_id):
        print(
            f"\n{bcolors.RED}Movimiento: {entry_id} no está pendiente de categorizar{bcolors.NORMAL}"
        )
        return start_entry_categorization()

    # TODO: Print categories
    # TODO: Print subcategories
    # TODO: Apply category and sub categories


@db_session
def entry_is_pending(entry_id):
    entry = entities.BankEntry[entry_id]

    return entry.ownCategory is None or entry.ownSubcategory is None


@db_session
def entry_exists(entry_id):
    try:
        entities.BankEntry[entry_id]
    except ObjectNotFound:
        return False

    return True


def print_menu():
    print(f"{bcolors.OKBLUE}Seleccione opción{bcolors.NORMAL}")
    print(
        f"\t{bcolors.OKGREEN}1 -{bcolors.NORMAL} Ver movimientos pendientes clasificar"
    )
    print(f"\t{bcolors.OKGREEN}2 -{bcolors.NORMAL} Categorizar movimiento")
    print(f"\t{bcolors.OKGREEN}3 -{bcolors.NORMAL} Crear nuevo mapeo categorías")
    print(f"\t{bcolors.OKGREEN}4 -{bcolors.NORMAL} Dividir movimientos")
    print(f"\t{bcolors.OKGREEN}0 -{bcolors.NORMAL} Salir")


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

        elif menu_option == "2":
            start_entry_categorization()

        elif menu_option == "0":
            print(f"\n{bcolors.RED}Fin programa.{bcolors.NORMAL}")
            exit = True
