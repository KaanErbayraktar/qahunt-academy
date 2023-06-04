from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from login import email, password
from time import sleep
from threading import Timer


def lixya_automation():

    raw_data = []
    products = []
    with open('./products.txt',encoding='utf8') as f:
        for line in f:
            raw_data.append(line.strip())
    for i in range(len(raw_data)):
        a = (raw_data[i])
        b = a.replace("{} - ".format(i+1),"")
        products.append(b)

    driver = webdriver.Chrome()
    driver.get("https://www.lixya.com/")
    driver.set_window_size(1936, 1066)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/a")))
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/a").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[2]/div[1]/div/div/div/form/div[1]/input")))
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[2]/div[1]/div/div/div/form/div[1]/input").send_keys(email)
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[2]/div[1]/div/div/div/form/div[2]/input").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[2]/div[1]/div/div/div/form/div[3]/button").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div/div/div[6]/div[2]/select")))
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/a/img").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/div/form/div/button")))
    first_tab_handle = driver.current_window_handle
    new_tab_link = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/a/img")
    for i in range(4):
        action = ActionChains(driver)
        action.key_down(Keys.CONTROL).click(new_tab_link).key_up(Keys.CONTROL).perform()
    for i in range(5):
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/div/form/div/input").send_keys(products[i])
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/div/form/div/button").click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/div/ul/li")))
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/div/ul/li").click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/div/div/div/div[1]/div/div[2]/form/div[2]/button")))
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/div/div/div/div[1]/div/div[2]/form/div[2]/button").click()
        if i != 4:
            driver.switch_to.window(driver.window_handles[i+1])
        else:
            driver.switch_to.window(first_tab_handle)
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/a/img").click()
            WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[11]/div/div/div/div/div/div/div/div[1]/a/div/img")))
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[4]").click()
            WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[4]/div[4]/div[5]")))
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[4]/div[4]/div[5]").click()
            sleep(10)

 
t = Timer(60, lixya_automation)
t.start()




   





