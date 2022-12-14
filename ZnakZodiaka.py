import pypyodbc



znak = int(input('Введите цифру соответствующую знаку зодиака :'
'\n1 - Овен (21.03 - 20.04)'
'\n2 - Телец (21.04 - 21.05)'
'\n3 - Близнецы (22.05 - 21.06)'
'\n4 - Рак (22.06 - 22.07)'
'\n5 - Лев (23.07 - 23.08)'
'\n6 - Дева (24.08 - 23.09)'
'\n7 - Весы (24.09 - 23.10)'
'\n8 - Скорпион (24.10 - 22.11)'
'\n9 - Стрелец (23.11 - 22.12)'
'\n10 - Козерог (23.12 - 20.01)'
'\n11 - Водолей (21.01 - 19.02)'
'\n12 - Рыбы (20.02 - 20.03)'              
'\nВвести цифру: '))

while True:
    if znak == 1:
        ZnakZodiak = 'Овен (21.03 - 20.04)'
        DataZodik = ("""Select LastName, FirstName, BirthDate, Address, City, Country FROM 
        dbo.Employees WHERE (MONTH([BirthDate])=3 AND DAY([BirthDate])>20) 
        OR (MONTH([BirthDate])=4 AND DAY([BirthDate])<21)""")
        break
    elif znak == 2:
        ZnakZodiak = 'Телец (21.04 - 21.05)'
        DataZodik = ("""Select LastName, FirstName, BirthDate, Address, City, Country FROM 
        dbo.Employees WHERE (MONTH([BirthDate])=4 AND DAY([BirthDate])>20) 
        OR (MONTH([BirthDate])=5 AND DAY([BirthDate])<22)""")
        break
    elif znak == 3:
        ZnakZodiak = 'Близнецы (22.05 - 21.06)'
        DataZodik = ("""Select LastName, FirstName, BirthDate, Address, City, Country FROM 
        dbo.Employees WHERE (MONTH([BirthDate])=5 AND DAY([BirthDate])>21) 
        OR (MONTH([BirthDate])=6 AND DAY([BirthDate])<22)""")
        break
    elif znak == 4:
        ZnakZodiak = 'Рак (22.06 - 22.07)'
        DataZodik = ("""Select LastName, FirstName, BirthDate, Address, City, Country FROM 
        dbo.Employees WHERE (MONTH([BirthDate])=6 AND DAY([BirthDate])>21) 
        OR (MONTH([BirthDate])=7 AND DAY([BirthDate])<23)""")
        break
    elif znak == 5:
        ZnakZodiak = 'Лев (23.07 - 23.08)'
        DataZodik = ("""Select LastName, FirstName, BirthDate, Address, City, Country FROM 
        dbo.Employees WHERE (MONTH([BirthDate])=7 AND DAY([BirthDate])>22) 
        OR (MONTH([BirthDate])=8 AND DAY([BirthDate])<24)""")
        break
    elif znak == 6:
        ZnakZodiak = 'Дева (24.08 - 23.09)'
        DataZodik = ("""Select LastName, FirstName, BirthDate, Address, City, Country FROM 
        dbo.Employees WHERE (MONTH([BirthDate])=8 AND DAY([BirthDate])>23) 
        OR (MONTH([BirthDate])=9 AND DAY([BirthDate])<24)""")
        break
    elif znak == 7:
        ZnakZodiak = 'Весы (24.09 - 23.10)'
        DataZodik = ("""Select LastName, FirstName, BirthDate, Address, City, Country FROM 
        dbo.Employees WHERE (MONTH([BirthDate])=9 AND DAY([BirthDate])>23) 
        OR (MONTH([BirthDate])=10 AND DAY([BirthDate])<24)""")
        break
    elif znak == 8:
        ZnakZodiak = 'Скорпион (24.10 - 22.11)'
        DataZodik = ("""Select * FROM dbo.Employees WHERE (MONTH([BirthDate])=10 AND DAY([BirthDate])>23) 
        OR (MONTH([BirthDate])=11 AND DAY([BirthDate])<23)""")
        break
    elif znak == 9:
        ZnakZodiak = 'Стрелец (23.11 - 22.12)'
        DataZodik = ("""Select LastName, FirstName, BirthDate, Address, City, Country FROM 
        dbo.Employees WHERE (MONTH([BirthDate])=11 AND DAY([BirthDate])>22) 
        OR (MONTH([BirthDate])=12 AND DAY([BirthDate])<23)""")
        break
    elif znak == 10:
        ZnakZodiak = 'Козерог (23.12 - 20.01)'
        DataZodik = ("""Select LastName, FirstName, BirthDate, Address, City, Country FROM 
        dbo.Employees WHERE (MONTH([BirthDate])=12 AND DAY([BirthDate])>22) 
        OR (MONTH([BirthDate])=01 AND DAY([BirthDate])<21)""")
        break
    elif znak == 11:
        ZnakZodiak = 'Водолей (21.01 - 19.02)'
        DataZodik = ("""Select LastName, FirstName, BirthDate, Address, City, Country FROM 
        dbo.Employees WHERE (MONTH([BirthDate])=1 AND DAY([BirthDate])>20) 
        OR (MONTH([BirthDate])=2 AND DAY([BirthDate])<20)""")
        break
    elif znak == 12:
        ZnakZodiak = 'Рыбы (20.02 - 20.03)'
        DataZodik = ("""Select LastName, FirstName, BirthDate, Address, City, Country FROM 
        dbo.Employees WHERE (MONTH([BirthDate])=2 AND DAY([BirthDate])>19) 
        OR (MONTH([BirthDate])=3 AND DAY([BirthDate])<21)""")
        break
    else:
        znak = int(input('Вы ввели не верную цифру, попробуйте еще раз : '))


mySQLServer = 'LAPTOP-2KTD1J9D\SQLEXPRESS'
myDatabase = 'Northwind'

connection = pypyodbc.connect('Driver={SQL Server};' # переменная для запуска БД
                              'Server=' + mySQLServer + ';'
                              'Database=' + myDatabase + ';')

cursor = connection.cursor() # переменная для запуска селекта в БД
cursor.execute(DataZodik) # запуска запроса mySQLQuery
results = cursor.fetchall() # вытащить весь результат ответа на запрос
connection.close() # закрыть БД


if results == []:
    print('С таким знаком зодиака нет людей')
else:
    print('Найдены люди рожденные под знаком зодиака ' + ZnakZodiak + ": ")
    for i in range(0, len(results)):
        print(results[i])
        i += 1