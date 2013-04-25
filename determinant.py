#Takes a matrix as parameter and returns the determinant of the matrix.
%cython
from sage.all import matrix

def get_determinant(mat):
    return mat.det()
