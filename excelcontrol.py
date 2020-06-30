import openpyxl as xl

colStart = 2
rowStart = "A"
excel = xl.load_workbook('./test.xlsx')
wb = excel['Sheet1']
f = open('audfuf.txt', 'r')

def personal(look):
    global rowStart,colStart,wb
    look = look.split(',')
    for i in range(0, 14):
        look[i] = look[i][look[i].find(":") + 1:].replace("}", "")
        wb[rowStart + str(colStart)]= look[i]
        rowStart = chr(ord(rowStart) + 1)
        if (rowStart == "O"):
            rowStart = "A"
            print(colStart)
            colStart += 1
            

file = f.read()
file = file.split("},")
for i in range(0, len(file)):
    file[i] = file[i] + "}"
    personal(file[i])
excel.save('./new_test.xlsx')
f.close()
excel.close()