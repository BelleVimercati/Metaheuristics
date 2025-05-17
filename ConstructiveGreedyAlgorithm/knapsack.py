class Knapsack:
    def __init__(self, capacity):   # Para instanciar uma mochila, precisamos apenas da capacidade dela
        self.capacity = capacity
    
    def calculate(self, profits, weights):
        self.putItems(profits, weights)
        self.sortItems()
        self.selectItems()
    
    def putItems(self, profits, weights):
        self.items = [(profits[i], weights[i], round(profits[i]/weights[i], 3)) for i in range(len(weights))]
    
    def sortItems(self):
        self.items = sorted(self.items, key = lambda tuple : tuple[2], reverse = True)
    
    def selectItems(self):
        self.selectedItems = [0 for i in range(len(self.items))]

        for item in range(len(self.items)):
            if self.items[item][1] <= self.capacity:
                self.selectedItems[item] = 1
                self.capacity -= self.items[item][1]
    
    def getItems(self):
        try:
            return self.items
        except:
            print('There are no items!')
    
    def getSelectedItems(self):
        try:
            return self.selectedItems
        except:
            print('There are no selected items!')
    
    def getKnapsackProfit(self):
        knapsackProfit = 0

        for item in range(len(self.selectedItems)):
            knapsackProfit += self.selectedItems[item] * self.items[item][0]
        
        return knapsackProfit
    
    def getKnapsackWeight(self):
        knapsackWeight = 0

        for item in range(len(self.selectedItems)):
            knapsackWeight += self.selectedItems[item] * self.items[item][1]
        
        return knapsackWeight