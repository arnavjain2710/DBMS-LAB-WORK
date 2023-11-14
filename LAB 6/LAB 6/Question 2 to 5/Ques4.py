import pandas as pd
import numpy as np

df = pd.read_csv('attendance.csv')

f = open("attendance.txt", "r")
arr = []
encountered_rollnos = set()

for x in f:
    x = x.rstrip()
    rollno = int(x)
    
    if rollno not in encountered_rollnos:
        arr.append(rollno)
    else:
        arr = [x for x in arr if x != rollno]

    encountered_rollnos.add(rollno)

df["Status"] = df["RollNo"].isin(arr).astype(int)
df.to_csv('output.csv', index=False)
