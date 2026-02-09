from openpyxl import Workbook
workbook=Workbook()
worksheet=workbook.active
worksheet.title='information'
worksheet['A1']="A"
worksheet['B1']="B"
worksheet['C1']="C"
workbook.save("san.xlsx")