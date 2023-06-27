''' 
    MISSING RECTANGLE CORNER

    A rectangle has four corners (x1, y1), (x1, y2), (x2, y1) and (x2, y2),
    for four integers x1, x2, y1, and y2, where x1 != x2 and y1 != y2.
    Your task is to find the missing corner, given three of the corners.

    Input:  Three lines, each line containing two integers x and y,
            separated by a space, representing a corner point (x, y). 
            It is guaranteed that the three input points are the
            corners of a rectangle as defined above.

    Output: A single line with two integers x and y, separated by a space,
            representing the missing corner point (x, y).

    Example:

      Input:  2 5
              4 3
              4 5

      Output: 2 3
'''


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())


if x1==x2:
    x=x3
    
if x3==x2:
    x=x1
    
if x3==x1:
    x=x2
    
if y1==y2:
    y=y3
    
if y3==y2:
    y=y1
    
if y3==y1:
    y=y2   
    
print(str(x)+' '+str(y))
    