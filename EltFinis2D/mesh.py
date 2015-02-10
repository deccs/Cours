# -*- coding: utf-8 -*-
""" classe Maillage elements finis 2D avec FreeFem++ """
from numpy import *
import matplotlib.pyplot as plt
#
# classe maillage EF
#
class mesh:
    """ maillage EF 2D avec numerotation des nds a partir de 0"""
    def __init__(self):
        self.nn=0
        self.ne=0
        self.X=None
        self.Frt=None
        self.Tbc=None
        self.nom=None
    def lecture(self,filename):
        """ lecture maillage dans un fichier """
        self.nom=filename
        F=open(filename,'r');
        # lecture dimension
        L=F.readline().split()
        self.nn=int(L[0]); self.ne=int(L[1])
        self.X=zeros((self.nn,2),dtype=float);
        self.Frt=zeros((self.nn),dtype=int);
        self.Tbc=zeros((self.ne,3),dtype=int);
        # coordonnees
        for i in range(self.nn):
            L=F.readline().split()
            self.X[i,:]=[float(L[0]),float(L[1])];
            self.Frt[i]=int(L[2]);
        # table de connection
        for l in range(self.ne):
            L=F.readline().split()
            self.Tbc[l,:]=[int(L[0])-1,int(L[1])-1,int(L[2])-1]
        F.close()
        return

    def info(self):
        """ affiche information sur le maillage """
        print "Maillage ",self.nom
        print "Nn,Ne=",self.nn,self.ne
        print "Xmin/max Ymin/max=",amin(self.X[:,0]),amax(self.X[:,0]),\
                                   amin(self.X[:,1]),amax(self.X[:,1])
        # calcul surface
        surf=0.0
        for l in range(self.ne):
                surf=surf+self.aire(l)
        print "surface ",surf
        return

    def plot(self,front=True):
        """ affiche le maillage avec ou sans les points (sommets)"""
        for  l in range(self.ne):
            num=zeros((4),dtype=int)
            num[0:3]=self.Tbc[l,:]; num[3]=self.Tbc[l,0]
            plt.plot(self.X[ix_(num,[0])],self.X[ix_(num,[1])],'g-')
        plt.axis('equal')
        return

    def gradient(self,l):
        """ calcul le gradient des fonctions de forme de l'elt l et l'aire""" 
        p=zeros((5),dtype=int)
        n=self.Tbc[l,:]; # numero des sommets de 0 a nn-1
        p[0:3]=n[:]; p[3:5]=n[0:2]; # permutation circulaire
        dX=self.X[ix_(p[1:4],[0,1])]-self.X[ix_(p[2:5],[0,1])]; # aretes
        Aire=0.5*(dX[0,0]*dX[1,1]-dX[1,0]*dX[0,1]);
        dN=array([dX[:,1],-dX[:,0]])/(2*Aire);
        return dN,Aire

    def aire(self,l):
        """ calcul de l'aire de l'elemet l"""
        n=self.Tbc[l,:];
        S21=self.X[n[0],:]-self.X[n[1],:]
        S13=self.X[n[2],:]-self.X[n[0],:]
        return 0.5*(S13[0]*S21[1]-S13[1]*S21[0])
