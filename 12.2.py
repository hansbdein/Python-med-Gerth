"""
HANDIN 6 (ancestors))

This handin is done by:

    201706079 Hans Brüner Dein

Reflection upon solution:

    
Først lavede jeg klassen Person. Derefter laved jeg annotatedperson, hvorefter
jeg var nød til at rette i Person, således ancestor kunne håndtere None når 
forældre ikke var angivet. For at teste indsatte jeg print_tree fra 9.2.
Sidst ændrede jeg default værdien af død og fødsel til en tom string, 
for at undgå at der stod margrethe døde i år None.

Fixede fejlene

"""







class Person:
    def __init__(self,name=None, mother=None, father=None, born=None, died=None):
        self.name = name
        self.mother = mother
        self.father = father
        self.born = born 
        self.died = died


    def __str__(self):
        return ("%s %s-%s" %(self.name,self.born if self.born else '', self.died if self.died else '',))
    
    def ancestor(self):
        
        return(str(self),('-' if self.father==None else self.father.ancestor(), 
                          '-' if self.mother==None else self.mother.ancestor()))
        
    
    
class AnnotatedPerson(Person):  
    
    def __init__(self,name=None, mother=None, father=None, born=None, died=None,note=None):
        self.note = note
        super().__init__(name, mother, father, born, died)
    
    def __str__(self):
        return super().__str__()+' ['+self.note+']'
    




louise_af_HK = Person("Louise of Hessen-Kassel", None, None, 1817, 1898)
christian_9 = Person("Christian 9.", None, None, 1818, 1906)
louise_af_SN = AnnotatedPerson("Louise of Sweden-Norway", None, None, 1851, 1926, "born Princess of Sweden and Norway")
frederik_8 = Person("Frederik 8.", louise_af_HK, christian_9, 1870, 1947)
christian_10 = Person("Christian 10.", louise_af_SN, frederik_8, 1870, 1947)
ingrid = AnnotatedPerson("Ingrid of Sweden", None, None, 1910, 2000, "Queen of Denmark 1947-1970")
frederik_9 = Person("Fredrik 9.", None, christian_10, 1899, 1972)
margrethe_ii = AnnotatedPerson("Margrethe II", ingrid, frederik_9, 1940, note="Queen of Denmark")




def print_tree(T,depth=0):
    for node in T:
        if isinstance(node,str):
            print('  |'*depth +'--'+node)
        else:
            print_tree(node,depth+1)






print_tree(margrethe_ii.ancestor())
