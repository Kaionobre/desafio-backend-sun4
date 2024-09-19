from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
import time

def encontrar_cidades(browser):
    cidades = browser.find_elements(By.CSS_SELECTOR, ".col-xs-6.col-sm-3")
    return cidades


