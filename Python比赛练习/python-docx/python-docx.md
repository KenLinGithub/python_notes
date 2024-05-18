```
from docx import Document

# 新建 Word 文件
doc = Document()

# 打开 Word 文件
doc = Document('Test.docx')

# 插入标题
doc.add_heading('heading')

# 插入段落
doc.add_paragraph('content')

# 插入图片
doc.add_picture('image.png')

# 插入分页符
doc.add_page_break()

# 保存 Word 文件
doc.save('Test.docx')
```