import csv
import pandas as pd
import plotly.express as px

with open("class1.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
total_mark=0
total_entries=len(file_data)

for marks in file_data:
    total_mark += float(marks[1])


mean=total_mark/total_entries
print("Mean (Average):", mean )

df=pd.read_csv("class1.csv")
fig=px.scatter(df,x="Student Number",y="Marks")
fig.show()

