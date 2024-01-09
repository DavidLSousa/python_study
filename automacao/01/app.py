from openpyxl import workbook
import openpyxl

wb = openpyxl.load_workbook('automacao/01/teste_01.xlsx')
sheet_teste_01 = wb['Planilha1']

data = []

for row in sheet_teste_01.iter_rows(min_row=2):
  data.append({
    'produto': row[0].value, 
    'Quantidade': row[1].value, 
    'Preço': row[2].value
  })

for dicItem in data:
  if (dicItem['Quantidade'] <= 2):
    print(type(dicItem['Quantidade']))
    print(dicItem)

# for item in data:
#   print(item)
