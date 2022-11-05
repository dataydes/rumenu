#code que baixa o pdf do site do r.u e salva em uma pasta;
from ast import Try
import sys
from threading import Timer
from selenium import webdriver #Coleta o nome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
import shutil
import time

#Apaga a pasta que receberá os pdfs
try:
    shutil.rmtree('./temp',ignore_errors=False, onerror=None)	
except:
    print("Pasta vazia")

#Cria a pastas que receberá os pdfs
path_loc = os.path.join(os.getcwd(), "temp")

#Configura o chromedriver
options = Options()
options.add_argument('--headless')
options.add_argument('window-size=800x600') # optional
chrome_prefs = {
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True,
    "download.open_pdf_in_system_reader": False,
    "profile.default_content_settings.popups": 0,
    # add location preference...
    "download.default_directory": path_loc
}
options.add_experimental_option("prefs", chrome_prefs)           
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://ru.unb.br/index.php/cardapio-refeitorio")
lnks=driver.find_elements_by_tag_name("a")
# traverse list
for lnk in lnks:
   # get_attribute() to get all href
   print(lnk)
driver.quit()



cardapioDarcy = driver.find_element_by_xpath('/html/body/div[2]/div[3]/main/div[2]/div[11]/a')
cardapioPlanaltina = driver.find_element_by_xpath('/html/body/div[2]/div[3]/main/div[2]/div[15]')
cardapioCeilandia = driver.find_element_by_xpath('/html/body/div[2]/div[3]/main/div[2]/div[19]')
cardapioGama = driver.find_element_by_xpath('/html/body/div[2]/div[3]/main/div[2]/div[23]')
cardapioFazenda = driver.find_element_by_xpath('/html/body/div[2]/div[3]/main/div[2]/div[27]')
cardapioDarcy.click()
time.sleep(1)
cardapioPlanaltina.click()
time.sleep(1)
cardapioCeilandia.click()
time.sleep(1)
cardapioGama.click()
time.sleep(1)
cardapioFazenda.click()
time.sleep(5)
driver.close()
exit()

