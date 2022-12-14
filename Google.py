import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from datetime import date
import xml.etree.ElementTree as ET

class USDEUROGoogle(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome('chromedriver.exe')

    def test_Seach_google(self):
        # 1.Открытие страницы http://google.ru/
        self.drv.get('http://google.ru/')
        assert 'Google' in self.drv.title
        # 2.Поиск курса USD ЦБ на гугл.ру
        USDEUROCB = self.drv.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        USDEUROCB.send_keys('Курс USD ЦБ')
        USDEUROCB.send_keys(Keys.RETURN)
        GoogleUSD = self.drv.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/div/table/tbody/tr[2]/td[3]/b').text
        GoogleEURO = self.drv.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/div/table/tbody/tr[3]/td[3]').text
        self.drv.back()
        # 3.SOAP запрос на сайт ЦБ курсы валют, вытаскиваем курс Доллара и Евро
        dt = str(date.today()).split('-')
        CBRURL = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + dt[2] + '/' + dt[1] + '/' + dt[0]
        response = requests.request("POST", CBRURL)
        resp_xml_content = str(response.content)  # ответ из byte в str
        resp_xml_content = resp_xml_content[2:-1]  # из str отрезаем первые два и один послендий элемент
        resp_xml_content = ET.fromstring(resp_xml_content)  # конвертирую str в xml
        xmlUSD = resp_xml_content[10][4].text  # тэг - 11, атрибут - 5 (отсчет от нуля идет)
        xmlEURO = resp_xml_content[11][4].text

        assert GoogleUSD == xmlUSD
        assert GoogleEURO == xmlEURO

    def tearDown(self):
        self.drv.close()

if __name__ == '__main__':
    unittest.main()