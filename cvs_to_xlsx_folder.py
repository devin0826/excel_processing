from pathlib import Path


path = Path('/Users/Devin/PycharmProjects/pythonProject3/HelloWorld/test_files')
for file in path.glob('*.csv'):
        import csv
        import openpyxl

        print(file)
        wb = openpyxl.Workbook()
        ws = wb.active

        with open(file) as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                        ws.append(row)
        wb.save(file[0:-4] + '.xlsx')