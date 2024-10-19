# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:43:08 2024

@author: Hi
"""
import math
def chuvi_dt(hinh, pheptinh, *args, **kwargs):
    if hinh == "vuong": 
        canh = args[0]
        return 4 * canh if pheptinh == "chuvi" else canh * canh
        # if pheptinh == "chuvi": 
            #return 4* canh
        #else: 
            #return canh*canh
    elif hinh == "chunhat":
        dai = args[0]
        rong = args[1]
        return 2 * (dai + rong) if pheptinh == "chuvi" else dai * rong
    elif hinh == "hinhtron": 
        ban_kinh = args[0]
        return 2 * math.pi * ban_kinh if pheptinh == "chuvi" else math.pi * ban_kinh ** 2
    else: 
        return "Hình không hợp lệ"
    
if __name__=="__main__":
    print("Chu vi hình vuông: ", chuvi_dt('vuong','chuvi',3))
    print("Diện tích hình vuông: ", chuvi_dt('vuong','dientich',3))
    print("Chu vi hình chữ nhật: ", chuvi_dt('chunhat','chuvi',3,4))
    print("Diện tích hình chữ nhật: ", chuvi_dt('chunhat','dientich',3,4))
    print("Chu vi hình tròn: ", chuvi_dt('hinhtron','chuvi',3)) 
    print("Diện tích hình tròn: ", chuvi_dt('hinhtron','dientich',3)) 
    
    

