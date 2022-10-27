from ast import Try
import sys
from threading import Timer
import time
import datetime
from selenium import webdriver #Coleta o nome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
#options.add_argument('--headless')
options.add_argument('window-size=800x600') # optional
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://ru.unb.br/index.php/cardapio-refeitorio")

cardapioDarcy = driver.find_element_by_xpath('/html/body/div[2]/div[3]/main/div[2]/div[11]/a')
cardapioPlanaltina = driver.find_element_by_xpath('/html/body/div[2]/div[3]/main/div[2]/div[15]')
cardapioCeilandia = driver.find_element_by_xpath('/html/body/div[2]/div[3]/main/div[2]/div[19]')
cardapioGama = driver.find_element_by_xpath('/html/body/div[2]/div[3]/main/div[2]/div[23]')
cardapioFazenda = driver.find_element_by_xpath('/html/body/div[2]/div[3]/main/div[2]/div[27]')
cardapioDarcy.click()


