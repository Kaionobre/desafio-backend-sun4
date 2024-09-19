from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
import time
from navegador import *


browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.tjpb.jus.br/comarcas/lista')

#cidades = browser.find_elements(By.CSS_SELECTOR, ".col-xs-6.col-sm-3")

for cidade in encontrar_cidades(browser):
    
    time.sleep(3)
    cidade_falha = cidade.get_attribute('style')

    if cidade_falha:
        continue
    else:
        while True:
            try:
                time.sleep(1.5)
                cidade.click()
                break
            except Exception as e:
                print(f"Erro ao clicar na cidade: {e}")
                continue  # Tenta clicar novamente
        
        while True:
            try:
                modal = browser.find_element(By.ID, "modal-detalhes-comarca")
                break
            except:
                continue

        while True:
            try:
                unidade = modal.find_element(By.CSS_SELECTOR, '#modal-detalhes-comarca > div > div > div.modal-body > table > tbody > tr > td:nth-child(1)')
                break
            except:
                continue

        while True:
            try:
                juiz = modal.find_element(By.CSS_SELECTOR, '#modal-detalhes-comarca > div > div > div.modal-body > table > tbody > tr > td:nth-child(2)')
                break
            except:
                continue

        while True:
            try:
                time.sleep(1)
                fechar_modal = modal.find_element(By.XPATH, '//*[@id="modal-detalhes-comarca"]/div/div/div[1]/button')
                if fechar_modal.is_displayed():
                    time.sleep(3)
                    fechar_modal.click()
                    print(f'cidade {cidade.text}, unidade {unidade.text}, juiz {juiz.text}')
                    break
            except:
                print('elemento não aparece')
                continue


# def q6_bot_consulta_jurisdicao():
    # """Realizar uma busca de todas as comarcas, suas respectivas jurisdições e os juízes.

    # A consulta é realizada através do site: https://www.tjpb.jus.br/comarcas/lista
    # O bot deve interagir com cada cidade, abrindo o modal, coletando as informações (ex.: vara única - juiz X)

    # Saída esperada: {cidade: "", jurisdicoes: [{jurisdicao1: juiz1, jurisdicao2: juiz2}]}
    # """

    # return {}