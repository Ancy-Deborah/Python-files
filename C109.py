import random
import statistics
import plotly.figure_factory as ff

dice_result=[]

for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)

mean=sum(dice_result)/len(dice_result)
std = statistics.stdev(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
print("Mean of the dice",mean)
print("Median of the dice",median)
print("Mode of the dice",mode)
print("std of the dice",std)

fig=ff.create_distplot([dice_result],["Result"])
fig.show()

