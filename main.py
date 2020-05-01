#!/usr/bin/venv python

import xlrd
#----------------------------------------------------------------------
def open_file(path):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)

    # get the first worksheet
    sheets = book.sheet_by_index(0)


    for cell in sheets.row(2):
        print(cell.value)


#----------------------------------------------------------------------
if __name__ == "__main__":
    path = "sheets/d.xls"
    open_file(path)

