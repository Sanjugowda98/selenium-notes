import xlrd
xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter=True
path=r'C:\Users\smahes5x\PycharmProjects\selenium_training\how_to_write_in_xls\san.xlsx'

workbook=xlrd.open_workbook(path)

worksheet=workbook.sheet_by_name("information")

rows=worksheet.get_rows()
print(rows)

for ele in rows:
    print(ele[0].value,ele[1].value)


