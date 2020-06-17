import pandas as pd
import matplotlib.dates as dates
import matplotlib.pyplot as plt
from connect_mssql import MSSQL

path = r'C:\\Users\\lilinyang\\Desktop\\'

a = pd.read_csv(path+'日报图表test.csv')
print(a['日期'].str[0:7])


# x = a['日期']
# y = a['订单数']
# fig, ax = plt.subplots()
# ax.xaxis.set_major_locator(x)
# ax.xaxis.set_minor_locator(x.str[0:6])
# plt.plot(x, y)
# plt.show()