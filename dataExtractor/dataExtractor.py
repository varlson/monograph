import pandas as pd
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

    _min, _max = min(g.degree()), max(g.degree())
    sizes = [ ((deg - _min)/(_max-_min))*8+10 for deg in g.degree() ]
    g.es['id'] = [str(int(deg)) for deg in g.es['id']]
    g.vs['size'] = sizes
    g.es['width'] = 0.34
    g.write_graphml(output)


def dataExtractorDriver():
    g1 = ig.Graph.Read_GraphML('../networkBuilder/input/grafo_peso_rodo.GraphML')
    g2 = ig.Graph.Read_GraphML('../networkBuilder/input/grafo_peso_hidro.GraphML')
    dataFilter(g2, "../networkBuilder/input/filtred/fluvial.GraphML")
    dataFilter(g1, "../networkBuilder/input/filtred/terrestrial.GraphML")


def sortDatasByMetrics(graph, lambdaFunction):
    metricValues = lambdaFunction(graph)
    filtred = [0 if pd.isnull(value) else value for value in metricValues]
    nodes= [x for x in range(graph.vcount())]
    geocodes = graph.vs['geocode']
    nodeTuple = list(zip(nodes, filtred, geocodes)) 
    # print(nodeTuple)
    sorted_tupleList = sorted(nodeTuple, key=lambda x:x[1], reverse=True)
    return sorted_tupleList


def covidCasesDataFilter(graph, outputName):
    df = pd.read_csv('input/cases-brazil-cities-time.csv')

    df_dates = list(df['date'])
    df_geocodes = list(df['ibgeID'])
    df_cities = list(df['city'])

    _tuples = []

    for geo in graph.vs['geocode']:
        index = df_geocodes.index(geo)
        city = df_cities[index]
        date = df_dates[index]
        _tuples.append((geo, city, date))

    _tuples = sorted(_tuples, key=lambda x:x[2])

    # print(_tuples)

    geocodes, cities, dates = zip(*_tuples)


    dict_res ={}
    dict_res['geocode'] = list(geocodes) 
    dict_res['cities'] =  list(cities)
    dict_res['dates'] =  list(dates)

    df_res = pd.DataFrame(dict_res)
    # print(df_res)

    df_res.to_csv(f'{outputName}_filtred_covid_cases_data.csv', index=False)


if __name__ == "__main__":
    # dataExtractorDriver()
    aerial = ig.Graph.Read_GraphML('../networkBuilder/input/filtred/aerial.GraphML')
    terrestrial = ig.Graph.Read_GraphML('../networkBuilder/input/filtred/terrestrial.GraphML')
    fluvial = ig.Graph.Read_GraphML('../networkBuilder/input/filtred/fluvial.GraphML')
    metricsLabels = ['degree', 'strength', 'betweenness', 'betweenness_w', 'closeness', 'closeness_w']
    lambdaFuncs = [lambda x:x.degree(), lambda x:x.strength(weights=x.es['weight']), lambda x:x.betweenness(), lambda x:x.betweenness(weights=x.es['weight']), lambda x:x.closeness(), lambda x:x.closeness(weights=x.es['weight'])]

    networkLabels = ['aerial', 'fluvial', 'terrestrial']
    for netIndex, g in enumerate( [aerial, fluvial, terrestrial]):
        data = {}
        for index,metric in enumerate(lambdaFuncs):
            res = sortDatasByMetrics(g, metric)
            nodes, metricValues, geocodes = zip(*res)
            data[metricsLabels[index]] = list(nodes)
            data[metricsLabels[index]+"_values"] = list(metricValues)
            data[metricsLabels[index]+"_geocde"] = list(geocodes)
        df = pd.DataFrame(data)
        df.to_csv(f"results/{networkLabels[netIndex]}/{networkLabels[netIndex]}.csv", index=False)
        
    # covidCasesDataFilter(aerial, "results/aerial/aerial")
    # covidCasesDataFilter(fluvial, "results/fluvial/fluvial")
    # covidCasesDataFilter(terrestrial, "results/terrestrial/terrestrial")





