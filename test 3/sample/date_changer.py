import datetime 
input_date = '2009/10/14'
# 'yyyy-mm-dd'
# 'dd-mm-yyyy'
input_date  = datetime.datetime.strptime(input_date,'%Y/%m/%d')
print(datetime.datetime.strftime(input_date,'%d-%m-%Y'))

# from datetime import datetime
# new_date = datetime.strptime("2023-05-15", "%Y-%m-%d").strftime("%d:%m:%Y")
# print(new_date)