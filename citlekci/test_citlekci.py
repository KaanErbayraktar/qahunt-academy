import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

class test_citlekci():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.vars = {}
        self.driver.get("https://www.citlekci.com.tr")
        self.driver.maximize_window()

    def test_bos_login(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.citlekci.com.tr")       
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Üye Girişi").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/form/div[6]/div[2]/div[1]/div/div/div[1]/div/div[1]/button")))
        self.driver.find_element(By.XPATH,"/html/body/form/div[6]/div[2]/div[1]/div/div/div[1]/div/div[1]/button").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/form/div[6]/div[2]/div[1]/div/div/div[1]/div/div[1]/div[1]/label[1]")))
        assert self.driver.find_element(By.XPATH, "/html/body/form/div[6]/div[2]/div[1]/div/div/div[1]/div/div[1]/div[1]/label[1]").text == "Bu Alan Zorunludur"

    def test_add_cart(self):
        self.driver.get("https://www.citlekci.com.tr/")
        self.driver.set_window_size(1936, 1066)
        self.driver.find_element(By.LINK_TEXT, "Yeni Ürünler").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ItemOrj:nth-child(1) .urunListeSpanSepeteEkle").click()
        self.driver.find_element(By.CSS_SELECTOR, ".fancybox-item").click()
        self.driver.find_element(By.CSS_SELECTOR, ".sepetTecxt").click()
        assert self.driver.find_element(By.LINK_TEXT, "Çitlekçi A.Fıstıklı Çekme Helva(100gr)").text == "Çitlekçi A.Fıstıklı Çekme Helva(100gr)"

