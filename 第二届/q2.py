import datetime
import os

if not os.path.exists('Daily'):
    os.makedirs('Daily')

content = input('Content: ')
date = datetime.date.today()
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().min

if content != '':
    with open('Daily\{}.txt'.format(date), 'a', encoding='utf8') as f:
        f.write('{}:{} {}\n'.format(hour, minute, content))