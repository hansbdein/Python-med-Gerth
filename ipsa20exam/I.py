'''
    VECTOR SORT

    In this problem you are given a list of tuples, each tuple
    containing three integers. We consider the tuples representing 3d
    vectors and your task is to sort the list of vectors by increasing
    norm, where the norm of (x, y, z) = sqrt(x**2 + y**2 + z** 2).

    Input:  A Python list of n tuples, where 1 <= n <= 1000 and each tuple
            contains 3 integers representing a 3d vector. It is
            guaranteed that all vectors have different length.

    Output: The list of tuples sorted with respect to increasing norm.

    Example:

      Input:  [(3, 1, 2), (-2, 1, 4), (2, 2, 2), (-1, 1, -1)]

      Output: [(-1, 1, -1), (2, 2, 2), (3, 1, 2), (-2, 1, 4)]

    Note: Below you only need to implement the function vector_sort,
          that as input gets the list of tuples.
'''

def vector_sort(vectors):
    return sorted(vectors, key=lambda L: sum(n**2 for n in L))


vectors = eval(input())
print(vector_sort(vectors))
