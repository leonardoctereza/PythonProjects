#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 22:09:03 2017
Collatz Conjecture
@author: leo
"""
def collatz_conjecture(n):
    count = 0
    while(n>1):
        if(n%2==0):
            n= n/2
        else: 
            n = n*3 +1
        count+=1
    return count

n = input("Choose a number bigger than 1:")
if(n>1):
    print "The number of steps to reach 1 in the collatz conjecture was: {}".format(collatz_conjecture(n))