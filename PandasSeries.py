import pandas as pd

data = [1,2,3,4]
series = pd.Series(data)       # print with default index 0,1,2...
print(series)          

# custom index series
series = pd.Series([1,2,3,4],index=['A','B','C','D'])
print(series)