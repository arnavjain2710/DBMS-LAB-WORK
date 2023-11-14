import pandas as pd
import numpy as np

df = pd.read_csv('attendance.csv')

f = open("attendance.txt", "r")
arr = []
for x in f:
    x = x.rstrip()
    arr.append(int(x))

df["Status"] = df["RollNo"].isin(arr).astype(int)

df.to_csv('output.csv', index=False)
