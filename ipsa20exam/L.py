'''
    RECURSIVE FUNCTION

    Consider the following recursively defined integer function 

        f(n) = f(n - 1) + 2 * f(n - 2) + 3 * f(n - 3)

    for n >= 3, and f(n) = 1 for 0 <= n < 3.

    Your task is to write a program that computes f(n).

    Input:

      A single line containing an integer n, where 1 <= n <= 10000.

    Output:

      f(n)

    Example:

      Input:  10

      Output: 2036
'''




n=int(input())


n1=1
n2=1
n3=1

for i in range(n-2):
    
    new = n3 + 2 * n2 + 3 * n1
    n1=n2
    n2=n3
    n3=new


print(new)
    
