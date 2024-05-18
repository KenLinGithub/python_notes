import pandas as pd
import requests


headers = {
    'Authorization': 'APPCODE 09d43a591fba407fb862412970667de4'
}

res = requests.get('https://dst.apigateway.data.gov.mo/dst_restaurant', headers=headers)
res.encoding = 'utf8'

with open('restaurant.xml', 'w', encoding='utf8') as f:
    f.write(res.text)


df = pd.read_xml('restaurant.xml')
df = df[['dish_name_zh', 'dish_name_en', 'name_cn', 'name_en']]
df.columns = ['Dish', 'Dish EN', 'Name', 'Name EN']
df.to_excel('restaurant.xlsx', index=False)

df = df.fillna(' ')
df = df.groupby('Dish').agg({'Name': 'count'})
df = df.reset_index()

rest_num = df['Name'].sum()

print('已將 .xml 轉換為 .xlsx 格式，涉及 {} 間餐廳資料，分別屬於下列菜式：'.format(rest_num))
for _, row in df.iterrows():
    print(row['Dish'], row['Name'])