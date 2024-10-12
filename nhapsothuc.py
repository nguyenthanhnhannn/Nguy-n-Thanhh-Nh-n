# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:25:26 2024

@author: Hi
"""

while True:
    try:
        n = float(input("Nhập một số thực (không phải số nguyên) thuộc [-89.9; 88.8]: "))
        if -89.9 <= n <= 88.8:
            if n % 1 != 0:  # Nếu phần dư khi chia cho 1 khác 0, tức là nó có phần thập phân
                print(f"Giá trị hợp lệ: {n}")
                break  
            else:
                print("Bạn đã nhập một số nguyên. Vui lòng nhập lại một số thực.")
        else:
            print("Giá trị không nằm trong khoảng [-89.9; 88.8]. Vui lòng nhập lại.")
    except ValueError:
        print("Đây không phải là một số thực hợp lệ. Vui lòng nhập lại.")