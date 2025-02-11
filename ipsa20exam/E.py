'''
    TREE MIRROR

    In this problem we consider the problem of mirroring a binary tree
    around a vertical line. We assume that the tree is represented by
    a recursive tuple, where leaves are integers and all other nodes
    have two children. The mirror of a tree is obtained by
    recursively reversing the order of the children of each internal
    node.

                 /\                               /\
                /  \                             /  \
               /    \                           /    \
              /\    /\            ==>          /\    /\
             1  \  4  5         mirror        5  4  /  1
                /\                                 /\ 
               2  3                               3  2
               
    T = ((1, (2, 3)), (4, 5))     mirror(T) = ((5, 4), ((3, 2), 1))

    Input:

        A recursive tuple representing a binary tree T where all
        leaves are integers, and all internal nodes have two
        children.  The tree has between 2 and 100 leaves.

    Output:

        A recursive tuple representing the mirror of the tree T.

    Example:

      Input:  ((1, (2, 3)), (4, 5))

      Output: ((5, 4), ((3, 2), 1))

    Note:

      The below code already takes care of reading a tree and printing
      the result of calling mirror(tree). Your task is to implement
      the body of the recursive function mirror.
'''


def mirror(tree):
    
    if isinstance(tree, int):
        return tree
    
    return (mirror(tree[1]),mirror(tree[0]))
        


tree = eval(input())
print(mirror(tree))
