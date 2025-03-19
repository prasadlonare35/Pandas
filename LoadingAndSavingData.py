import pandas as pd

# Loading Data
df = pd.read_csv("sample_data.csv")

# Adding new Column
df["Name"]=["Bob","alice","John","Rowan","Mike"]
print(df.head())

# saving Data
df.to_csv("Output.csv",index=False)