

a = [1]
a[0] = a

def deepcopy(L):
    Ln=[]
    for x in L:
        
        if isinstance(x,list):
            if x == x[0]:
                print('det virker')
                Ln.append(a)
            else:
                Ln.append(deepcopy(x))
        else:
            Ln.append(x)
    
    print(Ln)
    return Ln


L1 = [[1], [2], [3]]
L2 = deepcopy(L1)


L1[1] = L1[0]
L1[2][0] = L1


L3 = deepcopy(L1)


L3[0][0] = 7
print('{L1=} {L2=} {L3=}')




'''


from matplotlib.pyplot import plot


L=[1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596,2279184,14772512,95815104,666090624,4968057848,39029188884,314666222712,2691008701644,24233937684440,227514171973736,2207893435808352,22317699616364044,234907967154122528]

#y=list(range(1,len(L)))

y=[x/5**i for i,x in enumerate(L) ]

plot(range(len(L)),y)

'''