# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:14:29 2021

@author: Hans
"""
words = [w.split(';')[0] for w in words]
words = {re.sub('^[1-9]. |[ .]', '', w).lower() for w in words}