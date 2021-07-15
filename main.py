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

    # Print and select categories
    cat_id = select_category()

    if cat_id == 0:
        return

    # Print and select subcategories
    subcat_id = select_subcategory(cat_id)

    if subcat_id == 0:
        return

    # Apply category and sub categories to entry
    apply_categories_to_entry(int(entry_id), int(cat_id), int(subcat_id))

    print(f"\n{bcolors.OKGREEN}Correcto.{bcolors.NORMAL}\n")


@db_session
def apply_categories_to_entry(entry_id, category_id, subcategory_id):
    entry = entities.BankEntry[entry_id]

    entry.ownCategory = category_id
    entry.ownSubcategory = subcategory_id


def select_subcategory(cat_id):
    subcategories = get_own_subcategories(cat_id)

    subcategories_id = [subcat.id for subcat in subcategories]

    print(f"\n{bcolors.OKBLUE}Seleccione categoría:{bcolors.NORMAL}")

    for subcategory in subcategories:
        print(f"\t{subcategory.id} - {subcategory.name}")

    subcat_id = input(
        f"\n{bcolors.OKBLUE}Subcategoría (0 para salir) >> {bcolors.NORMAL}"
    )

    if subcat_id == "0":
        return 0

    if int(subcat_id) not in subcategories_id:
        print(f"\n{bcolors.RED}La Subcategoría no existe{bcolors.NORMAL}")
        return select_subcategory(cat_id)

    return subcat_id


def select_category():
    categories = get_own_categories()

    categories_ids = [cat.id for cat in categories]

    print(f"\n{bcolors.OKBLUE}Seleccione categoría:{bcolors.NORMAL}")

    for category in categories:
        print(f"\t{category.id} - {category.name}")

    cat_id = input(f"\n{bcolors.OKBLUE}Categoría (0 para salir) >> {bcolors.NORMAL}")

    if cat_id == "0":
        return 0

    if int(cat_id) not in categories_ids:
        print(f"\n{bcolors.RED}La categoría no existe{bcolors.NORMAL}")
        return select_category()

    return cat_id


@db_session
def get_own_categories():
    return select(c for c in entities.OwnCategory)[:]


@db_session
def get_own_subcategories(parent_category_id):
    return select(
        c
        for c in entities.OwnSubcategory
        if c.main_category.id == int(parent_category_id)
    )[:]


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
