a = 12.384539

b = ['a', 'ab']


def T(a, b, h):
    I = (a + b) * h / 2
    print(I)


T(1, 2, 3)

import xlrd
xlsx=xlrd.open_workbook('/Users/createyoung/Downloads/CourseCode/S1/1-1/PracticeNeed/7月下旬入库表.xlsx')
table = xlsx.sheet_by_index(0)
# table = xlsx.sheet_by_name('7月下旬入库表')
print(table.cell_value(5,4))
print(table.cell(5,4).value)
print(table.row(5)[4].value)

import xlwt

new_workbook = xlwt.Workbook()
worksheet = new_workbook.add_sheet('new_test')
worksheet.write(0, 0, 'hello')
new_workbook.save('/Users/createyoung/desktop/test.xls')