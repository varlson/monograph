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

    return correspondeceSequence






if __name__ == "__main__":
    correspondenceCalculatorDriver()