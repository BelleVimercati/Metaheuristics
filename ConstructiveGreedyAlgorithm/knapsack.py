def knapsack(capacity, profits, weights):
    items = [(profits[i], weights[i], round(profits[i]/weights[i], 3)) for i in range(len(weights))]      # Lista de itens (tuplas) com o valor de utilidade

    sortedItems = sorted(items, key = lambda tuple : tuple[2], reverse = True)                  # Lista de itens (tuplas) ordenados pelo valor de utilidade
    knapsackItems = [0 for i in range(len(items))]                                              # Lista de itens adicionados na mochila
    knapsackItemsProfit = 0                                                                     # Variável do valor atual da mochila
    knapsackItemsWeight = 0                                                                     # Variável do peso atual da mochila

    for item in range(len(sortedItems)):                                                        # Para cada item da lista ordenada
        if sortedItems[item][1] <= capacity:                                                    #   Se o peso do item observado for menor que a capacidade atual
            knapsackItems[item] = 1                                                             #       Adiciona o item na mochila
            knapsackItemsProfit += sortedItems[item][0]                                         #       Atualiza o valor atual da mochila
            knapsackItemsWeight += sortedItems[item][1]                                         #       Atualiza o peso atual da mochila
            capacity -= sortedItems[item][1]                                                    #       Diminui a capacidade atual da mochila
    
    return sortedItems, knapsackItems, knapsackItemsProfit, knapsackItemsWeight