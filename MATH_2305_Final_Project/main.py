from algorithms import prims
from functions.graph_operations import graph_cost

text = input('Please provide a graph to run the TSP on ')
G = text

text = input('Please provide a starting vertex ')
v = text

T = prims(G, v )
print(f'Optimal Tree is {T}')
print('')
print(f'Optimal cost: {graph_cost(T)}')
