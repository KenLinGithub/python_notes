```
from openpyxl import Workbook, load_workbook

# 新建 Excel 文件
wb = Workbook()

# 加载 Excel 文件
wb = load_workbook('text.xslx')

# 在索引为0的位置创建一个工作表
ws = wb.create_sheet('sheet1',0) 

# 选择工作表
ws = wb['sheet1']
ws = wb.get_sheet_by_name('sheet1')

# 删除工作表
wb.remove(ws)

# 工作表表名
wb.title

# 选择单元格
cell = ws['A1']
cell = ws.cell(row=1, column=1)

# 读取/写入单元格数值
cell.value

# 选取单元格数值
cell_range = ws2['A1':'C3']
colA = ws2['A']
col_range = ws2['A:C']
row1 = ws2[1]
row_range = ws2[1:5]

# 保存 Excel 文件
wb.save('test.xlsx')
```