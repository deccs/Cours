#! /usr/bin/env python
""" principe methode de Newton
    (C) Marc Buffat 2014
"""
from numpy import *
import matplotlib.pyplot as plt
def F(x):
    """ fonction dont on cherche la racine"""
    return x**6-(1.6)**6
def dF(x):
    """ dérivée de F(x) """
    return 6*x**5
def G(x):
    """ fonction intérative de Newton"""
    return x - F(x)/dF(x)
#
xs=1.6
x0=2.
x1=G(x0)
dF0=dF
xmin=0.8
xmax=2.1
ymin=-10
ymax=80
#print x0,x1,x2,x3
#
random.seed(0)
plt.xkcd(scale=1.2,length=100,randomness=2)
ax = plt.axes()
X=linspace(xmin,xmax,50)
ax.plot(X,F(X),'-',linewidth=3,label="y=f(x)")
ax.axhline(y=0,color='r',linewidth=2)
ax.plot([x0,x1],[F(x0),0.],'--',lw=2)

ax.plot([x0],[F(x0)],'^',color='b',markersize=10)
ax.plot([x1],[F(x1)],'^',color='g',markersize=10)
ax.plot([xs],[F(xs)],'^',color='black',markersize=10)
ax.plot([x0,x0],[ymin,F(x0)],'-',color='black')
ax.plot([x1,x1],[ymin,F(x1)],'-',color='black')
ax.plot([x0,xmin],[F(x0),F(x0)],'-',color='black')
ax.plot([x1,xmin],[F(x1),F(x1)],'-',color='black')
ax.legend(loc=0,fontsize=20)
ax.axis([xmin,xmax,ymin,ymax])
plt.title("methode de Newton",fontsize=32)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticks([xs,x1,x0])
ax.set_xticklabels(["x*","xn+1","xn"],fontsize=20)
ax.set_yticks([0.,F(x1),F(x0)])
ax.set_yticklabels(["0","f(xn+1)","f(xn)"],fontsize=20)
ax.tick_params(top='off',right='off')
plt.savefig("newton.png",transparent=True)
plt.show()
