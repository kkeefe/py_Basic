#!/usr/local/bin/python3

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import PrettyPrinter as pp

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name("client2_stuff.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Test Spread Sheet").sheet1

p1 = pp()
legislators = sheet.get_all_records()
p1.pprint(legislators)

# returns list of cols..
row1 = sheet.row_values(1)
row2 = sheet.row_values(2)
row3 = sheet.row_values(3)
p1.pprint(row1)
p1.pprint(row2)
p1.pprint(row3)

# returns list of cols..
col1 = sheet.col_values(1)
col2 = sheet.col_values(2)
col3 = sheet.col_values(3)
p1.pprint(col1)
p1.pprint(col2)
p1.pprint(col3)

# returns cell object
result = sheet.cell(1, 3)
print("result is: ", result.value)

# update a specific cell:
for i in range(1, 11):
    sheet.update_cell(10, i, i*i)
print("update complete..")
