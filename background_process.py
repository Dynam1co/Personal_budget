"""Used for background tasks:
    - Import excel files
    - Process excel files
    - Categorize entries"""


import bank_excel_mgt
import myconstants
from pony.orm import db_session
from pony.orm.core import select
import entities
import categorize


def create_entry_types():
    with db_session:
        for di in myconstants.EXPENSE_TYPE:
            if not expense_type_exists(di["name"], di["periodicity"]):
                entities.ExpenseType(name=di["name"], periodicity=di["periodicity"])


def expense_type_exists(name, period):
    obj_types = select(
        t for t in entities.ExpenseType if t.name == name and t.periodicity == period
    )

    return obj_types.count() > 0


def main():
    create_entry_types()

    bank_excel_mgt.run_import_process()

    categorize.categorize_new_entries()


if __name__ == "__main__":
    main()
