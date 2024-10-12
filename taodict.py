# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:08:27 2024

@author: Hi
"""


n = int(input("Nhập giá trị nguyên n: "))
tao_dict = {i: i** i for i in range(1, n + 1)}
print(tao_dict)