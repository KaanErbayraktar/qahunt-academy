import openpyxl
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

def automation():

    #Açılış ve işlem yapılacak sayfanın hazırlanması
    driver = webdriver.Chrome()
    driver.get("https://www.modamerve.com/")
    driver.set_window_size(1936, 1066)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#mainMenu > div > ul > li:nth-child(15) > a")))
    driver.find_element(By.CSS_SELECTOR, "#mainMenu > div > ul > li:nth-child(15) > a").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#mainColumn > div > div:nth-child(1) > div > div.product-image > a")))
    
    #İlgili bilgilerin tutulması için aynı sıra ile kaydedilmiş listeleri kullanıyoruz.
    web_links = []
    p_links = []
    comments = []
    usernames = []
    dates = []

    for i in range(11):
        o = str(i+1)

        #Web_Link
        web = driver.find_element(By.CSS_SELECTOR, "#mainColumn > div > div:nth-child({}) > div > div.product-image > a".format(o)).get_attribute("href")
        #Picture_Link
        picture = driver.find_element(By.CSS_SELECTOR, "#mainColumn > div > div:nth-child({}) > div > div.product-image > a > img".format(o)).get_attribute("src")
        #Comments
        comment = driver.find_element(By.CSS_SELECTOR, "#mainColumn > div > div:nth-child({}) > div > div.cart > div.text > div.comment".format(o)).text
        #Username
        username = driver.find_element(By.CSS_SELECTOR, "#mainColumn > div > div:nth-child({}) > div > div.cart > div.text > div.username".format(o)).text
        #Date
        date = driver.find_element(By.CSS_SELECTOR, "#mainColumn > div > div:nth-child({}) > div > div.cart > div.text > div.date".format(o)).text
        
        #Çekilen verilerin ilgili listelere eklenmesi
        web_links.append(web)
        p_links.append(picture)
        comments.append(comment)
        usernames.append(username)
        dates.append(date)

    #Çekilen dataların matris haline dönüştürülüp, excel dosyasına yazdırılması
    c = {'Kişi İsmi': usernames, 'Tarih': dates, 'Yorum': comments, 'Web Linki': web_links, 'Resim Linki': p_links}
    df = pd.DataFrame(c)
    df.to_excel('modamerve.xlsx')
    print(df)


automation()


