import igraph as ig
from util import covidCasesDataFilter,graphDataSorter
from networkMerger import networkMerger
import pandas as pd
from networkSorter import networkSorter
from correspondeceCalculator import correspondenceCalculator
from os import makedirs
from plotter import plot
import numpy as np

def covidCasesDataFilterDiver():

    aerial = ig.Graph.Read_GraphML('datas/graphs/aerial.GraphML')
    terrestrial = ig.Graph.Read_GraphML('datas/graphs/terrestrial.GraphML')
    fluvial = ig.Graph.Read_GraphML('datas/graphs/fluvial.GraphML')
    
    covidCasesDataFilter(aerial,"results/filtred/aerial")
    covidCasesDataFilter(terrestrial,"results/filtred/terrestrial")
    covidCasesDataFilter(fluvial,"results/filtred/fluvial")

def networkMergerDriver():

    aerialNet = ig.Graph.Read_GraphML('datas/aerial.GraphML')
    fluvialNet = ig.Graph.Read_GraphML('datas/fluvial.GraphML')
    terrestrialNet = ig.Graph.Read_GraphML('datas/terrestrial.GraphML')

    G = networkMerger([terrestrialNet, aerialNet, fluvialNet])
    _min, _max = min(G.degree()), max(G.degree())
    sizes = [ ((deg - _min)/(_max-_min))*8+10 for deg in G.degree() ]
    G.vs['size'] = sizes
    G.es['width'] = 0.39
    G.write_graphml('input/filtred/merged.GraphML')
    ig.summary(G)


def graphSorterDriver():
    aerialNet = ig.Graph.Read_GraphML('datas/graphs/aerial.GraphML')
    fluvialNet = ig.Graph.Read_GraphML('datas/graphs/fluvial.GraphML')
    terrestrialNet = ig.Graph.Read_GraphML('datas/graphs/terrestrial.GraphML')
    merged = ig.Graph.Read_GraphML('datas/graphs/merged.GraphML')

    networkSorter([aerialNet, fluvialNet, terrestrialNet,merged], ['aerial', 'fluvial', 'terrestrial', 'merged'])




def mobDataSorterDriver():
    covidDataFrame = pd.read_csv('datas/all.csv')
    
    aerial = ig.Graph.Read_GraphML('datas/filtred/aerial.GraphML')
    graphDataSorter(aerial, covidDataFrame,'aerial')

    fluvial = ig.Graph.Read_GraphML('datas/filtred/fluvial.GraphML')
    graphDataSorter(fluvial, covidDataFrame,'fluvial')

    terrestrial = ig.Graph.Read_GraphML('datas/filtred/terrestrial.GraphML')
    graphDataSorter(terrestrial, covidDataFrame,'terrestrial')


def intersectionCalculatorDriver():
    
    metrics = ["degree", "strength", "betweenness", "betweenness_w", "closeness", "closeness_w"]
    
    # AERIAL DATAS
    aerialIntersectionResults = {}
    aerialCovid = pd.read_csv('results/filtred/aerial_filtred_covid_cases_data.csv')
    
    for metric in metrics:
        data = pd.read_csv(f'results/sorted/aerial/{metric}/{metric}.csv')
        resul = correspondenceCalculator(list(data['geocode']), list(aerialCovid['geocode']))
        aerialIntersectionResults[metric] = resul
    
    aerialIntersectionResults['cities'] = aerialCovid['cities']
    aerialIntersectionResults['dates'] = aerialCovid['dates']

    fullpath = f'results/intersections/aerial'
    makedirs(fullpath, exist_ok=True)
    pd.DataFrame(aerialIntersectionResults).to_csv(f'{fullpath}/aerial.csv', index=False)



    # FLUVIAL DATAS
    fluvialIntersectionResults = {}
    fluvialCovid = pd.read_csv('results/filtred/fluvial_filtred_covid_cases_data.csv')
    
    for metric in metrics:
        data = pd.read_csv(f'results/sorted/fluvial/{metric}/{metric}.csv')
        resul = correspondenceCalculator(list(data['geocode']), list(fluvialCovid['geocode']))
        fluvialIntersectionResults[metric] = resul
    
    fluvialIntersectionResults['cities'] = fluvialCovid['cities']
    fluvialIntersectionResults['dates'] = fluvialCovid['dates']

    fullpath = f'results/intersections/fluvial'
    makedirs(fullpath, exist_ok=True)
    pd.DataFrame(fluvialIntersectionResults).to_csv(f'{fullpath}/fluvial.csv', index=False)




    # TERRESTRIAL DATAS
    terrestrialIntersectionResults = {}
    terrestrialCovid = pd.read_csv('results/filtred/terrestrial_filtred_covid_cases_data.csv')
    
    for metric in metrics:
        data = pd.read_csv(f'results/sorted/terrestrial/{metric}/{metric}.csv')
        resul = correspondenceCalculator(list(data['geocode']), list(terrestrialCovid['geocode']))
        terrestrialIntersectionResults[metric] = resul
    
    terrestrialIntersectionResults['cities'] = terrestrialCovid['cities']
    terrestrialIntersectionResults['dates'] = terrestrialCovid['dates']

    fullpath = f'results/intersections/terrestrial'
    makedirs(fullpath, exist_ok=True)
    pd.DataFrame(terrestrialIntersectionResults).to_csv(f'{fullpath}/terrestrial.csv', index=False)



def plotDriver():

    lbls = [r'$k$', r'$s$', r'$b$', r'$b_w$', r'$c$', r'$c_w$', ]
    metrics = ["degree", "strength", "betweenness", "betweenness_w", "closeness", "closeness_w"]


    # AERIAL NETWORK PLOT 
    # aerial = pd.read_csv('results/intersections/aerial/aerial.csv')
    # x_axis = aerial['dates']
    # y_axis =[]

    # for metric in metrics:
    #     y_axis.append(aerial[metric])
    

    # labels=[]
    # for index, metric_item in enumerate(lbls):
    #     average_rate = np.mean(list(aerial[metrics[index]]))
    #     sd_symbol = r'$\sigma$ = '
    #     mean_symbol = r'$\bar{x}$ = '
    #     sd = np.std(list(aerial[metrics[index]]))
    #     sd = ' %.2f' % sd
    #     label =  metric_item + ' (' + mean_symbol + ' %.2f' % average_rate + ' , ' + sd_symbol + str(sd) + ')' 
    #     labels.append(label)
    # y_axis.append(list(aerial[metrics[index]]))

    # plot(x_axis, y_axis, labels, 'results/plots/aerial', 'aerial', 'Rede de mobilidade aérea')


    # FLUVIAL NETWORK PLOT 

    fluvial = pd.read_csv('results/intersections/fluvial/fluvial.csv')
    x_axis = fluvial['dates']
    y_axis =[]

    for metric in metrics:
        y_axis.append(fluvial[metric])
    

    labels=[]
    for index, metric_item in enumerate(lbls):
        average_rate = np.mean(list(fluvial[metrics[index]]))
        sd_symbol = r'$\sigma$ = '
        mean_symbol = r'$\bar{x}$ = '
        sd = np.std(list(fluvial[metrics[index]]))
        sd = ' %.2f' % sd
        label =  metric_item + ' (' + mean_symbol + ' %.2f' % average_rate + ' , ' + sd_symbol + str(sd) + ')' 
        labels.append(label)
    y_axis.append(list(fluvial[metrics[index]]))

    plot(x_axis, y_axis, labels, 'results/plots/fluvial', 'fluvial', 'Rede de mobilidade fluvial')


    # TERRESTRIAL NETWORK PLOT 

    # terrestrial = pd.read_csv('results/intersections/terrestrial/terrestrial.csv')
    # x_axis = terrestrial['dates']
    # y_axis =[]

    # for metric in metrics:
    #     y_axis.append(terrestrial[metric])
    

    # labels=[]
    # for index, metric_item in enumerate(lbls):
    #     average_rate = np.mean(list(terrestrial[metrics[index]]))
    #     sd_symbol = r'$\sigma$ = '
    #     mean_symbol = r'$\bar{x}$ = '
    #     sd = np.std(list(terrestrial[metrics[index]]))
    #     sd = ' %.2f' % sd
    #     label =  metric_item + ' (' + mean_symbol + ' %.2f' % average_rate + ' , ' + sd_symbol + str(sd) + ')' 
    #     labels.append(label)
    # y_axis.append(list(terrestrial[metrics[index]]))

    # plot(x_axis, y_axis, labels, 'results/plots/terrestrial', 'terrestrial', 'Rede de mobilidade terrestre')




    # MULTIMODAL NETWORK PLOT 

    # merged = pd.read_csv('results/intersections/merged/merged.csv')
    # x_axis = merged['dates']
    # y_axis =[]

    # for metric in metrics:
    #     y_axis.append(merged[metric])
    

    # labels=[]
    # for index, metric_item in enumerate(lbls):
    #     average_rate = np.mean(list(merged[metrics[index]]))
    #     sd_symbol = r'$\sigma$ = '
    #     mean_symbol = r'$\bar{x}$ = '
    #     sd = np.std(list(merged[metrics[index]]))
    #     sd = ' %.2f' % sd
    #     label =  metric_item + ' (' + mean_symbol + ' %.2f' % average_rate + ' , ' + sd_symbol + str(sd) + ')' 
    #     labels.append(label)
    # y_axis.append(list(merged[metrics[index]]))

    # plot(x_axis, y_axis, labels, 'results/plots/merged', 'merged', 'Rede de mobilidade multimodal')


   

def main():

    # Filtrar dados, pegando só os existentes na rede de mobilidade
    # covidCasesDataFilterDiver()
    
    # Fazer merge das redes
    # networkMergerDriver()

    # Criar e ordenar dados com base nas metricas
    # graphSorterDriver()


    # Calcular correspondecia e salvá-las
    # intersectionCalculatorDriver()

    # Criar plots  

    plotDriver()

main()