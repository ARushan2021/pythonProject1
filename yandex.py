import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests

class Seach_selenide(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome('chromedriver.exe')
        time.sleep(1)

    def test_Seach_yandex(self):

        # 1.Открытие страницы http://ya.ru/
        self.drv.get('https://yandex.ru/search/?lr=213&text=USD+MOEX&wiz=finance')
        assert 'Яндекс' in self.drv.title
        time.sleep(1)
        # 2.Поиск на яндексе курса USD ЦБ
        USDCB1 = self.drv.find_element(By.XPATH, '//*[@id="a11y-search-result-converter"]/div[2]/div[2]/span[2]/button')
        time.sleep(1)
        USDCB1.click()
        time.sleep(1)
        USDCB1.send_keys(Keys.ARROW_UP)
        time.sleep(1)
        USDCB1.send_keys(Keys.ENTER)
        time.sleep(1)
        YaUSD = self.drv.find_element(By.XPATH, '//*[@id="a11y-search-result-converter"]/div[1]/div[2]/span[1]/input').get_attribute("value")
        time.sleep(1)
        YaUSD = float(YaUSD.replace(',', '.'))
        # 2.Поиск на яндексе курса Euro ЦБ
        EUROCB = self.drv.find_element(By.XPATH, '//*[@id="a11y-search-result-converter"]/div[1]/div[1]/span[3]/button')
        time.sleep(1)
        EUROCB.click()
        time.sleep(1)
        EUROCB.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        EUROCB.send_keys(Keys.ENTER)
        time.sleep(1)
        YaEURO = self.drv.find_element(By.XPATH, '//*[@id="a11y-search-result-converter"]/div[1]/div[2]/span[1]/input').get_attribute("value")
        YaEURO = float(YaEURO.replace(',', '.'))
        # 3.дата из яндекса
        DtYa = self.drv.find_element(By.XPATH, '// *[ @ id = "a11y-search-result-converter"] / div[2] / div[2] / a').text
        dt = str(DtYa[0:10]).split('.')
        # 4.SOAP запрос на сайт ЦБ курсы валют, вытаскиваем курс Доллара и Евро, дату в запрос вставялем из яндекса
        CBRURL = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + dt[0] + '/' + dt[1] + '/' + dt[2]
        response = requests.request("POST", CBRURL)
        exchangeUSDCBR = round(float(response.text[1722:1729].replace(',', '.')), 2)
        exchangeEuroCBR = round(float(response.text[1856:1863].replace(',', '.')), 2)

        assert YaUSD == exchangeUSDCBR
        assert YaEURO == exchangeEuroCBR

    def tearDown(self):
        self.drv.close()

if __name__ == '__main__':
    unittest.main()