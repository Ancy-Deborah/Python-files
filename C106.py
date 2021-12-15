import csv
import numpy as np
import plotly.express as px

def getDataSource(datapath):
    icecream_sales=[]
    cold_drinksales=[]
    with open("icecream.csv") as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            icecream_sales.append(float(row["Temperature"]))
            cold_drinksales.append(float(row["Ice-creamSales"]))
    return {"x":icecream_sales,"y":cold_drinksales}

def findCorr(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between ice cream sales vs temperature",correlation[0,1])

def setup():
    datapath="icecream.csv"
    datasource=getDataSource(datapath)
    findCorr(datasource)

setup()




