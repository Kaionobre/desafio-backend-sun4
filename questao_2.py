def q2_contar_frequencia_palavra(text):
    """Realiza uma contagem de quantas vezes uma determinada palavra ocorre
    Ao final, preferencialmente, ordenar o dicionário pelo volume de ocorrência

    Saída esperada: {'hello': 2, 'world': 1}
    """
    for i in text:
        print(i.split())

    return {text}

print(q2_contar_frequencia_palavra("Hello world hello"))
