import requests
from lxml import etree
from datetime import date

def USDCBR ():

        # текущую дату подставляю в url ЦБ
        dt = str(date.today()).split('-')
        CBRURL = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + dt[2] + '/' + dt[1] + '/' + dt[0]

        # POST request
        response = requests.request("POST", CBRURL)
        print(response.text)
        print(response.content)
        resp_xml_content = response.content
        tree = etree.XML(resp_xml_content)

        usd = tree.find()
        print(usd)



        #user_by_email = tree.xpath(f'/response/Valute ID="R01235"/[name = "USD" and value = "{USD}"]')
        #usd = etree.SubElement('ValCurs', 'Valute', 'Value')
        #print(usd)

        # Из ответа запроса вытаскиваем курс Доллара ЦБ и округляем до сотых
        #exchangeUSDCBR = round(float(response.text[1722:1729].replace(',', '.')), 2)
       #exchangeUSDCBR = str(exchangeUSDCBR)

        # Из ответа запроса вытаскиваем курс Евро ЦБ и округляем до сотых
        #exchangeEuroCBR = round(float(response.text[1856:1863].replace(',', '.')), 2)
        #exchangeEuroCBR = str(exchangeEuroCBR)

        #return exchangeEuroCBR, exchangeUSDCBR

#a = USDCBR()
#print(a[0])
#print(a[1])

USDCBR ()