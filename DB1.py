import pypyodbc

mySQLServer = 'LAPTOP-2KTD1J9D\SQLEXPRESS'
myDatabase = 'Northwind'

connection = pypyodbc.connect('Driver={SQL Server};' # переменная для запуска БД
                              'Server=' + mySQLServer + ';'
                              'Database=' + myDatabase + ';')

cursor = connection.cursor() # переменная для запуска селекта в БД
mySQLQuery = ("""
Select * FROM dbo.Customers
WHERE Country = 'Spain'
""")

cursor.execute(mySQLQuery) # запуска запроса mySQLQuery
results = cursor.fetchall() # вытащить весь результат ответа на запрос
connection.close() # закрыть БД

ContactName3 = results[3][2]
print(ContactName3)
print(type(mySQLQuery))


