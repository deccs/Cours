#! /usr/bin/env python
# -*- coding: utf-8 -*-
""" resolution laplacien  """
from numpy import *
from scipy.sparse import coo_matrix,csr_matrix
from scipy.sparse.linalg import dsolve,splu
from scipy.linalg import lu
import matplotlib.pyplot as plt
import matplotlib.tri as tri

from freefem import mesh

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
    """ assemblage matrice dense """
    K=zeros((G.nn,G.nn))
    for k in range(G.ne):
        Ke=MatRigidite(G,k)
        ni=G.Tbc[k,:]
        K[ix_(ni,ni)] += Ke
    return K

def AssemblageSp(G):
    """ assemblage matrice creuse """
    N=G.ne*3**2  # estimation dimension ne*ddl**2
    data=zeros(N)
    row=zeros(N,dtype=int)
    col=zeros(N,dtype=int)
    nz=0
    for k in range(G.ne):
        ni=G.Tbc[k,:]
        num=array([ni,ni,ni],dtype=int)
        Ke=MatRigidite(G,k)
        # conditions limites
        code=G.Frt[ix_(ni)]
        for k in nonzero(code)[0]:
            Ke[k,:]=0.0
            Ke[:,k]=0.0
            Ke[k,k]=1.0
        data[nz:nz+9]=Ke.reshape(9)
        row[nz:nz+9]=num.transpose().reshape(9)
        col[nz:nz+9]=num.reshape(9)
        nz=nz+9
    return data,row,col
#
def Smb(G,F):
    """ second membre """
    B=zeros((G.nn))
    for k in range(G.ne):
        Me=MatMasse(G,k)
        ni=G.Tbc[k,:]
        Fe=F[ix_(ni)]
        B[ix_(ni)] += dot(Me,Fe)
    return B

def Permutation(permc,permr):
    """calcul les matrices de permutations"""
    N=size(permc)
    Pc=zeros((N,N))
    Pr=zeros((N,N))
    for i in range(N):
        Pc[i,permc[i]]=1.0
        Pr[permr[i],i]=1.0
    return Pc,Pr
# lecture maillage
G=mesh("ellipse.msh")
G=G.raffin()
G=G.raffin()
G.info()
# assemblage
print "Resolution Laplacien matrice dense"
F=ones(G.nn)
A=Assemblage(G)
print "Matrice A",A.shape,A.size
B=Smb(G,F)
# conditions limites
for i in range(G.nn):
    if G.Frt[i]==1:
        A[i,:]=0.; A[:,i]=0.; A[i,i]=1.0;
        B[i]=0.0
# resolution
U=linalg.solve(A,B)
print "solution min/max=",amin(U),amax(U)
#
print "Resolution Laplacien matrice creuse"
data,row,col=AssemblageSp(G)
Ac=coo_matrix((data,(row,col)),shape=(G.nn,G.nn))
print "Matrice Ac ",Ac.shape,Ac.nnz
# conversion format compresse
Ar=Ac.tocsr()
print "Matrice Ar ",Ar.shape,Ar.nnz
# resolution
Ur=dsolve.spsolve(Ar,B,use_umfpack=True,permc_spec="MMD_ATA")
print "solution min/max=",amin(Ur),amax(Ur)

# tracer
if (True):
    plt.figure(1,figsize=(12,6))
    plt.subplot(1,2,1)
    plt.axis('equal')
    plt.spy(A,markersize=3)
    plt.title("A dim=%d non-zero=%d"%(size(A),count_nonzero(A)),fontsize=16)
    plt.subplot(1,2,2)
    plt.axis('equal')
    PL,U=lu(A,permute_l=True)
    PLU=PL+U
    plt.spy(PLU,markersize=3)
    plt.title("LU dim=%d non-zero=%d"%(size(PLU),count_nonzero(PLU)),fontsize=16)
    plt.draw()
    plt.savefig("matrixEF1.png")
    # 
    plt.figure(2,figsize=(12,6))
    plt.subplot(1,2,1)
    plt.axis('equal')
    As=Ar.tocsc()
    LUs=splu(As,permc_spec="MMD_ATA")
    #LUs=splu(As,permc_spec="NATURAL")
    Pc,Pr=Permutation(LUs.perm_c,LUs.perm_r)
    A2=dot(Pr,dot(A,Pc))
    plt.spy(A2,markersize=3)
    plt.title("A dim=%d non-zero=%d"%(size(A2),count_nonzero(A2)),fontsize=16)
    plt.subplot(1,2,2)
    plt.axis('equal')
    PL2,U2=lu(A2,permute_l=True)
    PLU2=PL2+U2
    plt.spy(PLU2,markersize=3)
    plt.title("LU dim=%d non-zero=%d"%(size(PLU2),count_nonzero(PLU2)),fontsize=16)
    plt.draw()
    plt.savefig("matrixEF2.png")
    plt.show()
#
