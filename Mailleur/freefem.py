# -*- coding: utf-8 -*-
""" classe Maillage elements finis 2D avec FreeFem++ """
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import subprocess
#
# classe maillage EF
#
class mesh:
    """ maillage EF 2D avec numerotation des nds a partir de 0"""
    nn=0
    ne=0
    X=None
    Frt=None
    Tbc=None
    nom=None
    # lecture du maillage
    def __init__(self,filename=None):
        """ lecture maillage dans un fichier """
        if filename==None: return
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
        print "Xmin/max Ymin/max=",amin(self.X[:,0]),amax(self.X[:,0]),amin(self.X[:,1]),amax(self.X[:,1])
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
        if front:
            COL=('k','b', 'g', 'r', 'c', 'm', 'y')
            ARF=self.arfront()
            for L in ARF:
                plt.plot(self.X[L,0],self.X[L,1],lw=2,color='k')
                code=self.Frt[L[0]]
                col="#777700"
                if code<7: col=COL[code]
                plt.plot(self.X[L[0],0],self.X[L[0],1],'o',color=col)
                code=self.Frt[L[1]]
                col="#777700"
                if code<7: col=COL[code]
                plt.plot(self.X[L[1],0],self.X[L[1],1],'o',color=col)
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

    def aretes(self):
        """ liste des aretes du maillage """
        # liste des aretes (en double)
        LA=vstack((self.Tbc[:,0:2],self.Tbc[:,1:],transpose(vstack((self.Tbc[:,2],self.Tbc[:,0])))))
        LA=sort(LA)
        # elimination des doubles par conversion en chaine des lignes
        # puis utilisation de unique et conversion en entier
        dim=LA.itemsize
        AR=unique(LA.view('S%d'%(2*dim))).view ('i%d'%dim)
        return AR.reshape((len(AR)/2, 2))

    def arfront(self):
        """ liste des aretes frontieres """
        # liste des artes (en double)
        LA=vstack((self.Tbc[:,0:2],self.Tbc[:,1:],transpose(vstack((self.Tbc[:,2],self.Tbc[:,0])))))
        LA=sort(LA)
        dim=LA.itemsize
        AR=unique(LA.view('S%d'%(2*dim))).view ('i%d'%dim)
        AR=AR.reshape((len(AR)/2, 2))
        # boucle sur les aretes de G
        narf=0
        for L in AR:
           if self.Frt[L[0]]!=0 and self.Frt[L[1]]!=0 :
                # verification si arete frontiere
                I1=where(LA[:,0]==L[0])[0]
                I2=where(LA[ix_(I1)]==L[1])[1]
                if len(I2)==1:
                        AR[narf,:]=L
                        narf+=1
        return AR[:narf,:]
        # tracer du champ Z sur le maillage G
    def isosurf(self,Z,titre,front=True):
        """ trace isosurface de Z sur le maillage """
        triang=tri.Triangulation(self.X[:,0],self.X[:,1],triangles=self.Tbc)
        plt.tricontourf(triang, Z)
        if front:
            ARF=self.arfront()
            for L in ARF:
                plt.plot(self.X[L,0],self.X[L,1],lw=2,color='k')
        plt.colorbar()
        plt.title(titre)
        return
    # raffinement maillage
    def raffin(self):
        """raffinement maillage"""
        AR=self.aretes()
        nar=AR.shape[0]
        G2=mesh()
        G2.nom=self.nom+"x2"
        G2.nn=self.nn+nar
        # creation des nds / artes
        G2.X=zeros((G2.nn,2),dtype=float)
        G2.X[:self.nn,:]=self.X[:,:]
        G2.Frt=zeros((G2.nn),dtype=int)
        G2.Frt[:self.nn]=self.Frt[:]
        nn2=self.nn
        for L in AR:
                G2.X[nn2,:]=0.5*(self.X[L[0],:]+self.X[L[1],:])
                nn2 += 1
        print "creation des noeuds ",nn2,nar,self.nn
        # aretes frontieres
        ARF=self.arfront()
        for L in ARF:
                I1=where(AR[:,0]==L[0])[0]
                I2=where(AR[ix_(I1),1]==L[1])[1]
                nn2=self.nn+I1[I2[0]]
                G2.Frt[nn2]=max(self.Frt[L[0]],self.Frt[L[1]])
        # creation des triangles
        G2.ne=4*self.ne
        G2.Tbc=zeros((G2.ne,3),dtype=int)
        N=zeros((6),dtype=int)
        for k in range(self.ne):
                N[:3]=self.Tbc[k,:]
                # recherche des nouveaux noeuds
                L1=[N[1],N[2]];
                if N[1]>N[2]: L1=[N[2],N[1]];
                I1=where(AR[:,0]==L1[0])[0]
                I2=where(AR[ix_(I1),1]==L1[1])[1]
                N[3]=self.nn+I1[I2[0]]
                L1=[N[2],N[0]];
                if N[2]>N[0]: L1=[N[0],N[2]];
                I1=where(AR[:,0]==L1[0])[0]
                I2=where(AR[ix_(I1),1]==L1[1])[1]
                N[4]=self.nn+I1[I2[0]]
                L1=[N[0],N[1]]; 
                if N[0]>N[1]: L1=[N[1],N[0]]; 
                I1=where(AR[:,0]==L1[0])[0]
                I2=where(AR[ix_(I1),1]==L1[1])[1]
                N[5]=self.nn+I1[I2[0]]
                # creation des 4 triangles
                G2.Tbc[4*k  ,:]=[N[0],N[5],N[4]]
                G2.Tbc[4*k+1,:]=[N[1],N[3],N[5]]
                G2.Tbc[4*k+2,:]=[N[2],N[4],N[3]]
                G2.Tbc[4*k+3,:]=[N[3],N[4],N[5]]
        print "creation des elts ",self.ne,G2.ne
        # fin
        return G2

# affiche matrice
def plotMat(Ai,titre):
        """affiche la forme de la matrice"""
        plt.figure(figsize=(6,4))
        plt.spy(A)
        plt.title(titre)
        plt.draw()
        return
# appel FreeFem++
def meshFreefem(nom,script):
        """ creation d'un maillage avec un script FreeFem """
        meshnom="%s.msh"%(nom)
        F=open("%s.edp"%(nom),'w')
        F.write(script)
        F.write('\nsavemesh(Th,"%s");\n'%(meshnom))
        F.close()
        subprocess.call(["FreeFem++","%s.edp"%(nom)])
        G=mesh(meshnom)
        return G
# lecture fichier de resultats
def readres(filename):
        F=open(filename,'r')
        L=F.readline()
        nn=int(L)
        U=loadtxt(F,dtype=float)
        print "lecture resultat ",nn,size(U)
        return U.reshape((nn))
# execution script Freefem
def Freefem(nom,script,log=False):
        """ execution script FreeFem"""
        F=open("%s.edp"%(nom),'w')
        F.write(script)
        F.close()
        if log:
            subprocess.call(["FreeFem++","%s.edp"%(nom)],stdout=open("%s.log"%(nom),'w'))
        else:
            subprocess.call(["FreeFem++","%s.edp"%(nom)])
        return

