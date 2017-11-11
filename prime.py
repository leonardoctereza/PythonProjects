#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 11:50:48 2017
Prime to the nth digit
@author: leo
"""
from math import sqrt
def prime(n):
    """
    Input n and return all primes till n
    """
    for i in range(n):
        result=0
        divided=3
        if i%2 == 0:
            result+=1
        while result<1 and divided <= (int)(sqrt(i)):
            if(i%divided == 0):
                result+=1
            else: divided+=1
        if(result ==0):
            yield i

n = input("Enter a number and it will return all prime numbes till him: ")
print list(prime(n))
            
