# Problema da Mochila
# Alunos: Isabelle Vimercati e Marcus Bispo

from random import randint
import parameters as p
import knapsack as k
import movement as m

weights = [randint(p.minWeight, p.maxWeight) for i in range(p.itemsQuantity)]
profits = [randint(p.minProfit, p.maxProfit) for i in range(p.itemsQuantity)]

sortedItems, knapsackItems, knapsackProfit, knapsackWeight = k.knapsack(p.knapsackCapacity, profits, weights)


print(f'Sorted Items: {sortedItems}')
print(f'Knapsack Items: {knapsackItems}')
print(f'Knapsack Profit: {knapsackProfit}')
print(f'Knapsack Weight: {knapsackWeight}\n')

m.movement(p.knapsackCapacity, sortedItems, knapsackItems, knapsackProfit, knapsackWeight)