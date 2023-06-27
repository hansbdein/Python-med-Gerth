
import random

while True:
    x, y, i, j, = [random.randint(-100, 100) for _ in range(4)]
    z, k = [random.randint(-10, 10) for _ in range(2)]
            
    if z == 0 or k == 0: # skip illegal input
        continue

    r = range(x, y, z)[i:j:k]

    a = x+z*i
    b = x+z*j
    c = z*k

    print("range(%s,%s,%s)[%s:%s:%s] =" % (x, y, z, i, j, k), r)
    
    if r != range(a, b, c):
        print("Wrong range: a b c =", a, b, c)
        break