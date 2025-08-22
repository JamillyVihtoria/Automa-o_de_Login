from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

#Limpa os logs de avisos
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

#Acessa o site  
driver.get('https://www.saucedemo.com/')

#Econtra o elemento da div e preenche e clica no login
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
time.sleep(1)
driver.find_element(By.ID,'user-name').send_keys('standard_user')
time.sleep(1)
driver.find_element(By.ID,'password').send_keys('secret_sauce')
time.sleep(1)
driver.find_element(By.ID, 'login-button').click()
time.sleep(1)

#Identifica a tela incial e clica no aviso da senha
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
time.sleep(2)
pyautogui.click(x=877, y=466)
time.sleep(2)

#Localiza os botões na div e coloca as roupas no carrinho
driver.find_element(By.ID,'add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.ID,'add-to-cart-sauce-labs-bike-light').click()
time.sleep(3)
print("Produtos adicionados ao carrinho!")

#Mostra o carrinho
pyautogui.click(x=1237, y=228)
time.sleep(5)

print("TESTE PASSOU: LOGIN BEM-SUCEDIDO")
