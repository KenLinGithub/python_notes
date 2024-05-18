import requests
import untangle
from bs4 import BeautifulSoup
import datetime


res = requests.get('https://xml.smg.gov.mo/')
res.encoding = 'utf8'

soup = BeautifulSoup(res.text)
table = soup.find_all('table')[5]
rows = table.find_all('tr')[1:]

weather_status_dict = {}
for row in rows:
    cells = row.find_all('td')
    weather_status = cells[0].text.strip()
    weather_name = cells[1].text.strip()

    weather_status_dict[weather_status] = weather_name


res = requests.get('https://xml.smg.gov.mo/c_7daysforecast.xml')
res.encoding = 'utf8'

obj = untangle.parse(res.text)
weather_list = obj.SevenDaysForecast.Custom.WeatherForecast

with open('forecast-{}.txt'.format(datetime.date.today()), 'w', encoding='utf8') as f:
    for weather in weather_list:
        date = weather.ValidFor.cdata
        weather_status = weather.WeatherStatus.cdata
        weather_name = weather_status_dict[weather_status]
        max_temp = weather.Temperature[0].Value.cdata
        min_temp = weather.Temperature[0].Value.cdata

        f.write('{} ({}) {} 至 {} 度\n'.format(date, weather_name, max_temp, min_temp))