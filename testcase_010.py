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
       self.driver.find_element(by=By.NAME, value=locators2.Sana2_Locators().username_inputBox).send_keys(data2.Sana2_Data().username)
       self.driver.find_element(by=By.NAME, value=locators2.Sana2_Locators.password_InputBox).send_keys(data2.Sana2_Data.password)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.LoginButton).click()
       assert self.driver.title == 'OrangeHRM'
       print("SUCCESS : Logged in with Username {a} and Password {b}". format(a=data2.Sana2_Data.username, b=data2.Sana2_Data.password))
       sleep(5)

       source=self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.pimbutton)
       action = ActionChains(self.driver)
       action.click(source).perform()
       sleep(5)

       source=self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.employeelist_button)
       action = ActionChains(self.driver)
       action.click(source).perform()
       sleep(5)

       source=self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.record)
       action = ActionChains(self.driver)
       action.click(source).perform()
       sleep(5)

       source=self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators.job_button)
       action = ActionChains(self.driver) 
       action.click(source).perform()
       sleep(5)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().terminate_employee).click()
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().terminateemployee_date).send_keys('1992-3-17')
       sleep(5)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().termination_reason).click()
       self.driver.find_element(by=By.XPATH, value="//div[@role='listbox']").click()
       sleep(5)
       self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().termination_savebutton).click()
       sleep(10)


