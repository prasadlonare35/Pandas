import pandas as pd

# creating DataFrame from Dictionary
data = {
    "ID":[1001,1002,1003,1004],
    "Name": ["Prasad","Viki","Om","Raj"],
    "Age":[21,23,43,None],
    "City":["Pune","Nashik",None,"Dubai"]
}
df1 = pd.DataFrame(data)            # print like excel or sql table
print(df1)

# creating DataFrame from List of List
print("-----------------------------------")
data = [[1001,"Prasad",21,"Pune"],[1002,"Alice",25,"Goa"]]
df2 = pd.DataFrame(data,columns=["ID","Name","Age","City"])
print(df2)

# Exploring data
print("-----------------------------------")
print(df1.shape)          # rows, columns
print(df1.columns)        # list of column names
print(df1.dtypes)         # data type of each column
print(df1.info())         # summary of dataset
print(df1.describe())     # statitics for numerical columns

# Selecting and filtering
print("-----------------------------------")
print(df1["Name"])      # selecting 1 column
print(df1[["Name","Age"]])      # selecting 2 column
print("-----------------------------------")
print(df1.iloc[1])      # selecting 2nd row
print(df1.loc[0])      # selecting 1st row
print("-----------------------------------")
print(df1[df1["Age"]>25])          # filtering
print(df1[df1["City"]=="Pune"])    # filtering

# Modifying DataFrames
print("-----------------------------------")
df1["Salary"]=[50000,30000,30200,2323]    # adding column
print(df1)
print("-----------------------------------")
df1["Age"]=df1["Age"]+1              # updating column
print(df1)
print("-----------------------------------")
df1.drop("Salary",axis=1,inplace=True)    # deleting column
print(df1)

# Handling Missing Data
print("-----------------------------------")
print(df1.isnull().sum())         # check missing value
print("-----------------------------------")
df1.fillna({"City":"Pune"},inplace=True)    # filling missing value
print(df1) 
print("-----------------------------------")
df1.dropna(inplace=True)          # drop row with missing value
print(df1)

# Sorting and Grouping
print("-----------------------------------")
df1.sort_values("Age",ascending=False,inplace=True)
print(df1)
print(df1.groupby("City")["Age"].mean())

# Merging 2 Df
print("-----------------------------------")
mdf = pd.merge(df1,df2,on="ID")
print(mdf)

# Joining DF
print("-----------------------------------")
edf1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

edf2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'City': ['New York', 'Los Angeles', 'Pune'],
    'Country': ['USA', 'USA', 'India']
})
edf1.set_index('ID', inplace=True)
edf2.set_index('ID', inplace=True)

print(edf1.join(edf2))

# working with TimeSeries Data
print("-----------------------------------")
data = {
    'Date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
    'Age': [25, 30, 35, 40, 45]
}
sdf1 = pd.DataFrame(data)

sdf1['Date'] = pd.to_datetime(sdf1['Date'])  # Convert 'Date' column to datetime format
print(sdf1)
sdf1.set_index("Date", inplace=True)         # Set 'Date' column as the index
resampled_df = sdf1.resample("ME").mean()     # Resample the data by month and compute the mean
print(resampled_df)

