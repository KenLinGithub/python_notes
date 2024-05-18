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
df = df[['address_cn']]
df['region'] = df['address_cn'].str[:2]
df = df.groupby('region').agg({'address_cn': 'count'})
df = df.reset_index()

for _, row in df.iterrows():
    print('{}：{}'.format(row['region'], row['address_cn']))