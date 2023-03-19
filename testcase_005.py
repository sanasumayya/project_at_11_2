from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from test_locators_2 import locators2
from test_data_2 import data2
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException



class Test_Sana:
   
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()
   
   
    # Test Login
    def test_Login(self, booting_function):
       self.driver.get(data2.Sana2_Data().url)
       wait = WebDriverWait(self.driver, 5)
       sleep(5)
       self.driver.find_element(by=By.NAME, value=locators2.Sana2_Locators().username_inputBox).send_keys(data2.Sana2_Data().username)
       self.driver.find_element(by=By.NAME, value=locators2.Sana2_Locators.password_InputBox).send_keys(data2.Sana2_Data.password)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.LoginButton).click()
       assert self.driver.title == 'OrangeHRM'
       self.driver.maximize_window()
       print("SUCCESS : Logged in with Username {a} and Password {b}". format(a=data2.Sana2_Data.username, b=data2.Sana2_Data.password))
       sleep(5)
       source=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a')
       action = ActionChains(self.driver)
       action.click(source).perform()
       sleep(2)
        
       source=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a')
       action = ActionChains(self.driver)                    
       action.click(source).perform()
       sleep(2)
       
       self.driver.find_element(by=By.NAME, value=locators2.Sana2_Locators.name1).send_keys(data2.Sana2_Data.name1_inputbox)
       sleep(2)
       self.driver.find_element(by=By.NAME, value=locators2.Sana2_Locators.name2).send_keys(data2.Sana2_Data.name2_inputbox)
       sleep(5)
       self.driver.find_element(by=By.NAME, value=locators2.Sana2_Locators.name3).send_keys(data2.Sana2_Data.name3_inputbox)
       sleep(5)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.nickname).send_keys(data2.Sana2_Data.nickname_inputbox)
       sleep(5)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.other_id).send_keys(data2.Sana2_Data.other_id_inputbox)
       sleep(5)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().licence_num).send_keys(data2.Sana2_Data.licence_num_inputbox)
       sleep(2)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().expiry_date).send_keys(data2.Sana2_Data.expirydate)
       sleep(2)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().nationality).click()
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().dd2).click()
       sleep(2)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().marital_status).click()
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().dd2).click()
       sleep(2)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().dob).send_keys(data2.Sana2_Data.dob_inputbox)
       sleep(2)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().gender).click()
       sleep(2)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().military).send_keys(data2.Sana2_Data.military_inputbox)
       sleep(2)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().save_button2).click()
       sleep(10)
    
       



      
       


