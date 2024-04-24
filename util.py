import pandas as pd
import os

def covidCasesDataFilter(graph, outputName):
    df = pd.read_csv('datas/cases-brazil-cities-time.csv')

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
    geocodes, cities, dates = zip(*_tuples)


    dict_res ={}
    dict_res['geocode'] = list(geocodes) 
    dict_res['cities'] =  list(cities)
    dict_res['dates'] =  list(dates)

    df_res = pd.DataFrame(dict_res)
    # print(df_res)

    df_res.to_csv(f'{outputName}_filtred_covid_cases_data.csv', index=False)


def graphDataSorter(graph, covidData, name):
    
    intersec = []
    geocodes = list(covidData['geocode'])
    dates = list(covidData['date'])
    cities = list(covidData['city'])

    for index, geo in  enumerate(geocodes):
        if geo in graph.vs['geocode']:
            intersec.append((geo, cities[index], dates[index]))

    all_geo, all_cities, all_dates = zip(*intersec)

    df = {}
    df['geocode'] = list(all_geo)
    df['cities'] = list(all_cities)
    df['dates'] = list(all_dates)
    pd.DataFrame(df).to_csv(f'results/{name}/filtred_{name}.csv')
