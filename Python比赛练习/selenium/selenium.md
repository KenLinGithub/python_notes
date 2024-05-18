```
from selenium import webdriver

# 打开浏览器
browser = webdriver.Chrome(driver_path)

# 退出浏览器
browser.quit()

# 访问网站
browser.get(url)

# 刷新页面
driver.refresh()

# 后退页面
driver.back()

# 前进页面
driver.forward()

# 根据 id 查找标签
find_elements_by_id()

# 根据 name 查找标签
find_elements_by_name()

# 根据 class 查找标签
find_elements_by_class_name()

# 根据标签名字查找标签
find_elements_by_tag_name()

# 根据 xpath 查找标签
find_elements_by_xpath()

# 根据 css 查找标签
find_elements_by_css_selector()

# 输入文字
element.send_keys('content')

# 删除键 Backspace
send_keys(Keys.BACK_SPACE)

# 空格键 Space
send_keys(Keys.SPACE)

# 制表键 Tab
send_keys(Keys.TAB)

# 回退键 Esc
send_keys(Keys.ESCAPE) 

# 回车键 Enter
send_keys(Keys.ENTER)

# 全选 Ctrl+A
send_keys(Keys.CONTROL,'a')

# 复制 Ctrl+C
send_keys(Keys.CONTROL,'c')

# 剪切 Ctrl+X
send_keys(Keys.CONTROL,'x')

# 粘贴 Ctrl+V
send_keys(Keys.CONTROL,'v')

# 全选 键盘 F1 - F12
send_keys(Keys.F1)

# 清除文字
element.clear()

# 点击元素
element.click()

# 模拟回车提交
element.submit()

# 获得元素文字
element.text
```