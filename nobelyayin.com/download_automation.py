from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import os

def downloading_automation():

#Masaüstüne ilgili dosyaları indireceğimiz klasörü oluşturmak:
    os.mkdir("C:/Users/Kaan/Desktop/nobelyayin_kitaplar")

#Driver kurulumu default folder'ın ayarlanması:
    optionss = webdriver.ChromeOptions()
    #prefs={"download.default_directory":r"C:\\Users\\Kaan\\Desktop\\nobelyayin_kitaplar"}
    optionss.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\Kaan\Desktop\nobelyayin_kitaplar",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True})
    driver = webdriver.Chrome(options=optionss)

#Otomasyonun başlatılması:
    driver.get("https://www.nobelyayin.com/")
    WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Fiyat Listesi")))
    driver.find_element(By.LINK_TEXT, "Fiyat Listesi").click()
    driver.set_window_size(1936, 1066)

# Kişisel Gelişim kategorisindeki alt kategorilerin "indir" butonlarına tıklanılarak ilgili dosyalar indirilir:
    WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".listeBosluk_1:nth-child(347) > a:nth-child(2)")))
    for i in range(9):
        total = 347 + i
        driver.find_element(By.CSS_SELECTOR, ".listeBosluk_1:nth-child({}) > a:nth-child(2)".format(total)).click()
    sleep(2)

downloading_automation()
    
    

   