# import pandas as pd
import igraph as ig


def dataFilter (graph, output):
    g = graph.copy()
    del g.vs['LATI']
    del g.vs['LONG']

    x = graph.vs['LONG']
    y = graph.vs['LATI']

    y = [(-1)* current for current in y]

    g.vs['x'] = x
    g.vs['y'] = y
    g.vs['name'] = graph.vs['NOMEMUN']
    del g.vs['NOMEMUN']

    g.write_graphml(output)




# g = ig.Graph.Read_GraphML('networkBuilder/input/grafo_peso_rodo.GraphML')
g = ig.Graph.Read_GraphML('networkBuilder/input/grafo_peso_hidro.GraphML')
dataFilter(g, "networkBuilder/input/filtred/fluvial.GraphML")