""" courbe efficacite a la main
    (C) Marc BUFFAT 2014
"""
from numpy import *
import matplotlib.pyplot as plt
def fact(N):
    PROD=zeros(len(N))
    for k,n in enumerate(N):
        prod=1
        for i in range(1,n+1):
            prod = prod*i
        PROD[k]=prod
    return PROD

with plt.xkcd():
    plt.figure(figsize=(8,6))
    n=100
    N = arange(1,n)
    N1 = arange(1,8)
    FN1 = 50+0.2*fact(N1)
    ax = plt.axes()
    ax.axis([0.,n,0.,200.])
    ax.plot(N, N, 'b', lw=2, label='$O(n)$')
    a1=2./n**2
    ax.plot(N, a1*N**3, 'r', lw=2, label='$O(n^3)$')
    ax.plot(5*N1, FN1, 'g', lw=2, label='$O(n!n^2)$')

    ax.set_title('efficacite')
    ax.set_xlabel('taille du probleme n')
    ax.set_ylabel('temps cpu')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.legend(loc=1,fontsize=18)
    plt.draw()
    plt.show()
#plt.savefig("coutN.png")
