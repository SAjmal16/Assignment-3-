import pandas as pd 

# df = pd.read_excel("results2024-11-25-144.xlsx")

df = pd.read_excel("group_results - Copy.xlsx")

df = df.drop("Entry", axis=1)
df = df.drop("Fastest Download", axis=1)
df = df.drop("Slowest Download", axis=1)
df = df.drop("Fastest Upload", axis=1)
df = df.drop("Slowest Upload", axis=1)
print(df.describe())

