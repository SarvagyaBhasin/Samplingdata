import pandas as pd
import csv 
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import random 

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()

populationmean=statistics.mean(data)
populationsd=statistics.stdev(data)
print("population mean: ", populationmean)
print("population standard deviation: ", populationsd)
def randomsetofmean(counter):
    dataset=[]
    for i in range(0, counter):
        ri=random.randint(0, len(data)-1)
        dataset.append(data[ri])
    mean=statistics.mean(dataset)
    return mean

def showgraph(meanlist):
    df=meanlist
    mean=statistics.mean(df)
    graph=ff.create_distplot([df], ["reading_time"], show_hist=False)
    graph.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="mean"))
    graph.show()

meanlist=[]
for i in range(0, 1000):
    setofmeans=randomsetofmean(100)
    meanlist.append(setofmeans)
showgraph(meanlist)
mean=statistics.mean(meanlist)
print("Mean of sampling distribution: ", mean)
sd=statistics.stdev(meanlist)
print("standard deviation: ", sd)