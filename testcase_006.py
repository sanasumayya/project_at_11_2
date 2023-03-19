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
       sleep(5)
       wait = WebDriverWait(self.driver, 5)
      
       self.driver.find_element(by=By.NAME, value=locators2.Sana2_Locators().username_inputBox).send_keys(data2.Sana2_Data().username)
       self.driver.find_element(by=By.NAME, value=locators2.Sana2_Locators.password_InputBox).send_keys(data2.Sana2_Data.password)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.LoginButton).click()
       assert self.driver.title == 'OrangeHRM'
       self.driver.maximize_window()
       print("SUCCESS : Logged in with Username {a} and Password {b}". format(a=data2.Sana2_Data.username, b=data2.Sana2_Data.password))
       sleep(5)

       source=self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.my_info)
       action = ActionChains(self.driver)
       sleep(10) 
       action.click(source).perform()
       sleep(20)
        
       source=self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.contact_details)
       action = ActionChains(self.driver)                    
       sleep(10)
       action.click(source).perform()
       sleep(20)

       input_box = self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.street_1)
       input_box.clear()
       input_box.send_keys(data2.Sana2_Data.street_1_inputbox)

       input_box = self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.street_2)
       input_box.clear()
       input_box.send_keys(data2.Sana2_Data.street_2_inputbox)

       input_box = self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.city)
       input_box.clear()
       input_box.send_keys(data2.Sana2_Data.city_inputbox)

       input_box = self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.state)
       input_box.clear()
       input_box.send_keys(data2.Sana2_Data.state_inputbox)

       input_box = self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.zip)
       input_box.clear()
       input_box.send_keys(data2.Sana2_Data.zip_inputbox)

       #country dropdown
   
       wait.until(EC.element_to_be_clickable((By.XPATH, locators2.Sana2_Locators().country1)))
       userrole1=self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().country1)
       userrole1.click()
       wait.until(EC.element_to_be_clickable((By.XPATH, locators2.Sana2_Locators().dd2)))
       drop_downvalue19=self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().dd2).text
       if drop_downvalue19.__contains__("India"):
              self.driver.execute_script("var a=arguments[0];a.innerHTML='India'",userrole1)
       sleep(5)
       
       input_box = self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.tel)
       input_box.clear()
       input_box.send_keys(data2.Sana2_Data.tel_inputbox)

       input_box = self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.mobile)
       input_box.clear()
       input_box.send_keys(data2.Sana2_Data.mobile_inputbox)

       input_box = self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.work)
       input_box.clear()
       input_box.send_keys(data2.Sana2_Data.work_inputbox)

       input_box = self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.work_email)
       input_box.clear()
       input_box.send_keys(data2.Sana2_Data.workemail_inputbox)

       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.save_button).click()
