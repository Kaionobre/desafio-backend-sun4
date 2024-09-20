from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
import time
from navegador import *

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.tjpb.jus.br/comarcas/lista')

dados_comarcas = {}

for cidade in encontrar_cidades(browser):

    nome_da_ciadde = cidade.text.strip()
    
    if cidades_com_falha(browser, cidade):
        continue
    else:

        clicar_na_cidade(browser, cidade)

        modal = browser.find_element(By.ID, "modal-detalhes-comarca")

        jurisdicoes = []

        # unidade = ler_unidade(browser, modal)
        # juiz = ler_juiz(browser, modal)
        unidades, juizes = ler_unidade_e_juiz(browser, modal)

        for unidade, juiz in zip(unidades, juizes):
            jurisdicoes.append({unidade: juiz})

        botao_fechar(browser, modal)

        dados_comarcas[nome_da_ciadde] = jurisdicoes

        print(dados_comarcas) 

# def q6_bot_consulta_jurisdicao():
    # """Realizar uma busca de todas as comarcas, suas respectivas jurisdições e os juízes.

    # A consulta é realizada através do site: https://www.tjpb.jus.br/comarcas/lista
    # O bot deve interagir com cada cidade, abrindo o modal, coletando as informações (ex.: vara única - juiz X)

    # Saída esperada: {cidade: "", jurisdicoes: [{jurisdicao1: juiz1, jurisdicao2: juiz2}]}
    # """

    # return {}