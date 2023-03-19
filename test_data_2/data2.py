class Sana2_Data:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'


    username = 'Admin'


    password = 'admin123'
      
    password2 = 'Invalid password'  

    First_Name = 'firstName'

    search_box = 'Admin'

    # testcase_002 dropdown (admin-enabled, ess-disables)
    usermanagement_name_inputbox = 'raechal'
    user_employee_name_inputbox = 'Aaliyah Haq'

# testcase3
    firstname_inputbox = 'harry'
    secondname_inputbox = 'potter'
    lastname_inputbox = 'snape'
    enabled_name_inputbox= 'abcde'
    enabled_password = '12345678'
    enabled_confirm_password = '12345678'
    

    # testcase_005 personal details
    name1_inputbox = 'harry'
    name2_inputbox = 'potter'
    name3_inputbox = 'snape'
    nickname_inputbox = 'joe'
    other_id_inputbox = '9980'
    licence_num_inputbox = '1234erf'
    expirydate = '2023-12-24'
    ssn_num_inputbox = 'er567'
    sin_num_inputbox = 'ghj456'
    dob_inputbox = '1996-12-26'
    military_inputbox = '12'




    # testcase_006 contact details
    street_1_inputbox = '4th cross'
    street_2_inputbox = '2nd lane'
    city_inputbox = 'bangalore'
    state_inputbox = 'karnataka'
    zip_inputbox = '00934'
    tel_inputbox = '879946556'
    mobile_inputbox = '4459873'
    work_inputbox = '98753452'
    workemail_inputbox = 'abc@gmail.com'

    # testcase_007 emergency contact
    emergency_name_inputbox = 'mary'
    relationship_inputbox = 'sister'
    emergency_mobnum_inputbox = '98765432'

    #testcase_008 dependency details
    dependent_name_inputbox = 'joe'
    calender_inputbox = '1970-12-22'

    #testcase_009 job details
    joineddate_inputbox = '1991-10-12'
    contract_startdate_inputbox = '1996-12-26'
    contract_enddate_inputbox = '2000-2-15'


 # testcase_12 salary details

    salarycomponents_inputbox = 'basic pay'
    amount_inputbox = '45000'
    accountnumber_inputbox = '3456hg788'
    routingnumber_inputbox = '12345678'
    amount2_inputbox = '45000'



#working with dropdown of tc_2 and tc_6


    # (//div[@class='oxd-select-text oxd-select-text--active'])[2].click
    #    //div[@role='listbox'].text
    #    print
    #    if
    #    (//div[@class='oxd-select-text oxd-select-text--active'])[2].click
    #    dropdown = self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().dd)
    #    dropdown_value = self.driver.find_element(by=By.XPATH, value=dropdown).text
    #    value = self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().country1)
    #    print(dropdown_value)
    #    if dropdown_value.__contains__("India"):
    #        self.driver.execute_script("var a =arguments[0];a.innerHTML='India'",value)

           
    #    wait.until(EC.element_to_be_clickable((By.XPATH, locators2.Sana2_Locators().dd)))
    #    dropdown = self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().dd1).click()
    #    dropdown_value = self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().dd2).text
    #    value = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]')
    #    if dropdown_value.__contains__("Admin"):
    #        self.driver.find_element(by=By.XPATH, value=locators2.Sana2_Locators().dd1).click()
           

   
       
    
   
   

