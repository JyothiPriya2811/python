import pandas as pd
data= pd.read_csv("C://Users/RK/Downloads/matches.csv")
print(data.head())
print(data.tail())
print(data.head(19))
print(data[200:240])
print(data.tail(10))
print(data[:45])
print(data.tail(90))
print(data.columns)
print(data[data['Season']==2008].shape[0])
print(data[data['City']=="Bangalore"])
print(data[data['Season']==2008])
print(data[data["Winner"]=="Chennai Super Kings"])
