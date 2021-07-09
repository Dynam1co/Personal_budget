from pony.orm.core import select
import myconstants
import os
from os import walk
import xlrd
from pony.orm import db_session
import entities


def run_import_process():
    # Get files to process
    files_to_process = get_input_files(myconstants.PROCESS_PATH)

    # Get all rows of files to process
    file_rows = [import_file(file) for file in files_to_process]

    # Store in database
    [insert_row_data(row) for rows in file_rows for row in rows]

    # Move to processed folder
    [move_file_to_processed(file) for file in files_to_process]


def get_input_files(path):
    os.chdir(path)

    processed_list = [
        file for (dirpath, dirnames, filenames) in walk(path) for file in filenames
    ]

    return processed_list


def import_file(file):
    wb = xlrd.open_workbook(file)

    sheet_obj = wb.sheet_by_index(0)
    max_row = sheet_obj.nrows
    initial_row = int(myconstants.INITIAL_ROW)

    # Extract data for each row
    rows = [sheet_obj.row(cur_row) for cur_row in range(initial_row, max_row)]

    return rows


def insert_row_data(row):
    # Extract fields and insert into database
    DATE_POS = 0
    CAT_POS = 1
    SUBCAT_POS = 2
    DESC_POS = 3
    AMOUNT_POS = 6
    BALANCE_POS = 7

    entry_date_time = xlrd.xldate_as_datetime(row[DATE_POS].value, 0)
    entry_date = entry_date_time.date()

    category = row[CAT_POS].value
    sub_category = row[SUBCAT_POS].value
    description = row[DESC_POS].value
    amount = row[AMOUNT_POS].value
    balance = row[BALANCE_POS].value

    with db_session:
        ing_cat = insert_category_if_not_exists(category)

        ing_subcategory = insert_subcategory_if_not_exists(sub_category)

        if not entry_exists(entry_date, description, amount):
            entities.BankEntry(
                entryDate=entry_date,
                ingCategory=ing_cat.id,
                ingSubcategory=ing_subcategory.id,
                amount=amount,
                balance=balance,
                description=description,
            )


def entry_exists(entry_date, entry_description, amount):
    obj_entry = select(
        e
        for e in entities.BankEntry
        if e.entryDate == entry_date and e.description == entry_description
    )

    ret = obj_entry.filter(lambda s: s.amount == amount)

    return ret.count() > 0


def insert_subcategory_if_not_exists(subcategory_name):
    obj_subcategory = select(
        s for s in entities.IngSubcategory if s.name == subcategory_name
    )

    if obj_subcategory.count() == 0:
        return entities.IngSubcategory(name=subcategory_name)

    return obj_subcategory.first()


def insert_category_if_not_exists(cat_name):
    obj_category = select(c for c in entities.IngCategory if c.name == cat_name)

    if obj_category.count() == 0:
        return entities.IngCategory(name=cat_name)

    return obj_category.first()


def move_file_to_processed(file):
    # Move file to processed folder
    initial_path = f"{myconstants.PROCESS_PATH}/{file}"
    final_path = f"{myconstants.PROCESSED_PATH}/{file}"

    os.rename(initial_path, final_path)
