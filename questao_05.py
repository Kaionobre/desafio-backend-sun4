from datetime import datetime, timedelta, date

def q5_calculo_prazo(data, prazo, tipo):
    """A partir de uma data realize o cálculo de prazos considerando o tipo de contagem.

    O tipo pode ser CORRIDO ou UTEIS.
    Caso seja UTEIS apenas serão contados os dias segunda, terça, quarta, quinta e sexta.
    Caso seja CORRIDO, deve-se incluir a contagem também o sábado e o domingo.
    
    A contagem deve sempre iniciar do dia seguinte (o dia atual não é contado)!
    
    Ao final deve ser retornado a data final do prazo aceito.
    
    Saída esperada: 
    Data 16/09/2024, prazo de 7 dias úteis, a data final é no dia 25/09/2024 e para os dias corridos 23/09/2024"""

    data = datetime.strptime(data, '%d/%m/%Y')

    dia = data.day
    mes = data.month
    ano = data.year

    data_percorrer = dia + 1
    data_inicial_formatada = data.strftime('%d/%m/%Y')

    if tipo == 'CORRIDOS':
        data_corrida = dia + prazo
        nova_data = datetime(ano, mes, data_corrida)
        data_formatada = nova_data.strftime('%d/%m/%Y')
        return (f'Data {data.strftime('%d/%m/%Y')}, prazo de {prazo} dias corridos, a data final é no dia {data_formatada}')
    
    elif tipo == 'UTEIS':
        
        dias_adicionados = 0
        while dias_adicionados < prazo:
            data += timedelta(days=1)
            if data.weekday() < 5:
                dias_adicionados += 1

        data_final = data.strftime('%d/%m/%Y')

        return f"Data {data_inicial_formatada}, prazo de {prazo} dias úteis, a data final é no dia {data_final}"

print(q5_calculo_prazo("11/09/2024", 7, "UTEIS"))
print(q5_calculo_prazo("16/09/2024", 7, "CORRIDOS"))