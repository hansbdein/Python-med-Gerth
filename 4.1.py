a = [[1, 2], [3, 4]]
b = a
c = a[:]
b[0] = [5, 6]
c[1][1] = 7
print(a, b, c)