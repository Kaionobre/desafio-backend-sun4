def q1_remover_duplicados(nums):
    """Retorna uma lista com apenas um registro de cada elemento
    Saída esperada: [1, 2, 3, 4, 5]"""

    lista = list(set(nums))
    return lista

print(q1_remover_duplicados([1, 2, 2, 3, 4, 4, 5]))






