import pandas

SalesDf = pandas.read_csv("taks1/sales.csv", sep=",")
SalesAddDf = pandas.read_csv("taks1/salesAdd.csv", sep=",")
SalesDf = SalesDf._append(SalesAddDf, ignore_index=True)
print(SalesDf)
SalesDf.to_csv("taks1/salesFiltered.csv", sep=",")
