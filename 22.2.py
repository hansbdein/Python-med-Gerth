# -*- coding: utf-8 -*-
"""
Created on Tue May 11 14:20:46 2021

@author: Hans
"""
import re



text = 'this.was a test!, and here comes   :   the rest'


ans=re.split(r'[^\w]*[!?;:.,][^\w]*',text)

print(ans)

['this', 'was a test', 'and here comes', 'the rest']