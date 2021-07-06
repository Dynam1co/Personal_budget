import os
from os import walk
from dotenv import load_dotenv
import xlrd

load_dotenv()


def run_import_process():
    process_path = os.getenv('PROCESS_PATH')
    processed_path = os.getenv('PROCESSED_PATH')

    process_input_files(process_path)


def process_input_files(path):
    os.chdir(path)

    processed_list = [import_file(file) for (dirpath, dirnames, filenames) in walk(path) for file in filenames]

    print(processed_list)


def import_file(file):
    wb = xlrd.open_workbook(file)

    sheet_obj = wb.sheet_by_index(0)
    max_col = sheet_obj.ncols
    max_row = sheet_obj.nrows

    for cur_row in range(0, max_row):
        for cur_col in range(0, max_col):
            cell = sheet_obj.cell(cur_row, cur_col)
            print(cell.value)

    return file
