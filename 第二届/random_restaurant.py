import pandas as pd
import requests
import random

headers = {
    'Authorization': 'APPCODE 09d43a591fba407fb862412970667de4'
}

res = requests.get('https://dst.apigateway.data.gov.mo/dst_restaurant', headers=headers)
res.encoding = 'utf8'

with open('restaurant.xml', 'w', encoding='utf8') as f:
    f.write(res.text)


df = pd.read_xml('restaurant.xml')
df = df[['name_cn', 'address_cn']]
df = df.reset_index()

rest_list = []
for _, row in df.iterrows():
    rest_list.append([row['name_cn'], row['address_cn']])


rest = random.choice(rest_list)
print('今晚一於食{}，位於{}。'.format(rest[0], rest[1]))