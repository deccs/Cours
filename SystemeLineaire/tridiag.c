/* ================================ */
/* resolution système tridiagonale  */
/* [X]=tridiag(A,B)                 */
/* =================================*/
#include <math.h>
#include <stdlib.h>

/* resolution d'un systeme tridiagonal */

void tridiag(double *A0,double *A1,double *A2,double *B,double *X,int N) {

  int j;
  double det;
  /* vecteur de travail */
  double *U;
  U=(double *)malloc(sizeof(double)*N);
  /* decomposition et subsitution */
  det=A1[0];
  X[0]=B[0]/det; U[0]=0;
  for(j=1; j<N; j++) {
    U[j]=A2[j-1]/det;
    det=A1[j]-A0[j]*U[j];
    X[j]=(B[j]-A0[j]*X[j-1])/det;
  }
  /* remontee */
  for (j=N-2; j>=0; j--) {
    X[j]-= U[j+1]*X[j+1];
  }
  free(U);
  return;
}
