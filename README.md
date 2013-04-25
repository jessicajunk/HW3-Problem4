HW3-Problem4
============
Calculates the determinant of a matrix.

Example:

from sage.all import matrix
A = Matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

get_determinant(A) --> 0


Code in python: timeit("get_determinant(A)") --> 625 loops, best of 3: 6.11 µs per loop

Code in cython: timeit("get_determinant(A)") --> 625 loops, best of 3: 5.61 µs per loop
