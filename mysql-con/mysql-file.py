import mysql.connector
'''
    we are creating a connection and creating a database and listing all the databases 
'''
# connection = mysql.connector.connect(host='localhost',user='root',password='welcome')
# print(connection)
# my_cursor = connection.cursor()
# # my_cursor.execute('CREATE DATABASE examplepy')
# my_cursor.execute('show databases')
# for x in my_cursor:
#     print('database is ',x)

mydb= mysql.connector.connect(host='localhost',user='root',password='welcome',database='examplepy')
print(mydb)
db_cursor = mydb.cursor()
# db_cursor.execute('CREATE TABLE Users(name VARCHAR(20),age INT(3))')
# db_cursor.execute('SHOW TABLES')
# for table in db_cursor:
#     print('table is ',table)
# db_cursor.execute('INSERT INTO Users(name,age) VALUES("ashik",20)')
# db_cursor.execute('INSERT INTO Users(name,age) VALUES("Ravi",10)')
# db_cursor.execute('INSERT INTO Users(name,age) VALUES("Ram",80)')
# db_cursor.execute('INSERT INTO Users(name,age) VALUES("Riya",7)')
# db_cursor.execute('INSERT INTO Users(name,age) VALUES("Yogi",15)')
db_cursor.execute('SELECT * FROM Users')
for column in db_cursor:
    print('column is ',column)


