# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:44:10 2024

@author: Hi
"""

def tinhtong(*args, **kwargs):
    return sum(args)
def tinh_tich(*args, **kwargs):
    tich = 1
    for i in args:
        tich*= i
    return tich
if __name__=="__main__":
    ds = [1,2,3,4,5]
    print(tinhtong(*ds))
    print(tinh_tich(*ds))