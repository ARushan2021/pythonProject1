import datetime

year = int(input("Введите год: "))
holiday = int(input("Введите колличество праздничных дней в будни : "))
anothervacation = int(input("Введите колличество отпускных дней в будни : "))
businessdays = 0
for m in range(1, 13): # Вычисляем кол.во будних дней в заданной году, перебираем месяцы
    for i in range(1, 32): # перебираем дни недели
        try:
            thisdate = datetime.date(year, m, i)
        except(ValueError):
            break
        if thisdate.weekday() < 5: # выясняем день недели пришелся на выходной или будни
            businessdays += 1

businessdays = businessdays - holiday - anothervacation # вычитаем праздники и отпуск
print('Колличество рабочих дней в ' + str(year) + ' равно ' + str(businessdays))
