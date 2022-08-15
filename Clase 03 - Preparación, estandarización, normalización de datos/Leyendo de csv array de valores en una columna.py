import os
os.system("clear")

import pandas as pd
import json

df = pd.read_csv("test.csv")

print(df)
print("\n")
print(type(df["def"][0]))
print("\n")

def desjsonear(x) :
    return json.loads(x)

df["def"] = df["def"].apply(desjsonear)

print(df)
print("\n")
print(type(df["def"][0]))
print(type(df["def"][0][2]))
