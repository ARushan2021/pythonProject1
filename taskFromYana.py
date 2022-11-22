import math

def areaCircle():
    r = float(input("Введите радиус круга: "))
    s = math.pi * (r**2)
    return print('Площадь круга равна: ' + str(s))

areaCircle()

