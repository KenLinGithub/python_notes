import datetime
today = datetime.date.today()

print('{} 年 {} 月 {} 日'.format(today.year, str(today.month).zfill(2), str(today.day).zfill(2)))

date_after_7_days = today + datetime.timedelta(days=7)

print('{} 年 {} 月 {} 日'.format(date_after_7_days.year, str(date_after_7_days.month).zfill(2), str(date_after_7_days.day).zfill(2)))