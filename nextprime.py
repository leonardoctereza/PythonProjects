#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:33:52 2017

@author: leo
"""
from math import sqrt
def prime(n):
    """
    Input n and return all primes till n
    """
    result=0
    divided=3
    if n%2 == 0:
        result+=1
    while result<1 and divided <= (int)(sqrt(n)):
        if(n%divided == 0):
            result+=1
        else: divided+=1
    if(result ==0):
        return True
    else: return False

def next_prime(n):
    while(prime(n)!= True):
        n+=1
    return n

n = input("Enter a number: ")
answer = raw_input("Do you want the next prime of that number? y/n: ")
while answer == 'y':
    n = next_prime(n)
    print n
    answer = raw_input("Do you want the next prime of that number? y/n: ")
    n+=1