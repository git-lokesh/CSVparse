import pandas as p

d1 = p.read_csv("learn.csv")
d2 = p.read_csv("data.csv")
# print("BASIC INFO : ")
print(d2.info())
# print("DESCRIBE  :")
print(d2['Annual_Income_(k$)'].mean())
print(d2.isnull().sum())