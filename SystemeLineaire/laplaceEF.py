#! /usr/bin/env python
# -*- coding: utf-8 -*-
""" resolution laplacien  """
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.tri as tri

from mesh import mesh

def MatRigidite(G,k):
    """ calcul matrice de rigidite sur l'elt k du maillage G """
    dN,Aire=G.gradient(k)
    K22=dot(dN[:,1],dN[:,1])*Aire
    K33=dot(dN[:,2],dN[:,2])*Aire
    K23=dot(dN[:,1],dN[:,2])*Aire
    Ke=array([[K22+K33+2*K23, -K23-K22,-K23-K33],
              [-K23-K22     , K22     , K23],
              [-K23-K33     , K23     , K33]])
    return Ke

def MatMasse(G,k):
    """ calcul matrice de masse sur l'elt k du maillage G """
    Aire=G.aire(k)
    Me=Aire/12.0*array([[ 2, 1 ,1 ],
                        [ 1, 2 ,1 ],
                        [ 1, 1 ,2 ]])
    return Me

def Assemblage(G):
    K=zeros((G.nn,G.nn))
    for k in range(G.ne):
        Ke=MatRigidite(G,k)
        ni=G.Tbc[k,:]
        K[ix_(ni,ni)] += Ke
    return K
def Smb(G,F):
    B=zeros((G.nn))
    for k in range(G.ne):
        Me=MatMasse(G,k)
        ni=G.Tbc[k,:]
        Fe=F[ix_(ni)]
        B[ix_(ni)] += dot(Me,Fe)
    return B
# tracer champ Z sur maillage
def isosurf(G,Z,titre):
    """ trace isosurface de Z sur le maillage G"""
    triang=tri.Triangulation(G.X[:,0],G.X[:,1],triangles=G.Tbc)
    plt.tricontourf(triang, Z)
    plt.colorbar()
    plt.title(titre)
    return

#
def laplaceEF(meshname):
    G=mesh()
    G.lecture(meshname)
    G.info()
    # assemblage
    print "Resolution Laplacien EF "
    F=ones(G.nn)
    A=Assemblage(G)
    B=Smb(G,F)
    # conditions limites
    for i in range(G.nn):
        if G.Frt[i]==1:
            A[i,:]=0.; A[:,i]=0.; A[i,i]=1.0;
            B[i]=0.0
    return A,B,G
