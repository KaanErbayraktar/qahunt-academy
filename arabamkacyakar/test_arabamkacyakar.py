from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
from threading import Timer



def test_arabamkacyakar():
    driver = webdriver.Chrome()
    driver.get("https://arabamkacyakar.com/yakit-tuketimi-hesapla")
    driver.set_window_size(1936, 1066)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/label[2]")))
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/label[2]").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div/span[2]/input[2]").send_keys("Ankara")
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div/span[2]/span[2]/div/span/div[1]")))
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div/span[2]/span[2]/div/span/div[1]").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[3]/div/span[2]/input[2]").send_keys("Kayseri")
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[3]/div/span[2]/span[2]/div/span/div[1]")))
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[3]/div/span[2]/span[2]/div/span/div[1]").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div/label[1]").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[1]/label/select")))
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[1]/label/select").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[1]/label/select/option[22]").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/label/select")))
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/label/select").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/label/select/option[2]").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/label/select")))
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/label/select").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/label/select/option[4]").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[4]/div/label/select")))
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[4]/div/label/select").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[4]/div/label/select/option[4]").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[5]/div/label/select")))
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[5]/div/label/select").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[5]/div/label/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/input[1]").click()
    sleep(2)

"/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[1]/label/select"


test_arabamkacyakar()

    