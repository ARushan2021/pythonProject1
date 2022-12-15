import pypyodbc

def Zodiak():
    # даты рождения для знаков зодиака, первый знак указан "Овн" указан специально, что-бы отсчет велся не с нуля, а с цифры один
    ZnakZodiak = ('(55.55 - 55.55) - Овн',
                  '(21.03 - 20.04) - Овен: 1',
                  '(21.04 - 21.05) - Телец: 2',
                  '(22.05 - 21.06) - Близнецы: 3',
                  '(22.06 - 22.07) - Рак: 4',
                  '(23.07 - 23.08) - Лев: 5 ',
                  '(24.08 - 23.09) - Дева: 6 ',
                  '(24.09 - 23.10) - Весы: 7',
                  '(24.10 - 22.11) - Скорпион: 8',
                  '(23.11 - 22.12) - Стрелец: 9',
                  '(23.12 - 20.01) - Козерог: 10',
                  '(21.01 - 19.02) - Водолей: 11',
                  '(20.02 - 20.03) - Рыбы: 12')

    # Выводим все знаки зодиака, что-бы выбрать нужный
    print('Введите цифру соответствующую знаку зодиака :')
    for i in range(1, 13):
        print(ZnakZodiak[i])
        i += 1

    # вводим нужный знак зодиака, проверка того что ввели число
    znak = int(input('Ввести цифру: '))

    # Проверяем что введенное число от 1 до 12
    while True:
        if znak >=1 and znak <=12:
            break
        else:
            znak = int(input('Вы ввели не верную цифру, попробуйте еще раз : '))

    # Из ZnakZodiak вытаскиваем день месяц рождения для селекта в sql
    DAYBirthDate1 = (int(ZnakZodiak[znak][1:3])) - 1
    DAYBirthDate1 = str(DAYBirthDate1)
    MONTHBirthDate1 = ZnakZodiak[znak][4:6]

    DAYBirthDate2 = (int(ZnakZodiak[znak][9:11])) + 1
    DAYBirthDate2 = str(DAYBirthDate2)
    MONTHBirthDate2 = ZnakZodiak[znak][12:14]

    # Составляем запрос для селекта в sql
    DataZodik = 'Select LastName, FirstName, BirthDate, Address, City, Country FROM dbo.Employees WHERE (MONTH([BirthDate])=' \
                + MONTHBirthDate1 + ' AND DAY([BirthDate])>' + DAYBirthDate1 + ') OR (MONTH([BirthDate])=' \
                + MONTHBirthDate2 + ' AND DAY([BirthDate])<' + DAYBirthDate2 + ')'
    return DataZodik

def BDZodiak(DT):

    # Данные о БД
    mySQLServer = 'LAPTOP-2KTD1J9D\SQLEXPRESS'
    myDatabase = 'Northwind'

    connection = pypyodbc.connect('Driver={SQL Server};' # переменная для запуска БД
                                  'Server=' + mySQLServer + ';'
                                  'Database=' + myDatabase + ';')

    cursor = connection.cursor() # переменная для запуска селекта в БД
    cursor.execute(DT) # запуска запроса mySQLQuery
    results = cursor.fetchall() # вытащить весь результат ответа на запрос
    connection.close() # закрыть БД

    if results == []:
        print('С таким знаком зодиака нет людей') # Если в ответ на селект ничего не пришло
    else:
        print('Найдены люди рожденные под знаком зодиака :') # перебираем всех найденных людей
        for i in range(0, len(results)):
            print(results[i])
            i += 1

if __name__ == '__main__':
    BDZodiak(Zodiak())