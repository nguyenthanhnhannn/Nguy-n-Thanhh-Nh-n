# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 23:19:30 2024

@author: Hi
"""

n = int(input("Nhập số vào từ [-99;99]: "))
while n < -99 or n > 99:
    n = int(input("Nhập lại n, n chỉ được từ [-99;99]: "))
print(n)
    
