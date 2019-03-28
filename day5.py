from xlutils.copy import copy
import xlrd
import xlwt

tem_excel = xlrd.open_workbook('/Users/createyoung/Downloads/CourseCode/S1/1-2/PracticeNeed/日统计.xls',
                               formatting_info=True)
tem_sheet = tem_excel.sheet_by_index(0)

new_excel = copy(tem_excel)
new_sheet = new_excel.get_sheet(0)

style = xlwt.XFStyle()

font = xlwt.Font()
font.name = '宋体'
font.bold = True
font.height = 12*20
style.font = font

borders = xlwt.Borders()
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
style.borders = borders

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_LEFT
alignment.vert = xlwt.Alignment.VERT_TOP
style.alignment = alignment

new_sheet.write(2, 1, 8, style)
new_sheet.write(3, 1, 9, style)
new_sheet.write(4, 1, 10, style)
new_sheet.write(5, 1, 11, style)

new_excel.save('/Users/createyoung/desktop/new日统计.xls')
