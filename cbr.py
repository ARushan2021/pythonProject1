import requests
from datetime import date
import xml.etree.ElementTree as ET

def USDCBR ():

        # текущую дату подставляю в url ЦБ
        dt = str(date.today()).split('-')
        CBRURL = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + dt[2] + '/' + dt[1] + '/' + dt[0]
        # POST request
        response = requests.request("POST", CBRURL)
        resp_xml_content = str(response.content) # ответ из byte в str
        resp_xml_content = resp_xml_content[2:-1] # из str отрезаем первые два и один послендий элемент
        resp_xml_content = ET.fromstring(resp_xml_content) # конвертирую str в xml
        xmlUSD = resp_xml_content[10][4].text # тэг - 11, атрибут - 5 (отсчет от нуля идет)
        xmlEURO = resp_xml_content[11][4].text
        xmlUSD = float(xmlUSD.replace(',', '.'))
        xmlEURO = float(xmlEURO.replace(',', '.'))
        print(type(xmlEURO))
        print(xmlEURO)
        print(type(xmlUSD))
        print(xmlUSD)

        #for x in resp_xml_content[10]:
        #        print(x.tag, x.text)


USDCBR ()