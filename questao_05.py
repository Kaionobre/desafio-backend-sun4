def q5_calculo_prazo(data, prazo, tipo):
    """A partir de uma data realize o cálculo de prazos considerando o tipo de contagem.

    O tipo pode ser CORRIDO ou UTEIS.
    Caso seja UTEIS apenas serão contados os dias segunda, terça, quarta, quinta e sexta.
    Caso seja CORRIDO, deve-se incluir a contagem também o sábado e o domingo.
    
    A contagem deve sempre iniciar do dia seguinte (o dia atual não é contado)!
    
    Ao final deve ser retornado a data final do prazo aceito.
    
    Saída esperada: 
    Data 16/09/2024, prazo de 7 dias úteis, a data final é no dia 25/09/2024 e para os dias corridos 23/09/2024"""
    return

print(q5_calculo_prazo("16/09/2024", 7, "UTEIS"))
print(q5_calculo_prazo("16/09/2024", 7, "CORRIDOS"))