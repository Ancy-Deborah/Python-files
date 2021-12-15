import csv
from collections import Counter

with open('height-weight.csv',newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
#print(file_data)

new_data="whitehatjr"
data=Counter(new_data)
print(data)

new_list=data.items()
print(new_list)

value=data.values()
print(value)