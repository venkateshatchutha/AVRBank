import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [5, 6]
plt.rcParams["figure.autolayout"] = True

headers = ['Tag', 'Start', 'End', 'Mean', 'Min', 'Max', 'Std', 'Cnt']
df = pd.read_csv('C:/Users/User/Documents/MS-Projects/test/test.csv', parse_dates=True, names=headers)
df['Start'] = df['Start'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))
print(df)
df = df.pivot(index='Start', columns='Tag', values='Mean')
df.plot()
plt.show()
