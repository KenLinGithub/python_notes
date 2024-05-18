```
import untangle

# 解析 XML 文件
doc = untangle.parse(content)

# 获得 tag 内容
text = doc.tag.cdata

# 获得 tag 属性
text = doc.tag['attribute']
text = doc.tag.get_attribute('attribute')
```