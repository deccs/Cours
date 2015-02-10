#! /usr/bin/env python
from math import log

def serie(x,n):
    """ calcul de la somme de n termes de la serie x-x^2/2+x^3/3- """
    coef=x
    somme=0.0
    for i in range(1,n+1):
        somme = somme + coef/i
        coef  = -coef*x
    return somme
#
x=0.2
n=20
print "Calcul de la serie pour x=",x," et n=",n
print "somme    = ",serie(x,n)
print "log(1+x) = ", log(1+x)
