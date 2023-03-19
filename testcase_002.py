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
       print("SUCCESS : Logged in with Username {a} and Password {b}". format(a=data2.Sana2_Data.username, b=data2.Sana2_Data.password))
       sleep(5)
      
       wait.until(EC.element_to_be_clickable((By.XPATH, locators2.Sana2_Locators().Admin)))
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().Admin).click()
           
       wait.until(EC.element_to_be_clickable((By.XPATH, locators2.Sana2_Locators().user_management)))
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().user_management).click() 
           
       wait.until(EC.element_to_be_clickable((By.XPATH, locators2.Sana2_Locators().user)))
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().user).click()  
       self.driver.execute_script("window.stop();");  
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().name_usermanagement).send_keys(data2.Sana2_Data().usermanagement_name_inputbox)
       sleep(2)
       wait.until(EC.element_to_be_clickable((By.XPATH, locators2.Sana2_Locators().user_employee_name)))
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().user_employee_name).send_keys(data2.Sana2_Data().user_employee_name_inputbox)    
       sleep(5)  
            
       wait.until(EC.element_to_be_clickable((By.XPATH, locators2.Sana2_Locators().userrole)))
       userrole1=self .driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().userrole)
       userrole1.click()
       wait.until(EC.element_to_be_clickable((By.XPATH, locators2.Sana2_Locators().dropdown)))
       drop_downvalue19=self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().dropdown).text
       if drop_downvalue19.__contains__("general.admin"):
              self.driver.execute_script("var a=arguments[0];a.innerHTML='general.admin'",userrole1)
       sleep(5)
       wait.until(EC.element_to_be_clickable((By.XPATH, locators2.Sana2_Locators().userstatus)))
       userrole1=self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().userstatus)
       userrole1.click()
       wait.until(EC.element_to_be_clickable((By.XPATH, locators2.Sana2_Locators().dropdown)))
       drop_downvalue19=self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().dropdown).text
       if drop_downvalue19.__contains__("general.enabled"):
              self.driver.execute_script("var a=arguments[0];a.innerHTML='general.enabled'",userrole1)
       sleep(5)

       wait.until(EC.element_to_be_clickable((By.XPATH, locators2.Sana2_Locators().userrole)))
       userrole1=self .driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().userrole)
       userrole1.click()
       wait.until(EC.element_to_be_clickable((By.XPATH, locators2.Sana2_Locators().dropdown)))
       drop_downvalue19=self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().dropdown).text
       if drop_downvalue19.__contains__("general.ess"):
              self.driver.execute_script("var a=arguments[0];a.innerHTML='general.ess'",userrole1)
       sleep(5)

       wait.until(EC.element_to_be_clickable((By.XPATH, locators2.Sana2_Locators().userstatus)))
       userrole1=self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().userstatus)
       userrole1.click()
       wait.until(EC.element_to_be_clickable((By.XPATH,locators2.Sana2_Locators().drop_down)))
       drop_downvalue19=self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().dropdown).text
       if drop_downvalue19.__contains__("general.disabled"):
            self.driver.execute_script("var a=arguments[0];a.innerHTML='general.disabled'",userrole1)
       sleep(5)      
      

      