from os import stat
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv,statistics,random

df=pd.read_csv("StudentMark.csv")
data=df["Math_score"].tolist()

##fig=ff.create_distplot([data],["Math scores"],show_hist=False)
#fig.show()

mean=statistics.mean(data)
std=statistics.stdev(data)
print("mean",mean)
print("std",std)

def random_set_of_mean(counter):
    dataset=[]
    for i  in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_mean=random_set_of_mean(100)
    mean_list.append(set_of_mean)


std=statistics.stdev(mean_list)
mean=statistics.mean(mean_list)
print("Mean of Sampling",mean)
print("Std of Sampling",std)




fig=ff.create_distplot([mean_list],["Math scores"],show_hist=False)
fig.show()
