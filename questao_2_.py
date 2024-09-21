def q2_contar_frequencia_palavra(text: str):
    """Realiza uma contagem de quantas vezes uma determinada palavra ocorre
    Ao final, preferencialmente, ordenar o dicionário pelo volume de ocorrência

    Saída esperada: {'hello': 2, 'world': 1}
    """
    palavras = text.lower().split(' ')
    dicionario_palavra_repetida = {}

    for palavra in palavras:
        if palavra in dicionario_palavra_repetida:
            dicionario_palavra_repetida[palavra] +=1
        else:
            dicionario_palavra_repetida[palavra] = 1

    return dicionario_palavra_repetida

print(q2_contar_frequencia_palavra("Hello world hello"))