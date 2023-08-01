from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import pytest

class Test_Epsikolog:

  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  def test_first(self):
# Testin yapılacağı site açılır ve ilgili adımlar uygulanmaya başlanır;
    driver = webdriver.Chrome()
    self.driver.get("https://www.evimdekipsikolog.com/")
    self.driver.set_window_size(1936, 1066)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#home-consultant-container > div:nth-child(1) > div:nth-child(3) > div.card-body.text-center.text-md-left > div > div.bs4-col > div > div.action-buttons.bs4-col-xl-auto.align-self-center.buttons.bs4-col-xl.mt-4.mt-xl-0 > button.bs4-btn.bs4-btn-sm.bs4-btn-blue.bs4-btn-block")))
    self.driver.find_element((By.CSS_SELECTOR, "#home-consultant-container > div:nth-child(1) > div:nth-child(3) > div.card-body.text-center.text-md-left > div > div.bs4-col > div > div.action-buttons.bs4-col-xl-auto.align-self-center.buttons.bs4-col-xl.mt-4.mt-xl-0 > button.bs4-btn.bs4-btn-sm.bs4-btn-blue.bs4-btn-block")).click
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#frm-app-buy > fieldset:nth-child(4)")))
    self.driver.find_element((By.CSS_SELECTOR, "#frm-app-buy > fieldset:nth-child(4) > div.list-group > a:nth-child(1)")).click

# Üçüncü psikologdan hizmet almak için randevu alma butonuna tıklanıp görüşmenin detaylarını ayarladığımız menüye gelip ayarlarımızı yapıyoruz;
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"body > div.jconfirm.jconfirm-light.jconfirm-open > div.jconfirm-scrollpane > div > div > div > div > div > div > div")))
    self.driver.find_element((By.CSS_SELECTOR, "body > div.jconfirm.jconfirm-light.jconfirm-open > div.jconfirm-scrollpane > div > div > div > div > div > div > div > div.jconfirm-buttons > button")).click
    self.driver.find_element((By.CSS_SELECTOR, "#frm-app-buy > fieldset:nth-child(4) > div.f1-buttons > button")).click

# 01.08.23 ve 20:00-21:00 tarih ve saatleri için randevuyu ayarlıyoruz;    
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#frm-app-buy > fieldset:nth-child(5)")))
    self.driver.find_element((By.CSS_SELECTOR, "#ScheduleDate")).click
    self.driver.find_element((By.CSS_SELECTOR, "#ScheduleDate")).send_keys("01.08.2023")
    self.driver.find_element((By.CSS_SELECTOR, "#ScheduleTime")).click
    self.driver.find_element((By.CSS_SELECTOR, "#ScheduleTime > option:nth-child(11)")).click
    self.driver.find_element((By.CSS_SELECTOR, "#frm-app-buy > fieldset:nth-child(5) > div.f1-buttons > button.btn.btn-next")).click

# Rumuz ayarlarını yapıyoruz;
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#frm-app-buy > fieldset:nth-child(6)")))
    self.driver.find_element((By.CSS_SELECTOR, "#NickName")).send_keys("QA Hunt")
    self.driver.find_element((By.CSS_SELECTOR, "#frm-app-buy > fieldset:nth-child(6) > div.f1-buttons > button.btn.btn-next")).click()

# Telefon kaydı ve gerekli sözleşmelerin okunduğunun onayı ve eksik onay bulunduğunda düzgün bir şekilde hata verildiğinin kontrolü;
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#frm-app-buy > fieldset:nth-child(7)")))
    self.driver.find_element((By.CSS_SELECTOR, "#PhoneNumber")).send_keys("5555555555")
    self.driver.find_element((By.CSS_SELECTOR, "#chkKvkk")).click()
    self.driver.find_element((By.CSS_SELECTOR, "#frm-app-buy > fieldset:nth-child(7) > div.f1-buttons > button.btn.btn-next")).click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#chkRegister")))
    assert self.driver.find_element((By.CSS_SELECTOR, "#chkRegister")).text == "Bu alanın doldurulması zorunludur."

    self.driver.find_element((By.CSS_SELECTOR, "#chkRegister")).click()
    self.driver.find_element((By.CSS_SELECTOR, "#frm-app-buy > fieldset:nth-child(7) > div.f1-buttons > button.btn.btn-next")).click()

# Görüşme kaydının yapılması için gereken şifrenin girildiği bölüme gelinir ve çeşitli hatalı seneryolar kontrol edilir;
    
    # Şifre alanı boş bırakıldığında;
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#frm-app-buy > fieldset:nth-child(6)")))
    self.driver.find_element((By.CSS_SELECTOR, "#btnAppLogin")).click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#Password-error")))
    assert self.driver.find_element((By.CSS_SELECTOR, "#Password-error")).text == "Lütfen şifrenizi giriniz."

    # Şifre alanına geçersiz şifre yazıldığında;
    self.driver.find_element((By.CSS_SELECTOR, "#Password")).send_keys("787878")
    self.driver.find_element((By.CSS_SELECTOR, "#btnAppLogin")).click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"body > div.jconfirm.jconfirm-light.jconfirm-open > div.jconfirm-scrollpane > div > div > div > div > div > div > div")))
    assert self.driver.find_element((By.CSS_SELECTOR, "#jconfirm-box40652 > div")).text == "Gecersiz sms kodu girdiniz, lütfen telefonunuza gelen kodu giriniz."




    
