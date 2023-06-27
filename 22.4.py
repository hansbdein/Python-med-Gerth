
import re
from collections import Counter

'''
s = open('saxo.txt').read()  

S = re.sub('\n', ' ', s).lower()

thewords=re.findall(r'the \w+',S)



[print(str(word[1]) + ' ' + word[0]) for word in Counter(thewords).most_common(11)]

'''


[print(str(word[1]) + ' ' + word[0]) for word in Counter(re.findall(r'the \w+',re.sub('\n', ' ', open('saxo.txt').read()).lower())).most_common(11)]