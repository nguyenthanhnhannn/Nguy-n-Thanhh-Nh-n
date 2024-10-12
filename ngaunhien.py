# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:46:29 2024

@author: Hi
"""

import random
phantu = random.randint(20, 30)

giatribinhphuong = [random.uniform(18, 99) ** 2 for _ in range(phantu)]

print(f"Số lượng phần tử: {phantu}")
print("Các giá trị bình phương:", giatribinhphuong)