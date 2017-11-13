#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 22:44:35 2017
Merge Sort
@author: leo
"""
def merge_sort(vector):
    if(len(vector)>1):
        middle = (len(vector))/2
        left_vector= vector[:middle]
        right_vector = vector[middle:]
        merge_sort(left_vector)
        merge_sort(right_vector)
        i=0
        j=0
        k=0
        while i<len(left_vector) and j < len(right_vector):
            if left_vector[i]<right_vector[j]:
                vector[k] = left_vector[i]
                i+=1
            else:
                vector[k]=right_vector[j]
                j+=1
            k+=1
        while i < len(left_vector):
            vector[k] = left_vector[i]
            i+=1
            k+=1
        while j< len(right_vector):
            vector[k] = right_vector[j]
            j+=1
            k+=1
    return vector


print merge_sort([10,2,4,5,8,12,3,24,9,15])