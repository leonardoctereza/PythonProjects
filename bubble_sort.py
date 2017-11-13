#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 22:36:13 2017
Bubble Sort
@author: leo
"""

def bubble_sort(nlist):
    aux = 0
    for i in range(len(nlist)):
        for j in range(len(nlist)):
            if(nlist[j]>nlist[i]):
                aux = nlist[j]
                nlist[j] = nlist[i]
                nlist[i] = aux
    return nlist

x = [10,14,15,20,1,7,4,3,8,12,1,7]
print bubble_sort(x)