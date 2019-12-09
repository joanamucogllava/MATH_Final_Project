# Prims goes here
from functions.graph_operations import check_tree, add_new_edge;
    
def prims(G, v):
 
    T = ([v], [])
  
    while check_tree(G,T) == 0:
        T = add_new_edge(G,T)
    return T
