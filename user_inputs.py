from api import *
import pandas as pd

csv_location = input("Enter the address of the csv file: ")
df = pd.read_csv(csv_location)
print("1. Insert into existing Spreadsheet\n2. Create new Spreadsheet")
choice = int(input())
if choice == 1:
    sheet_name = input("Enter the name of the existing sheet: ")
    sh = gc.open(sheet_name)
    
else:
    sheet_name = input("New sheet name: ")
    sh = gc.create(sheet_name)

for j in sh.worksheets():
        print(j)
ws = input("Select a worksheet: ")
try:
    worksheet = sh.worksheet(ws)
except:
     worksheet = sh.add_worksheet(ws, rows=1000, cols=1000)

for col in df.columns:
     col_choice = input(f"Do you want to include the column {col}?(Y/N)\n")
     if col_choice == "N":
          del df[col]
          print(f"Deleted {col}")

print(df.head)
worksheet.update([df.columns.values.tolist()] + df.values.tolist())
