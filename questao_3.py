from datetime import datetime

def q3_tratar_datas(data):
    """Tratar e converter datas para o formato americano AAAA-MM-DD.
    
    Saída esperada: 2022-11-30"""

DATAS_PARA_TRATAR = [
    '30/11/2022',
    '01 dez 2022', 
    '25/12/2022', 
    '31 de dezembro de 2022'
]


for data in DATAS_PARA_TRATAR:
    print(q3_tratar_datas(DATAS_PARA_TRATAR))