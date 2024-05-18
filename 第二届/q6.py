import pandas
import matplotlib.pyplot as plt


df = pandas.read_excel('desc.xlsx')
df['year'] = df['time'].str[:4]
df = df.groupby('year').agg({'car': 'sum', 'motor': 'sum'})
df = df.reset_index()
df.columns = ['Year', 'Car', 'Motor']
df = df.set_index('Year')
df.to_excel('macao-vehicles-by-year.xlsx')

fig = df.plot.bar()
fig.set_title('Sum Reg. of vehicles in Macao')
fig.legend(loc='upper right')
plt.show()
#fig = fig.get_figure()
#fig.show(block = False)