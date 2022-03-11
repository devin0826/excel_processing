# excel_processing

errors i see when running cvs_to_xlsx_folder

/Users/Devin/PycharmProjects/pythonProject3/HelloWorld/venv/bin/python /Users/Devin/PycharmProjects/pythonProject3/HelloWorld/cvs_to_xlsx_folder.py
/Users/Devin/PycharmProjects/pythonProject3/HelloWorld/test_files/Trend Data 2022-01-11 (35 min).csv
Traceback (most recent call last):
  File "/Users/Devin/PycharmProjects/pythonProject3/HelloWorld/cvs_to_xlsx_folder.py", line 15, in <module>
    for row in reader:
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x81 in position 18: invalid start byte
