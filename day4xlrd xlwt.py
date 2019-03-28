import xlrd, xlwt

xlsx = xlrd.open_workbook('/Users/createyoung/Downloads/CourseCode/S1/1-1/PracticeNeed/7月下旬入库表.xlsx')
table = xlsx.sheet_by_index(0)
newworkbook = xlwt.Workbook()
worksheet = newworkbook.add_sheet('new7月下旬入库表')
for x in range(0, table.nrows):
    for y in range(0, table.ncols):
        if table.cell(x, y).ctype == 3:
            # style = xlwt.XFStyle()
            # style.num_format_str = 'YYYY/MM/DD'
            # values = table.cell(x, y).value
            # worksheet.write(x, y, values, style)
            datecell = xlrd.xldate.xldate_as_datetime(table.cell(x, y).value, 0)
            values = datecell.strftime('%Y/%m/%d')
            print(values)
            worksheet.write(x, y, values)
        else:
            values = table.cell(x, y).value
            worksheet.write(x, y, values)
        print(values)
newworkbook.save('/Users/createyoung/desktop/new7库存.xls')
