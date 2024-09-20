from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
import time

def encontrar_cidades(browser):
    cidades = browser.find_elements(By.CSS_SELECTOR, ".col-xs-6.col-sm-3")
    return cidades

def cidades_com_falha(browser, cidade):
    time.sleep(0.5)
    cidade_falha = cidade.get_attribute('style')
    return cidade_falha

def clicar_na_cidade(browser, cidade):
    while True:
        try:
            time.sleep(1)
            cidade.click()
            break
        except Exception as e:
            print(f"Erro ao clicar na cidade: {e}")
            continue 

def ver_modal(browser):
    while True:
        try:
            modal = browser.find_element(By.ID, "modal-detalhes-comarca")
            break
        except:
            continue
    return modal

def ver_unidade(browser, modal):
    while True:
        try:
            unidade = modal.find_element(By.CSS_SELECTOR, '#modal-detalhes-comarca > div > div > div.modal-body > table > tbody > tr > td:nth-child(1)')
            break
        except:
            continue
        
    return unidade

def mostrar_resultado(cidade, unidade, juiz):
    print(f'cidade {cidade.text}, unidade {unidade.text}, juiz {juiz.text}')
