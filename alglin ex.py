import numpy as np
import scipy.integrate as integr
import matplotlib.pyplot as plt

def euler(n):
    def f(x):
        return 1
    T=[f]
    for i in range(n+1):
        def E(x):
            return (i+1)*(integr.quad(T[-1],0,x)[0])-(i+1/2)*(integr.quad(T[-1],0,1)[0])  
        T.append(E)
    return T
T=euler(9)
for j in range (10):
    print(T[j](0))
