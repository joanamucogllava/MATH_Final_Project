

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
    min, returnedge = cost(G, inedges[0]), [] #starting minimum and return edge
    for e in inedges:  #loop through incident edges
        edgecost = cost(G, e)
        if edgecost < min:  #if cost is smaller than minimum
            min = edgecost  #set minimum
            returnedge = e  #set return
        
    return returnedge
    
    
# graph cost returns the total weight of a graph