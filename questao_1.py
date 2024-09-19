def q1_remover_duplicados(nums):
    """Retorna uma lista com apenas um registro de cada elemento
    Saída esperada: [1, 2, 3, 4, 5]"""

    lista_sem_repetidos = []

    for i in nums: 
        if i not in lista_sem_repetidos:
            lista_sem_repetidos.append(i)
    
    return lista_sem_repetidos

print(q1_remover_duplicados([1, 2, 2, 3, 4, 4, 5]))





