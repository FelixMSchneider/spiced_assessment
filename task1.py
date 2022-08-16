import numpy as np


f=open("./datapoints.csv")

A=f.readlines()

X=np.array([float(a.split(",")[0]) for a in A[1:]])
Y=np.array([float(a.split(",")[1]) for a in A[1:]])
print(X)
print(Y)

