"""Abordagem Construtiva gulosa:
1. Ordenar os itens com o valor-peso
2. Selecionar os itens em ordem decrescente, adicionando apenas se couber na mochila.
Alunos: Marcus Bispo e Isabelle Vimercati
"""


def knapsack_01(values, weights, capacity):
    n = len(values)
    items = [(i, values[i], weights[i], values[i] / weights[i]) for i in range(n)]
    items.sort(key= lambda x: x[3], reverse=True)

    total_values = 0
    total_weights = 0
    selected_items = []

    for item in items:
        i , value, weight, _ = item
        if total_weights + weight <= capacity:
            selected_items.append((i,value,weight))
            total_values += value
            total_weights += weight

    return total_values, selected_items


values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, selected = knapsack_01(values, weights, capacity)
print("Valor máximo:", max_value);
print("Itens selecionados:", selected)
