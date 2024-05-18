```
import requests

# 获取网页内容
page = requests.get(url)

# 网页编码
page.encoding = 'utf8'

# 获取网页内容
content = page.text
```