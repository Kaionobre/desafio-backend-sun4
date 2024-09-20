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


def botao_fechar(browser, modal):
    while True:
        try:
            time.sleep(1)
            fechar_modal = modal.find_element(By.XPATH, '//*[@id="modal-detalhes-comarca"]/div/div/div[1]/button')
            if fechar_modal.is_displayed():
                time.sleep(3)
                fechar_modal.click()
                break
        except:
            print('elemento não aparece')
            continue


def mostrar_resultado(cidade, unidade, juiz):
    print(f'cidade {cidade.text}, unidade {unidade.text}, juiz {juiz.text}')



def ler_unidade_e_juiz(browser, modal):
    unidades = []
    juizes  = []

    while True:
        try:
            linhas = modal.find_elements(By.CSS_SELECTOR, '#modal-detalhes-comarca > div > div > div.modal-body > table > tbody')

            for linha in linhas:
                dado = linha.find_elements(By.TAG_NAME, 'td')

                if len(dado) >= 2:
                    unidade = dado[0].text
                    juiz = dado[1].text
                    unidades.append(unidade)
                    juizes.append(juiz)
            break
        except:
            continue

    return unidades, juizes

    
def ler_unidade(browser, modal): 
    while True:
        try:
            time.sleep(2)
            unidade = modal.find_element(By.CSS_SELECTOR, '#modal-detalhes-comarca > div > div > div.modal-body > table > tbody > tr > td:nth-child(1)')
            break
        except:
            continue
    return unidade.text

def ler_juiz(browser, modal):

    while True:
        try:
            time.sleep(2)
            juiz = modal.find_element(By.CSS_SELECTOR, '#modal-detalhes-comarca > div > div > div.modal-body > table > tbody > tr > td:nth-child(2)')
            break
        except:
            continue

    return juiz.text