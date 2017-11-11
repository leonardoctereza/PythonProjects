#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 11:07:33 2017
Fibonacii using yield and list
@author: leo
"""
def fib(n):
    """
        Func that returns fibonacii sequence
        input n and generates n fibonacci numbers 
    """
    a,b = 1,1
    for i in range(n):
        yield a
        a,b = b,a+b
        
n = input("How many numbers in fibonacci sequence you want to see? ")
if n <= 10000:
    print list(fib(n))
else:
    print "Number too large to generate fibonacci"
    