# 🧊 Metaheurísticas - Problema da Mochila com Simulated Annealing

Este projeto foi desenvolvido como parte da disciplina de Metaheurísticas, e tem como objetivo resolver o clássico Problema da Mochila 0/1 (Knapsack Problem) utilizando a técnica de otimização probabilística Simulated Annealing (SA).

O algoritmo busca encontrar uma combinação de itens que maximize o lucro total sem exceder a capacidade da mochila.

## 🔧 Parâmetros

Todos os parâmetros estão definidos no arquivo **generate_items.py**. Entre eles:

- knapsackCapacity: capacidade máxima da mochila.
- itemsQuantity: número de itens a serem gerados.
- minWeight / maxWeight: intervalo de pesos dos itens.
- minProfit / maxProfit: intervalo de lucros dos itens.

## 📥 Como Gerar os Itens

Execute o script de geração:

~~~terminal
    python generate_items.py
~~~

Isso criará (ou sobrescreverá) o arquivo items.txt, com a seguinte estrutura:

~~~txt
    <capacidade_da_mochila>
    <peso_1> <lucro_1>
    <peso_2> <lucro_2>
...
~~~

## 🚀 Como Executar o Algoritmo

Depois de gerar os itens, execute o script principal:

~~~terminal
    python main.py
~~~
