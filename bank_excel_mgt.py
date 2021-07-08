import myconstants
import os
from os import walk
import xlrd


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
    # TODO: Extract fields and insert into database
    pass


def move_file_to_processed(file):
    # TODO: Move file to processed folder
    pass
