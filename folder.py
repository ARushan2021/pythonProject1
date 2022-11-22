import os
import shutil
import time
def fileDistribution():
    directoryFiles = 'C:/моя папка/Мои документы/для разбора/разобрать/'
    directoryFirst = 'C:/моя папка/Мои документы/для разбора/а-н/'
    directorySecond = 'C:/моя папка/Мои документы/для разбора/о-я/'
    directoryOther = 'C:/моя папка/Мои документы/для разбора/остальные/'
    firstFolder = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н')
    secondFolder = ('о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я')

    files = os.listdir(directoryFiles)
    y = len(files)

    for x in range(y):
        g = files[x]
        if g[0] in firstFolder:
            shutil.move(directoryFiles + g, directoryFirst)
        elif g[0] in secondFolder:
            shutil.move(directoryFiles + g, directorySecond)
        else:
            shutil.move(directoryFiles + g, directoryOther)
        x += 1
    return print(str(y) + ' файл(а/ов) разобран(но)')

def b():
    while True:
        time.sleep(10) # программа запускается каждые 10 сек
        fileDistribution()

b()