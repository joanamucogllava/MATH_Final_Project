# Prims goes here

import check_tree;
import add_new_edge;
    
def prims(G, v):
 
    T = ([v], [])
  
    while check_tree(G,T) == 0:
        add_new_edge(G,T)
    return T
