from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from test_locators_2 import locators2
from test_data_2 import data2
import pytest


class Test_Sana:
   
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()
   
    # Test the title of your web application
    def test_get_title(self, booting_function):
        self.driver.get(data2.Sana2_Data().url)
        sleep(5)
        assert self.driver.title == self.driver.title
        print("SUCCESS : Web Title Captured Successfully !")
   
    # Test Login
    def test_Login(self, booting_function):
       self.driver.get(data2.Sana2_Data().url)
       sleep(5)
       self.driver.find_element(by=By.NAME, value=locators2.Sana2_Locators().username_inputBox).send_keys(data2.Sana2_Data().username)
       self.driver.find_element(by=By.NAME, value=locators2.Sana2_Locators.password_InputBox).send_keys(data2.Sana2_Data.password)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.LoginButton).click()
       assert self.driver.title == 'OrangeHRM'
       print("SUCCESS : Logged in with Username {a} and Password {b}". format(a=data2.Sana2_Data.username, b=data2.Sana2_Data.password))
       self.driver.implicitly_wait(5)
       menu_items = ['ADMIN','PIM','LEAVE','TIME','RECRUITMENT','MY INFO','PERFORMANCE','DASHBOARD','DIRECTORY','MAINTENANCE','BUZZ']
       for items in menu_items:
           self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().search_box_input).send_keys(items)
           self.driver.refresh()
           self.driver.implicitly_wait(2)
           self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().search_box_input).send_keys(items.lower())
           self.driver.refresh()
           self.driver.implicitly_wait(2)


       