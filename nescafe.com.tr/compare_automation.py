from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import random
import pandas as pd


def nescafe_automation():

    print("Test başlatılıyor...")
    print("*********************************************")
#Rastgele sayı üretip bu sayıları ileride kullanmak adına listede topluyoruz.
    x = 0
    y = 0
    quotes = []
    secimler = []
    for i in range(4):
        b = random.randint(1,4)
        if i == 1 and b == 4:
            b = random.randint(1,3)
        secimler.append(b)

#Otomasyonun başlatılması ve sitenin uygun halde başlatılması;
    driver = webdriver.Chrome()
    driver.get("https://www.nescafe.com/tr/")
    driver.set_window_size(1936, 1066)

#Mouse over edildiğinde açılan altmenüyü açılır hale getirmek için gerekli kodlar;
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/div/ul/li/label")))
    element = driver.find_element(By.XPATH, "//div/div/ul/li/label")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

#Açılan Nescafe'nizi Bulun fonksiyonun başlatılması;
    driver.find_element(By.CSS_SELECTOR, ".category-coffees .cell:nth-child(1)").click()
    WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "NESCAFÉ\'nizi Bulun")))
    driver.find_element(By.LINK_TEXT, "NESCAFÉ\'nizi Bulun").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[4]/main/section/div/section/form/section/div[1]/div[1]/div/div/div/div/div[2]/a")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[4]/main/section/div/section/form/section/div[1]/div[1]/div/div/div/div/div[2]/a").click()

#Döngüde önceki adımda rastgele seçilmiş sayılar kullanılarak seçimler yapılır ve text'ler kaydedilir.
    for i in range(4):
        a = i + 1
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "question-{}".format(a))))
        sleep(5)
        text = driver.find_element(By.CSS_SELECTOR, "#qs-{}-option-{} > div > div.container-text.show > span".format(a,secimler[i])).text
        quotes.append(text)
        driver.find_element(By.ID, "qs-{}-option-{}".format(a,secimler[i])).click()
    sleep(10)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#block-nescafe-design-refresh-content > section > div > div > div.coffee-profiler-result--top-img > div:nth-child(2) > div > h2:nth-child(3)")))
    sonuc = driver.find_element(By.CSS_SELECTOR, "#block-nescafe-design-refresh-content > section > div > div > div.coffee-profiler-result--top-img > div:nth-child(2) > div > h2:nth-child(3)").text
    print("Data almak için yapılan testin sonucu şu şekildedir:{}".format(sonuc))
    print("*********************************************")


#Sayılar ve döngüdeki textler kullanılarak Excel dosyası oluşturulur ve bu datalar excel dosyasından çekileceği için sıfırlanır.
    c = {'Sıra': secimler, 'Yazılar': quotes,}
    df = pd.DataFrame(c)
    df.to_excel('nescafe.xlsx')
    print("Seçim sırası ve text şablonu aşağıdaki gibidir:")
    print(df)
    print("*********************************************")

    secimler = []
    quotes = []

# Oluşturulan Excel dosyası okunarak ilgili seçim ve yazılar alınır.
    excel = pd.read_excel('nescafe.xlsx')
    df = pd.DataFrame(excel)
    for i in range(4):
        sıra = df.at[(i),"Sıra"]
        yazi = df.at[(i),"Yazılar"]
        secimler.append(sıra)
        quotes.append(yazi)
    sonuclar = []

# Excel'den alınan veriler kullanılarak aynı döngü 5 kere çalıştırılıp girdiler ve sonuç kontrol edilir.
    for i in range(5):
        driver.find_element(By.LINK_TEXT, "Testi tekrar yap").click()
        #WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "NESCAFÉ\'nizi Bulun")))
        #driver.find_element(By.LINK_TEXT, "NESCAFÉ\'nizi Bulun").click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[4]/main/section/div/section/form/section/div[1]/div[1]/div/div/div/div/div[2]/a")))
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[4]/main/section/div/section/form/section/div[1]/div[1]/div/div/div/div/div[2]/a").click()
        a = 1
        for z in secimler:
            WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "question-{}".format(a))))
            sleep(5)
            text = driver.find_element(By.CSS_SELECTOR, "#qs-{}-option-{} > div > div.container-text.show > span".format(a,z)).text
            if text != quotes[a-1]:
                print("Seçim sırasındaki Text'lerde Hata var!")
                x += 1
            driver.find_element(By.ID, "qs-{}-option-{}".format(a,z)).click()
            a += 1
        sleep(5)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#block-nescafe-design-refresh-content > section > div > div > div.coffee-profiler-result--top-img > div:nth-child(2) > div > h2:nth-child(3)")))
        yeni_sonuc = driver.find_element(By.CSS_SELECTOR, "#block-nescafe-design-refresh-content > section > div > div > div.coffee-profiler-result--top-img > div:nth-child(2) > div > h2:nth-child(3)").text
        sonuclar.append(yeni_sonuc)
        if yeni_sonuc != sonuc:
            print("Sonuçlar farklı geliyor!")
            y += 1

# Programın sonunda hata sayaçları kontrol edilerek fonksiyonda hata olup olmadığı test sonunda terminal'e yazılır.
    print("Her tekrar sonucunda elde edilen sonuçlar şu şekildedir:{}".format(sonuclar))
    print("*********************************************")
    if x == 0 and y == 0:
        print("Test hatasız tamamlandı.")
        print("*********************************************")
    elif x != 0 and y == 0:
        print("Seçim sırasındaki Text'lerde hata var fakat sonuç hatasız geliyor.")
        print("*********************************************")
    elif x == 0 and y != 0:
        print(" Sıra aynı şekilde seçildi fakat sonuç ilk örnekten farklı geliyor")
        print("*********************************************")
    else:
        print("Hem seçimdeki text'lerde hata var hem de sonuçta!!!")
        print("*********************************************")


nescafe_automation()






   


