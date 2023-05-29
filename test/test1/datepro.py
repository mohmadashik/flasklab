d1 = '2023-01-23'
# d = d1.split('-')[2]
# m = d1.split('-')[1]
# print(f"{d}-{m}-{y}")

from datetime import datetime 
# d1 = datetime(d1)
# print(d1)
# print(d1.date)

datetime.strptime(d1,'%d-%m-%y')