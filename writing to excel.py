import xlsxwriter
def writer(listname,tenantname):
    row = 1
    column = 0
    for item in listname.get(tenantname):
        worksheet.write(row, column, item)
        row += 1
    row = 1
    column = 1
    for item in listname.get(tenantname):
        worksheet.write(row, column,tenantname)
        row +=1
        workbook.close()

a = input ("Enter First Tenant Name: ")
content = {'alpha': [33, 42, 8, 2, 13, 19, 43, 50, 31, 45, 32, 17, 47],
 'beta': [7, 20, 35, 28, 49, 34, 27, 48, 12, 21, 14, 24, 39],
 'gamma': [44, 26, 15, 25, 52, 3, 30, 41, 16, 37, 46, 4, 36],
 'Lambda': [18, 9, 5, 22, 11, 6, 51, 1, 29, 38, 10, 23, 40]}

workbook = xlsxwriter.Workbook('Example2.xlsx') 
worksheet = workbook.add_worksheet()

writer(content,a)


