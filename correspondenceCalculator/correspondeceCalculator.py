import pandas as pd

def intersectionCalculator(size, netData, covidData):
    intersect = (set(netData) & set(covidData))
    correspondence = float(len(intersect)) / float(size)
    return correspondence

def correspondenceCalculator(networkData, covidCaseDataFrame):
    correspondeceSequence = []
    for index in range(len(covidCaseDataFrame)):
        corresp = intersectionCalculator(index+1, networkData[:index+1], covidCaseDataFrame[:index+1])
        correspondeceSequence.append(corresp)
    # print(correspondeceSequence)

    return correspondeceSequence



def correspondenceCalculatorDriver():
    metrics = ["degree", "strength", "betweenness", "betweenness_w", "closeness", "closeness_w"]

    # aerial datas
    aerialNet = pd.read_csv('../dataExtractor/results/aerial/aerial.csv')
    aerialCovid = pd.read_csv('../dataExtractor/results/aerial/aerial_filtred_covid_cases_data.csv')


    # fluvial datas
    fluvialNet = pd.read_csv('../dataExtractor/results/fluvial/fluvial.csv')
    fluvialCovid = pd.read_csv('../dataExtractor/results/fluvial/fluvial_filtred_covid_cases_data.csv')

    # terrestrial datas
    terrestrialNet = pd.read_csv('../dataExtractor/results/terrestrial/terrestrial.csv')
    terrestrialCovid = pd.read_csv('../dataExtractor/results/terrestrial/terrestrial_filtred_covid_cases_data.csv')


    datas = {}
    for metr in metrics:
        res = correspondenceCalculator(list(terrestrialNet[f'{metr}_geocde']), list(terrestrialCovid['geocode']))
        datas[metr] = res
    
    df = pd.DataFrame(datas)
    df.to_csv('results/terrestrial/terrestrial.csv', index=False)

    del datas
    datas = {}
    for metr in metrics:
        res = correspondenceCalculator(list(aerialNet[f'{metr}_geocde']), list(aerialCovid['geocode']))
        datas[metr] = res
    
    df = pd.DataFrame(datas)
    df.to_csv('results/aerial/aerial.csv', index=False)

    del datas
    datas = {}
    for metr in metrics:
        res = correspondenceCalculator(list(fluvialNet[f'{metr}_geocde']), list(fluvialCovid['geocode']))
        datas[metr] = res
    
    df = pd.DataFrame(datas)
    df.to_csv('results/fluvial/fluvial.csv', index=False)


if __name__ == "__main__":
    correspondenceCalculatorDriver()