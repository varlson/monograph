
import igraph as ig
import pandas as pd
import matplotlib.pyplot as plt

def getUniquesNodes(daframe):
    geocodes =[]
    city_names =[]
    edge_list=[]
    weights=[]
    ids = []

    for index, rows in daframe.iterrows():

        geo_src = rows['COD_CID_A']
        geo_trg = rows['COD_CID_B']

        id = str(int(geo_src))+str(int(geo_trg))

        if geo_src not in geocodes:
            geocodes.append(geo_src)
            city_names.append(rows['NOME_CID_A'])

        
        if geo_trg not in geocodes:
            geocodes.append(geo_trg)
            city_names.append(rows['NOME_CID_B'])
        

        paxAmount = rows['VAR09']

        if not pd.isnull(paxAmount) and paxAmount != 0 and geo_src != geo_trg:
            weekly_frequency = paxAmount/52
            weights.append(weekly_frequency)
            edge_list.append((geo_src, geo_trg))

    return (geocodes, city_names, edge_list, weights)



def aerailNetGenerator():
    dataFrame = pd.read_csv('datas/aerial.csv')
    geocodes, city_names, edge_list,weights = getUniquesNodes(dataFrame)

    N = len(geocodes)
    graph = ig.Graph(N)
    graph.vs['geocode'] = geocodes
    graph.vs['NOMEMUN'] = city_names

    for curr_index, edge in enumerate(edge_list):
        src, trg = geocodes.index(edge[0]), geocodes.index(edge[1])
        graph.add_edge(src, trg)
        id = str(int(edge[0]))+str(int(edge[1]))
        index = graph.ecount()-1
        graph.es[index]['id'] = id
        graph.es[index]['weight'] = weights[curr_index]

    return graph

def nodeSizeSetter(g):
    _min, _max = min(g.degree()), max(g.degree())
    sizes = [ ((deg - _min)/(_max-_min))*8+10 for deg in g.degree() ]
    g.vs['size'] = sizes
    g.es['width'] = 0.39

    return g






def setVisualization(g):

    aerial = ig.Graph.Read_GraphML('datas/aerial.GraphML')
    fluvial = ig.Graph.Read_GraphML('datas/fluvial.GraphML')
    terrestrial = ig.Graph.Read_GraphML('datas/terrestrial.GraphML')
    merged = ig.Graph.Read_GraphML('datas/merged.GraphML')

    colors = ["#9b0ff2", "#eb2161", "#217ceb", "#187835"]
    colors.reverse()

    for (g, gname, color) in zip([aerial,fluvial, terrestrial, merged], ['aerial', 'fluvial', 'terrestrial', 'merged'],colors):
        g = settingCoord(g)
        g.vs['size'] = nodeSizeSetter(g)
        g.es['width'] = 0.39
        g.vs['color'] = color
        ig.plot(g, f"results/{gname}.png", bbox=(0,0,1000,1000), dpi=3000)

    for index, nodeGeocode in enumerate(merged.vs['geocode']):
        if nodeGeocode not in (aerial.vs['geocode'] + fluvial.vs['geocode']):
            merged.vs[index]['color'] = "#217ceb"
    ig.plot(g, "results/merged.png", bbox=(0,0,1000,1000), dpi=3000)



def settingCoord(graph):
    coordDF = pd.read_csv('datas/cities_coord.csv')
    x_axis = list(coordDF['x'])
    y_axis = list(coordDF['y'])
    geocodes = list(coordDF['geocode'])

    for current_index, geocode in enumerate(graph.vs['geocode']):
        index = geocodes.index(geocode)
        graph.vs[current_index]['x'] = x_axis[index]
        graph.vs[current_index]['y'] = 1 * y_axis[index]
        # print(index)
    return graph


if __name__ == "__main__":
    fig, ax = plt.subplots(figsize=(5,5))
    g = aerailNetGenerator()
    g = settingCoord(g)
    g = nodeSizeSetter(g)
    
    ig.plot(g, target=ax)
    plt.show()
    g.write_graphml('datas/aerial.GraphML')

