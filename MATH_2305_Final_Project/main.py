from algorithms import *
from functions.graph_operations import graph_cost

text = input('Please provide a graph to run the TSP on ')

text = input('Please provide a starting vertex ')

T = prims(G, v )
print(f'Optimal Tree is {T}')
print('')
print(f'Optimal cost: {graph_cost(T)}')
