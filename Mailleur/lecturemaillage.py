# -*- coding: utf-8 -*-
"""
Lecture mailleg FreeFem
Created on Wed Oct 29 12:00:40 2014

@author: buffat
"""
from numpy import *

F=open("ellipse.msh","r")
L=F.readline()
nn =int(L.split()[0])
ne =int(L.split()[1])
print "nb,ne=",nn,ne 
for i in range(nn):
    L=F.readline()
print L
F.close()
