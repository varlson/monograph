import igraph as ig
import pandas as pd
# g1 = ig.Graph.Read_GraphML('input/filtred/fluvial.GraphML')
# ig.summary(g1)


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
        # if id in ids:
        #     print('ja existe')
        # else:
        #     print('nao existe')
        # ids.append(id)

        if geo_src not in geocodes:
            geocodes.append(geo_src)
            city_names.append(rows['NOME_CID_A'])

        if geo_trg not in geocodes:
            geocodes.append(geo_trg)
            city_names.append(rows['NOME_CID_B'])
        

        paxAmount = rows['VAR09']

        # if paxAmount == 0:
        #     print('sem conexao')
        # else:
        #     print('com conexao sim')

        # print(type(paxAmount))
        if not pd.isnull(paxAmount) and paxAmount != 0:
            weekly_frequency = paxAmount/52
            weights.append(weekly_frequency)


            edge_list.append((geo_src, geo_trg))
        # if pd.isnull(paxAmount):
        #     print(paxAmount, end=" ")
        #     print('invalid', end='\n')
        # else:
        #     print(paxAmount, end=" ")
        #     print('valid', end='\n')

    return (geocodes, city_names, edge_list, weights)


def settingCoord(graph):
    coordDF = pd.read_csv('input/cities_coord.csv')
    x_axis = list(coordDF['x'])
    y_axis = list(coordDF['y'])
    geocodes = list(coordDF['geocode'])

    for current_index, geocode in enumerate(graph.vs['geocode']):
        index = geocodes.index(geocode)
        graph.vs[current_index]['x'] = x_axis[index]
        graph.vs[current_index]['y'] = -1 * y_axis[index]
        # print(index)
    return graph

def aerailNetGenerator():
    dataFrame = pd.read_csv('input/aerial.csv')
    geocodes, city_names, edge_list,weights = getUniquesNodes(dataFrame)

    # print(len(city_names))
    # print(edge_list[:10])
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
    # print(graph.ecount(), end="\n")
    # print(graph.es['id'])

    return graph



def modalColorSetting():
    aerial = ig.Graph.Read_GraphML('input/filtred//aerial.GraphML')
    fluvial = ig.Graph.Read_GraphML('input/filtred//fluvial.GraphML')
    terrestrial = ig.Graph.Read_GraphML('input/filtred//terrestrial.GraphML')
    merged = ig.Graph.Read_GraphML('input/filtred//merged.GraphML')

    intersect = []
    for nodeCode in terrestrial.vs['geocode']:
        if nodeCode in aerial.vs['geocode'] or nodeCode in fluvial.vs['geocode']:
            intersect.append(nodeCode)
    
    # print(intersect)

    for nodecode in intersect:
        index = merged.vs['geocode'].index(nodeCode)

        merged.vs[index]['color'] = '#07aab3'

    _min, _max = min(merged.degree()), max(merged.degree())

    sizes = [ ((deg - _min)/(_max-_min))*8+7 for deg in merged.degree() ]
    # # print(sizes)
    merged.vs['size'] = sizes

    ig.plot(merged)

if __name__ == "__main__":
    modalColorSetting()

    # g = aerailNetGenerator()
    # g = settingCoord(g)
    # _min, _max = min(g.degree()), max(g.degree())

    # sizes = [ ((deg - _min)/(_max-_min))*8+10 for deg in g.degree() ]
    # # print(sizes)
    # g.vs['size'] = sizes
    # g.es['width'] = 0.39
    # g.write_graphml('input/filtred/aerial.GraphML')


    # # ig.plot(g)
    # ig.summary(g)
