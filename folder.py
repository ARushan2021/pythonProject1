import os
import shutil

directoryFiles = 'C:/моя папка/Мои документы/для разбора/разобрать/'
directoryFirst = 'C:/моя папка/Мои документы/для разбора/а-н/'
directorySecond = 'C:/моя папка/Мои документы/для разбора/о-я/'
directoryOther = 'C:/моя папка/Мои документы/для разбора/остальные/'
firstFolder = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н')
secondFolder = ('о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я')

files = os.listdir(directoryFiles)

for x in range(len(files)):
    g = files[x]
    if g[0] in firstFolder:
        shutil.move(directoryFiles + g, directoryFirst)
    elif g[0] in secondFolder:
        shutil.move(directoryFiles + g, directorySecond)
    else:
        shutil.move(directoryFiles + g, directoryOther)
    x += 1






