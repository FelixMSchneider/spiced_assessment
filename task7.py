import numpy as np
import pylab as plt


#
#
# here I improve the alorithm by using mathematical formulars (not given functions) 
# for linear regression
#
#


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


# optimize by using formuars for linear regression:


XX=X-np.mean(X)
YY=Ytrue-np.mean(Ytrue)

slope=sum(XX*YY)/sum(XX**2)
Y0=np.mean(Ytrue)-slope*np.mean(X)

print("the slope and Y0 values from linear regression formulars are", Y0, slope)

plt.scatter(X,Ytrue)
plt.plot(X,func(X,aopt,bopt), label="iterative linear regression")
plt.plot(X,func(X,slope,Y0), label="optimized")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")

plt.savefig("task7.png")
plt.show()
