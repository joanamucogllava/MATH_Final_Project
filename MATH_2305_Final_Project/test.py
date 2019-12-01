from functions.reading_writing_functions import get_graph
from functions.graph_operations import incident_edges, cost, min_cost_incident_edge, add_new_edge


G = get_graph('G1.txt')

print('')
print(f'V(G) = {G[0]}')  #print all vertices
print('')
print(f'E(G) = {G[1]}')  #print all edges

#initialize tree

T = ( [3, 1, 4], [ (1, 3), (1, 4) ] )

print('')
print(f' T = {T}')  #print tree

#print incident edges with costs
print('')
for e in incident_edges(G, T):
    print(f'The cost of edge {e} is {cost(G, e)}')
    
#print edge with minimum cost
minedge = min_cost_incident_edge(G, T)
print('')
print(f'The edge with minimum cost is {minedge}, with a cost of {cost(G, minedge)}')

#print edge with minimum cost

T = add_new_edge(G, T)
print('')
print(f'the new tree is: T = { T }')

