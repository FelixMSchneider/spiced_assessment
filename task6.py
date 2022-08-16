import numpy as np
import pylab as plt


def func(x,a,b):
    return a*x+b

f=open("./datapoints.csv")

A=f.readlines()

X=np.array([float(a.split(",")[0]) for a in A[1:]])
Ytrue=np.array([float(a.split(",")[1]) for a in A[1:]])



b=-3

for j in range(61):

    a=10
    for i in range(100):
        
    
        Ynew=func(X,a,b)
    
        MSEnew=1/len(Ytrue)*np.sum((Ytrue-Ynew)**2)
    
        if i==0 and j==0:
            MSE=MSEnew
            aopt=a
        else:
            if MSEnew<MSE: 
                MSE=MSEnew
                aopt=a
                bopt=b
    
        a-=0.1

    b+=0.1    

print("a_opt, b_opt and the corresponding MSE are ", round(aopt,1),round(bopt,1) ,MSE)


plt.scatter(X,Ytrue)
plt.plot(X,func(X,aopt,bopt))
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("task6.png")
plt.show()
