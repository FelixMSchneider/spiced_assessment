import numpy as np
import pylab as plt

f=open("./datapoints.csv")

A=f.readlines()

X=np.array([float(a.split(",")[0]) for a in A[1:]])
Y=np.array([float(a.split(",")[1]) for a in A[1:]])




plt.scatter(X,Y)
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("task2.png")

plt.show()
