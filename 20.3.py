

def subsets(L):
    for i in range(2**len(L)):
        yield [L[y] for y, x in enumerate(format(i, "0"+str(len(L))+"b")) if int(x)]


print(list(subsets([1,2,3,4])))


