import xlrd

def parse_to_dictionary(workbook_path):
    workbook = xlrd.open_workbook(workbook_path)
    worksheet = workbook.sheet_by_index(0)

    first_row = []  # The row where we stock the name of the column
    for col in range(worksheet.ncols):
        first_row.append(worksheet.cell_value(0, col))

    # transform the workbook to a dictionary of dictionaries
    data = {}
    for row in range(1, worksheet.nrows):
        elm = {}
        for col in range(1, worksheet.ncols):
            if worksheet.cell_value(row, col):
                elm[first_row[col]] = worksheet.cell_value(row, col)
        data[worksheet.cell_value(row, 0)] = elm
    
    return data