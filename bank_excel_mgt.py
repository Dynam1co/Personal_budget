import myconstants
import os
from os import walk
import xlrd


def run_import_process():
    process_input_files(myconstants.PROCESS_PATH)

    # TODO: Move processed files


def process_input_files(path):
    os.chdir(path)

    processed_list = [
        import_file(file)
        for (dirpath, dirnames, filenames) in walk(path)
        for file in filenames
    ]

    print(processed_list)


def import_file(file):
    wb = xlrd.open_workbook(file)

    sheet_obj = wb.sheet_by_index(0)
    max_row = sheet_obj.nrows
    initial_row = int(myconstants.INITIAL_ROW)

    # Extrat data for each row and insert into database
    [get_row_data(sheet_obj.row(cur_row)) for cur_row in range(initial_row, max_row)]

    return file


def get_row_data(row):
    # TODO: Extrat fields and insert into database
    pass
