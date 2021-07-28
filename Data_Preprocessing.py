import pandas as pd

dataset = pd.read_csv('Data.csv')  # creates the data frame
x = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1].values

print(x)
print(y)
