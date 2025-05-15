# Problema da Mochila
# Alunos: Isabelle Vimercati e Marcus Bispo

import knapsack as k

weights = []
profits = []

#Capturando as informações do arquivo txt
with open("items.txt", "r") as f:
    knapsackCapacity = int(f.readline().strip())
    for line in f:
        w, pr = map(int, line.strip().split())      
        weights.append(w)
        profits.append(pr)


sortedItems, knapsackItems, knapsackProfit, knapsackWeight = k.knapsack(knapsackCapacity, profits, weights)


print(f'Sorted Items: {sortedItems}')
print(f'Knapsack Items: {knapsackItems}')
print(f'Knapsack Profit: {knapsackProfit}')
print(f'Knapsack Weight: {knapsackWeight}\n')