#include <stdlib.h>
#include <math.h>
#include <iostream>
//
// calcul de la somme de n termes de la serie x-x^2/2+x^3/3-
//
double serie(double x,int n)
{
	double coef=x;
	double somme=0.0;
	for (int i=1; i<=n; i++)
	{
		somme = somme + coef/i;
		coef = -coef*x;
	}
	return somme;
}
//
int main(int argc,char *argv[])
{
	int n=20;
	double x=0.2;
	std::cout<<"Calcul de la serie pour n="<<n<<" et x="<<x<<std::endl;
	std::cout<<"Somme   = "<<serie(x,n)<<std::endl;
	std::cout<<"Log(1+x)= "<<log(1+x)<<std::endl;
	return 0;
}

