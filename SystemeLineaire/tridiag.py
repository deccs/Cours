import numpy as np
import ctypes

_libfunctions = np.ctypeslib.load_library('libtridiag', '.')

_libfunctions.tridiag.argtypes = [np.ctypeslib.ndpointer(dtype=np.float), 
                                  np.ctypeslib.ndpointer(dtype=np.float),
                                  np.ctypeslib.ndpointer(dtype=np.float),
                                  np.ctypeslib.ndpointer(dtype=np.float),
                                  np.ctypeslib.ndpointer(dtype=np.float),
                                  ctypes.c_int]
_libfunctions.tridiag.restype  = ctypes.c_void_p

def tridiag(a,b,c,F):
    """ resolution AU=F pour un ematrice A tridiagonale [a,b,c] """
    a = np.asarray(a, dtype=np.float)
    b = np.asarray(b, dtype=np.float)
    c = np.asarray(c, dtype=np.float)
    F = np.asarray(F, dtype=np.float)
    n=len(a)
    U = np.empty(len(a), dtype=np.float)
    _libfunctions.tridiag(a,b,c,F,U,int(n))
    return U