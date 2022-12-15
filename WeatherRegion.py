import requests
from datetime import date
import json

def WeatherRegion():
    # текущую дату подставляю в url
    dt = str(date.today())
    cityCoor = ('55.67,37.52,Moscow',
                '59.94,30.31,St Petersburg',
                '55.67,37.52,Ekaterinburg',
                '55.67,37.52,Krasnoyarsk')
    for i in range(0, len(cityCoor)):
        latitude1 = cityCoor[i][0:5]
        longitude1 = cityCoor[i][6:11]
        city = cityCoor[i][12::]

        MeteoURL = 'https://api.open-meteo.com/v1/forecast?latitude=' + latitude1 + '&longitude=' + longitude1 + \
                   '&hourly=apparent_temperature&timezone=Europe%2FMoscow&start_date=' + dt + '&end_date=' + dt
        # Get request
        response = requests.request("GET", MeteoURL)
        resp = json.loads(response.content)
        tm = resp['hourly']['apparent_temperature']
        averageTm = (float(tm[11]) + float(tm[12]) + float(tm[13]) + float(tm[14])
                     + float(tm[15]) + float(tm[16]) + float(tm[17])) / 7
        averageTm = round(averageTm)

        print(city + ': ' + str(averageTm))

WeatherRegion()

"""   
    resp_xml_content = str(response.content,
                           'windows-1251')  # ответ из byte в str и кодировка 'windows-1251', что бы название валюты отображалось корректно.
    resp_xml_content = ET.fromstring(resp_xml_content)  # конвертирую str в xml
    xmlUSD = resp_xml_content[10][4].text  # тэг - 11, атрибут - 5 (отсчет от нуля идет)
    xmlEURO = resp_xml_content[11][4].text
    xmlUSD = float(xmlUSD.replace(',', '.'))  # меняем "," на "." и конвертируем в float
    xmlEURO = float(xmlEURO.replace(',', '.'))
    xmlUSDName = resp_xml_content[10][3].text  # из xml вытаскиваем название валюты, для вывода print
    xmlEUROName = resp_xml_content[11][3].text

    print(xmlUSDName, '- ', xmlUSD)
    print(xmlEUROName, '- ', xmlEURO)

"""