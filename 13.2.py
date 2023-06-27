
#inputstr='matind.txt'



def Transpose():
    inputstr=input("what is the name of input file: ")
    while True:
        try:
            f = open(inputstr)
        except FileNotFoundError:
            print('Could not find file')
            continue
            
            
            
        lines=f.readlines()
        rows = [list(line.rstrip("\n").split(";")) for line in lines]
        f.close()
     
        try:    
            for row in rows:
                if len(row)!=len(rows[0]):
                    raise TypeError
                
        except TypeError:
            print('File does not contain a valid matrix')
            continue
        else:
            getoutput(list( zip(*rows)))
            break
        
        


        

def getoutput(L):
    
    while True:
        outputstr=input("what is the name of output file: ")
        try:
            open(outputstr).close()
            
        except FileNotFoundError:
            writematrix(L,outputstr)
            break
        else:
            
            answer=False
            while not answer:
                confirm=input("Do you want to overwrite existing file: ")
                if confirm=='yes':
                    writematrix(L,outputstr)
                    answer=True
                    break
                elif confirm=='no':
                    continue
                    answer=True
                else:
                    print('please answer yes or no')
    

def writematrix(L,outputstr):
    
    g = open(outputstr,'w')
    
    for x in L :
        g.write(';'.join(x)+'\n') 
    
    g.close
    



        
Transpose()       



