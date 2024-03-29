
def incident_edges(G, T):
        
    edges = []
    for e in G[1]:  #loop through all edges
        for v in T[0]:  #loop through all vertices
            cycle = 'false'  #not a cycle edge by default
            if v in e and e not in T[1]:  #if a vertex is in an edge and the edge is not already in the tree
                for secondv in T[0]:  #loop through all vertices again
                    if secondv is not v and secondv in e:  #if the vertex is a separate vertex and is also in the edge
                        cycle = 'true'  #it is a cycle edge
                if cycle == 'false':  #if it is not a cycle edge
                    edges.append(e)  #it's an incident edge
            
    return edges

def cost(G, e):
    return G[1][e]

def min_cost_incident_edge(G, T):
    
    inedges = incident_edges(G, T)  #get incident edges
    min, returnedge = cost(G, inedges[0]), inedges[0] #starting minimum and return edge
    for e in inedges:  #loop through incident edges
        edgecost = cost(G, e)
        if edgecost < min:  #if cost is smaller than minimum
            min = edgecost  #set minimum
            returnedge = e  #set return
        
    return returnedge

    
def add_new_edge(G, T):
     
     newedge = min_cost_incident_edge(G, T)
     T[1].append(newedge)
     for v in newedge: 
          if v not in T[0]:
              T[0].append(v)
        
     return T
   
# checks tree to see if it's path has been completed
def check_tree(G, T):
    
    g_len = len(G[0])
    t_len = len(T[0])
    
    if g_len == t_len:
        return 1
    else:
        return 0    
  
def tree_cost(G,T): # finds edgecost of tree
    treecost = 0
    for e in T[1]:
        treecost += cost(G,e)
    return treecost
