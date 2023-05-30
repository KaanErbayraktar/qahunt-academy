import openpyxl
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

class TestTestotokoc():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testotokoc(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
    Names = []
    Numbers = []
    Addresses = []
    self.driver.get("https://www.otokocikinciel.com/")
    self.driver.set_window_size(1936, 1066)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[8]/div/div/form/div[3]/div/button[1]")))
    self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[8]/div/div/form/div[3]/div/button[1]").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/header/div[1]/div/div/div[1]/a[1]/div")))
    self.driver.find_element(By.XPATH, "/html/body/div[3]/div/header/div[1]/div/div/div[1]/a[1]/div").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div")))
    self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div/form/div[4]/select").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div/form/div[4]/select/option[9]")))
    self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div/form/div[4]/select/option[9]").click()
    self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div/form/div[5]/select").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div/form/div[5]/select/option[10]")))
    self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div/form/div[5]/select/option[11]").click()
    self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div/form/div[6]/div[2]").click()
    #self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div/form/div[13]/select").click()
    self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div/form/div[13]/select/option[1]").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div/form/div[14]/div[1]")))
    self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div/form/div[14]/div[1]").click()
    self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div/form/div[18]/button").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div")))
    first_tab_handle = self.driver.current_window_handle

    
    for i in range(2,12):
        o = str(i)
        new_tab_link = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[2]/div/div/div[{}]".format(o))
        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL).click(new_tab_link).key_up(Keys.CONTROL).perform()
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[i-1])
        sleep(2)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[3]/div/div[3]/div/div[4]/div[4]")))
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[3]/div/div[4]/div[4]").click()
        name = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[3]/div/div[4]/div[2]").text
        address = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[3]/div/div[4]/div[3]/a").text 
        number = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[3]/div/div[4]/div[5]/div[1]/div/span").get_attribute("innerHTML")
        Names.append(name)
        Addresses.append(address)
        Numbers.append(number)
        self.driver.switch_to.window(first_tab_handle)
        sleep(2)
        
    print(Names)
    print(Addresses)
    print(Numbers)

    c = {'Müşteri Temsilcisi': Names, 'Adres': Addresses, 'Telefon Numarası': Numbers}
    df = pd.DataFrame(c)
    print(df)
    writer = pd.ExcelWriter('otokoc.xlsx')
    df.to_excel(writer)
    

   
    
a = TestTestotokoc()
a.test_testotokoc()