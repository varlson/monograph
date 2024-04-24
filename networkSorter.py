import pandas as pd
from os import makedirs 

def sortByMetric(g, lambdafuntion, label, netName, isWeighted=False):

    metricValues = []

    if(isWeighted):
        weights = [1/weight if weight > 0 else 1/0.000001 for weight in g.es['weight']]
        metricValues = lambdafuntion(g, weights)
    else:
        metricValues = lambdafuntion(g)

    nodes = [node for node in range(g.vcount())]
    geocodes = g.vs['geocode']
    zipDatas =  zip( nodes, metricValues, geocodes )
    listOfTuples = list(zipDatas)
    tupleSorted = sorted(listOfTuples, key=lambda _tuple:_tuple[1], reverse=True)

    sorted_nodes, sorted_metric_values, sorted_geocodes = zip(*tupleSorted)

    dataFrame = {}
    dataFrame['nodes'] = list(sorted_nodes)
    dataFrame['matric_values'] = list(sorted_metric_values)
    dataFrame['geocode'] = list(sorted_geocodes)
    full_path = f'results/sorted/{netName}/{label}'
    makedirs(full_path, exist_ok=True)
    pd.DataFrame(dataFrame).to_csv(f'{full_path}/{label}.csv', index=False)

    
def networkSorter( networkList, names ):
    for g_index, g in enumerate(networkList):

        metricsLabels = ["degree", "betweenness", "closeness", "strength", "betweenness_w", "closeness_w"]
        metricsLambdaFnc = [lambda g : g.degree(), lambda g : g.betweenness(),
                                lambda g : g.closeness(), lambda g, w : g.strength(weights=w),
                                lambda g, w : g.betweenness(weights=w), lambda g, w : g.closeness(weights=w)]
        
        for index, label in enumerate(metricsLabels):
            if index>= 3:
                sortByMetric(g, metricsLambdaFnc[index], label, names[g_index], True)
            else:
                sortByMetric(g, metricsLambdaFnc[index], label, names[g_index], False)

