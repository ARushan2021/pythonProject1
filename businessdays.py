import datetime

year = int(input("Введите год: "))
holiday = int(input("Введите колличество праздничных дней в будни : "))
anothervacation = int(input("Введите колличество отпускных дней в будни : "))
businessdays = 0
for m in range(1, 13):

    for i in range(1, 32):
        try:
            thisdate = datetime.date(year, m, i)
        except(ValueError):
            break
        if thisdate.weekday() < 5:
            businessdays += 1

businessdays = businessdays - holiday - anothervacation
print('Колличество рабочих дней в ' + str(year) + ' равно ' + str(businessdays))
