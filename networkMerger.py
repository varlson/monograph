# from fakeNet import g1, g2
import pandas as pd
import igraph as ig


def extractTheUniquesNodes(graphLst):
    alluniqueGeocodes=[]
    infos = []
    index =0
    for graph in graphLst:
        for currentiIndex, geocode in enumerate(graph.vs['geocode']):
            if geocode not in alluniqueGeocodes:
                alluniqueGeocodes.append(geocode)
                x,y, color, cityName = graph.vs['x'][currentiIndex], graph.vs['y'][currentiIndex], graph.vs['color'][currentiIndex], graph.vs['name'][currentiIndex]
                infos.append((x, y, color, cityName))
   
    # alluniqueGeocodes = set(graphLst[0].vs['geocode'] + graphLst[1].vs['geocode'] + graphLst[2].vs['geocode'])
    return  (len(alluniqueGeocodes), alluniqueGeocodes, infos)


def networkMerger(graphLst):
    N, uniqGeocodes, infos = extractTheUniquesNodes(graphLst)
    x_coords, y_coords, colors, citynames = zip(*infos)
    
    # print('uniqGeocodes')
    # print(uniqGeocodes)
    G = ig.Graph(N)
    G.es['id'] = ['' for _ in range(N-1)] 
    G.vs['geocode'] = uniqGeocodes
    G.vs['x']= list(x_coords)
    G.vs['y']= list(y_coords)



    # print(x_coords, y_coords, colors, citynames)
    G.vs['name']= list(citynames)
    G.vs['color'] = list(colors)


    for graphIndex, graph in enumerate(graphLst):
        for index, edgeID in enumerate(graph.es['id']):
            srcNodeCode = float(edgeID[:7])
            trgNodeCode = float(edgeID[7:])
            srcNodeIndex = G.vs['geocode'].index(srcNodeCode)
            trgNodeIndex = G.vs['geocode'].index(trgNodeCode)

            # if graphIndex == 0 and index ==0:
            #     G.add_edge(srcNodeIndex, trgNodeIndex)
            #     lastEdgeIndex = 0
            #     G.es[lastEdgeIndex]['id'] = edgeID
            #     G.es[lastEdgeIndex]['weight'] = graph.es['weight'][index]
            # else:
            if edgeID not in G.es['id']:
                
                # print(G.es['id'], end="  -  ")
                # print(edgeID, end="\n")

                G.add_edge(srcNodeIndex, trgNodeIndex)
                lastEdgeIndex = G.ecount()-1
                G.es[lastEdgeIndex]['id'] = edgeID
                G.es[lastEdgeIndex]['weight'] = graph.es['weight'][index]
            else:
                existedIndex = G.es['id'].index(edgeID)
                G.es[existedIndex]['weight'] += graph.es['weight'][index]
    return G

if __name__ == "__main__":
    aerialNet = ig.Graph.Read_GraphML('../networkBuilder/input/filtred/aerial.GraphML')
    # fluvial datas
    fluvialNet = ig.Graph.Read_GraphML('../networkBuilder/input/filtred/fluvial.GraphML')

    # terrestrial datas
    terrestrialNet = ig.Graph.Read_GraphML('../networkBuilder/input/filtred/terrestrial.GraphML')

    G = networkMerger([terrestrialNet, aerialNet, fluvialNet])
    _min, _max = min(G.degree()), max(G.degree())
    sizes = [ ((deg - _min)/(_max-_min))*8+10 for deg in G.degree() ]
    # print(sizes)
    G.vs['size'] = sizes
    G.es['width'] = 0.39

    G.write_graphml('input/filtred/merged.GraphML')
    ig.summary(G)
#     ig.plot(G)

# G = networkMerger([g1, g2])

# print(g1.es['weight'])
# print(g1.es['id'], end="\n\n")
# print(g2.es['weight'])
# print(g2.es['id'], end="\n\n")
# print(G.es['weight'])
# print(G.es['id'], end="\n\n")
# # G.vs['label'] = [x for x in G.vs['geocode']]
# # g1.vs['label'] = [x for x in g1.vs['geocode']]
# # g2.vs['label'] = [x for x in g2.vs['geocode']]
# # G.es['label'] = [int(x) for x in range (G.ecount())]


# ig.plot(G)