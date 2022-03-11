import csv
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

with open('Trend Data 2022-02-03.csv') as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        ws.append(row)

wb.save('Trend Data 2022-02-03_copy_copy.xlsx')
