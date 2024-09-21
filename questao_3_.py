from datetime import datetime, date
import locale

def q3_tratar_datas(data):
    """Tratar e converter datas para o formato americano AAAA-MM-DD.
    
    Saída esperada: 2022-11-30"""

    locale.setlocale(locale.LC_TIME, '')

    formatos = ['%d/%m/%Y', '%d %b %Y', '%d de %B de %Y']

    for formato in formatos:
        try:
            data_certa = datetime.strptime(data, formato).date()
            return data_certa.strftime('%Y-%m-%d')
        except:
            continue

DATAS_PARA_TRATAR = [
    '30/11/2022',
    '01 dez 2022', 
    '25/12/2022', 
    '31 de dezembro de 2022'
]

for data in DATAS_PARA_TRATAR:
    print(q3_tratar_datas(data))