# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 02:05:36 2024

@author: Hi
"""
#1
def can_bac_n(x, n):
    return x ** (1/n)

#x = int(input("Nhập x: "))
#n = int(input("Nhập n: "))
if __name__== "__main__":
    print(can_bac_n(8, 3)) 

#2 
def tinh_binh_phuong(so):
    if so > 0:
        return so ** 2
    else:
        return "Vui lòng nhập một số dương"
      
#so = int(input("Nhập số nguyên dương: "))
if __name__== "__main__":
    print(tinh_binh_phuong(3))

#3
def kiem_tra_chan_am(x):
    return x < 0 and x % 2 == 0
#x = int(input("Nhập vào có phải là số chẵn và có giá trị âm: "))
if __name__== "__main__":
    print(kiem_tra_chan_am(3)) 

#4 
def kiem_tra_so(x):
    if x < 0 and x % 2 != 0:
        return -1
    elif x > 0 and x % 2 == 0:
        return 1
    else:
        return 0

#x = int(input("Nhập x: "))
if __name__== "__main__":
    print(kiem_tra_so(5)) 

#5 
def ktra_gtri():
    n= input("nhap n:")
    if n.replace('.','',1).replace('-','',1).isdigit():
        n = float(n)
    #if n.lstrip('-').isdigit():(-)123
    #n = int(n)
    #if n.strip('-').isdigit():(-)123(-)
    #n = int(n)
    if -89 <= n <=90:
        return n
    print("khong hop le,nhap lai")
    return ktra_gtri()
         
if __name__== "__main__":
    print(ktra_gtri())