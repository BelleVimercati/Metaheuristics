from random import randint

#Definição dos parâmetros
knapsackCapacity = 50
itemsQuantity = 6

minWeight = 2
maxWeight = 30

minProfit = 2
maxProfit = 30


# Gera listas aleatórias com base nos parâmetros
weights = [randint(minWeight, maxWeight) for _ in range(itemsQuantity)]
profits = [randint(minProfit, maxProfit) for _ in range(itemsQuantity)]

# Salva no arquivo como: peso lucro
with open("items.txt", "w") as f:
    f.write(f"{knapsackCapacity}\n")
    for w, pr in zip(weights, profits):
        f.write(f"{w} {pr}\n")
