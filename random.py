# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:26:09 2021

@author: Shreya
"""
#this program generates random number from 0 to 10 without the help of any
#random function
import time
milliseconds = int(round(time.time() * 1000))
print(milliseconds)
x=milliseconds
num=(x*8)%11
print(num)





