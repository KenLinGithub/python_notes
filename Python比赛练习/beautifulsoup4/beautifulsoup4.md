```
from bs4 import BeautifulSoup

# 解析 HTML 文件
soup = BeautifulSoup(content)

# 寻找第一个标签
json.find("div")

# 寻找所有标签
json.find_all("div")

# 通过 class 寻找所有标签
json.find_all(class_='title')

# 通过 id 寻找所有标签
json.find_all(id='title')

# 获得标签文字
tag.text

# 获得标签属性
tag['attribute']
```