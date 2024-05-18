```
import pandas as pd

# 读取 CSV 文件
df = pd.read_csv(filepath)

# 遍历列表
for index, row in df.iterrows():
    value= row['column_name']

# 读取特定行
df[0]
df.iloc[0]

# 读取特定列
df['column_name']

# 列表筛选
df[df['column_name']=='title']

# 列表排序 True 为升序 False 为降序
df.sort_values(by='column_name', ascending=True)

# 列表行数
len(df)

# 列总和
df["column_name"].sum()

# 转换为日期格式
pd.to_datetime(df['date'], format='%Y')
```