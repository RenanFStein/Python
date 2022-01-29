
from fileinput import close
from turtle import clear
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

# VARIAVEL DRIVE CHAMA O O WEBDRIVER 

driver = webdriver.Chrome(executable_path=r'C:\Users\renan\AppData\Local\Programs\Python\Python310\chromedriver.exe')

#DRIVER.GET VAI ABRIR O SITE ESCOLHIDO

driver.get('https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/cotacoes/')
time.sleep(1)

driver.get('https://www.youtube.com/')
time.sleep(1)

# usando .clear pra limpar qualquer preenchimento no campo de busca
driver.find_element_by_name('search_query').clear()
# usando o .send_keys para colocar o texto a ser preenchido no campo de busca
driver.find_element_by_name('search_query').send_keys('Aprendendo automação Python')
driver.find_element_by_name('search_query').send_keys(Keys.RETURN)
time.sleep(1)

# usando o .click pra apertar sobre a busca no Youtube conforme .send_keys
driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string').click()
time.sleep(1)

# DAQUI PRA BAIXO É PRATICAMENTE OS ELEMENTOS ACIMA EM DIVERSAS PAGINAS/BUSCAS
driver.find_element_by_name('search_query').clear()
driver.find_element_by_name('search_query').send_keys('Engenharia de Software')
driver.find_element_by_name('search_query').send_keys(Keys.RETURN)
time.sleep(1)

driver.get('https://www.google.com/')
time.sleep(1)

driver.find_element_by_name('q').clear()
driver.find_element_by_name('q').send_keys('B3')
driver.find_element_by_name('q').send_keys(Keys.RETURN)
time.sleep(1)

driver.find_element_by_name('q').clear()
driver.find_element_by_name('q').send_keys('MGLU3')
driver.find_element_by_name('q').send_keys(Keys.RETURN)
time.sleep(1)

driver.find_element_by_name('q').clear()
driver.find_element_by_name('q').send_keys('VALE3')
driver.find_element_by_name('q').send_keys(Keys.RETURN)
time.sleep(1)

driver.find_element_by_name('q').clear()
driver.find_element_by_name('q').send_keys('SANB11')
driver.find_element_by_name('q').send_keys(Keys.RETURN)
time.sleep(1)

driver.find_element_by_name('q').clear()
driver.find_element_by_name('q').send_keys('MXRF11')
driver.find_element_by_name('q').send_keys(Keys.RETURN)
time.sleep(1)

driver.find_element_by_name('q').clear()
driver.find_element_by_name('q').send_keys('PETR4')
driver.find_element_by_name('q').send_keys(Keys.RETURN)
time.sleep(1)

driver.find_element_by_name('q').clear()
driver.find_element_by_name('q').send_keys('INVESTIMENTOS')
driver.find_element_by_name('q').send_keys(Keys.RETURN)
time.sleep(1)

driver.find_element_by_name('q').clear()
driver.find_element_by_name('q').send_keys('CURSO AUTOMAÇÃO SELENIUM')
driver.find_element_by_name('q').send_keys(Keys.RETURN)
time.sleep(1)

driver.find_element_by_name('q').clear()
driver.find_element_by_name('q').send_keys('SELENIUM')
driver.find_element_by_name('q').send_keys(Keys.RETURN)
time.sleep(1)

driver.find_element_by_name('q').clear()
driver.find_element_by_name('q').send_keys('PYTHON')
driver.find_element_by_name('q').send_keys(Keys.RETURN)
time.sleep(1)

driver.find_element_by_name('q').clear()
driver.find_element_by_name('q').send_keys('DESENVOLVEDOR PYTHON')
driver.find_element_by_name('q').send_keys(Keys.RETURN)
time.sleep(1)

driver.find_element_by_name('q').clear()
driver.find_element_by_name('q').send_keys('DESENVOLVEDOR WEB')
driver.find_element_by_name('q').send_keys(Keys.RETURN)
time.sleep(1)

driver.quit()


