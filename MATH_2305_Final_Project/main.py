from prims_algorithms import prims
from functions.graph_operations import tree_cost
from functions.reading_writing_functions import get_graph

text = input('Graph data file: ')
G = get_graph (text)

print('')
print(f'Selected Graph: G = {G}')

text = input('Starting vertex: ')
v = int(text)

T = prims(G, v)
print('')
print(f'Optimal Tree is: T = {T}')
print('')
print(f'OPtimal cost: { tree_cost(G,T)}')
