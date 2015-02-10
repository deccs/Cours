#! /usr/bin/env python
# -*- coding: utf-8 -*-
from numpy import *
""" lecture maillage EF FreeFem ++ """
# canevas code python pour lire un maillage
F = open("ellipse.msh","r")
# lecture 1ere ligne
L = F.readline().split()
# extraction nbre de nds et nbre d'elements
nn = int(L[0])
ne = int(L[1])
narf= int(L[2])
print "geometrie nn,ne,narf=",nn,ne,narf
# boucle lecture des coordonnées
X=zeros((nn,2))
Frt=zeros(nn,dtype=int)
for i in range(nn):
    L=F.readline().split()
    X[i,0]=float(L[0])
    X[i,1]=float(L[1])
    Frt[i]=int(L[2])
print "Xmin/max =",amin(X[:,0]),amax(X[:,0]), \
      " Ymin/max=",amin(X[:,1]),amax(X[:,1])
# et de la table de connexion
Tbc=zeros((ne,3),dtype=int)
for k in range(ne):
    L=F.readline().split()
    for i in range(3):
        Tbc[k,i] = int(L[i])
print "Tbc ",amin(Tbc),amax(Tbc)
#
F.close()
