import numpy as np
import pylab as plt


def func(x,a,b):
    return a*x+b

f=open("./datapoints.csv")

A=f.readlines()

X=np.array([float(a.split(",")[0]) for a in A[1:]])
Ytrue=np.array([float(a.split(",")[1]) for a in A[1:]])

Ynew=func(X,10,0)


plt.scatter(X,Ytrue)
plt.scatter(X,Ynew)


MSE=1/len(Ytrue)*np.sum((Ytrue-Ynew)**2)

print("The rsulting MSE value for task4 is", MSE)

