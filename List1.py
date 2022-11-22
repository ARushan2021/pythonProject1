import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Seach_selenide(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome('chromedriver.exe')

    def test_Seach_selenide(self):
        # 1.Открытие страницы http://google.com/ncr
        self.drv.get('https://www.google.com/ncr')
        assert 'Google' in self.drv.title

        # 2.Поиск слова “selenide”
        selenide = self.drv.find_element(By.NAME, "q")
        selenide.send_keys('Selenide')
        selenide.send_keys(Keys.RETURN)
        assert 'Selenide' in self.drv.title

        # 3.Провека, что первый результат – ссылка на сайт selenide.org.
        selenide_link = 'https://selenide.org/'
        first_link = self.drv.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3')
        first_link.click()
        first_link = self.drv.current_url
        assert selenide_link == first_link

