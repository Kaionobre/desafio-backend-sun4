def q1_remover_duplicados(nums):
    """Retorna uma lista com apenas um registro de cada elemento
    
    Saída esperada: [1, 2, 3, 4, 5]"""
    return nums

print(q1_remover_duplicados([1, 2, 2, 3, 4, 4, 5]))


def q2_contar_frequencia_palavra(text):
    """Realiza uma contagem de quantas vezes uma determinada palavra ocorre
    Ao final, preferencialmente, ordenar o dicionário pelo volume de ocorrência

    Saída esperada: {'hello': 2, 'world': 1}
    """
    return {}

print(q2_contar_frequencia_palavra("Hello world hello"))

def q3_tratar_datas(data):
    """Tratar e converter datas para o formato americano AAAA-MM-DD.
    
    Saída esperada: 2022-11-30"""
    return data

DATAS_PARA_TRATAR = [
    '30/11/2022',
    '01 dez 2022', 
    '25/12/2022', 
    '31 de dezembro de 2022'
]
for data in DATAS_PARA_TRATAR:
    print(q3_tratar_datas(DATAS_PARA_TRATAR))

def q4_converter_arrays_em_dict(arr1, arr2):
    """Converter os arrays recebidos em um dicionário. O arr1 deve ser utilizado como chaves e o arr2 como valores.
    
    Saída esperada: {chave: valor, chave2: valor2}"""
    return {}

CHAVES = ['data_distribuicao', 'valor_da_causa', 'classe_judicial', 'assunto']
VALORES = ['14/04/2024', 'R$ 810,26', 'EXECUÇÃO DE TÍTULO EXTRAJUDICIAL (12154)', 'Nota Promissória (4980)']
print(q4_converter_arrays_em_dict(CHAVES, VALORES))

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

def q6_bot_consulta_jurisdicao():
    """Realizar uma busca de todas as comarcas, suas respectivas jurisdições e os juízes.

    A consulta é realizada através do site: https://www.tjpb.jus.br/comarcas/lista
    O bot deve interagir com cada cidade, abrindo o modal, coletando as informações (ex.: vara única - juiz X)

    Saída esperada: {cidade: "", jurisdicoes: [{jurisdicao1: juiz1, jurisdicao2: juiz2}]}
    """
    return {}