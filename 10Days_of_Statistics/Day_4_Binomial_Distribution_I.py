#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:48:29 2021

@author: soyoon-yoon
"""



boy = 109/209
girl = 100/209


value = 1-(girl**6)-(6*(girl**5)*(boy))-(15*(girl**4)*(boy**2))
value = round(value,3) #print("%.3f" %value)

print(value)


