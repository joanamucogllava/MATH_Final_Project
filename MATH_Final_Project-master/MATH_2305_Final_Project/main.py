from algorithms import prims
from functions.graph_operations import graph_cost
from fucntions.readin_writing_functions import get_graph

text = inut('Graph data file: ')
G = get_graph (text)

print('')
print(f'Selected Graph: G = {G}')

text = input('Starting vertex: ')
v = int(text)

T = prims(G, v)
print('')
print(f'Optimal Tree is: T = {T}')
print('')
print(f'OPtimal cost: { graph_cost(G,T)}')