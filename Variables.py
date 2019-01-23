# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:08:36 2017

@author: User
"""

#find age
DOB=1994
Age=2018-DOB
AgeMessage="your age is {} and DOB {}".format(Age,DOB)
print(AgeMessage)
print("your age is" , Age)

############ ID memory, type de variable
x=10
y=3,4
z="chfiha"
print(type(x))
print(type(y))
print(type(z))
print(id(x))
print(id(y))
print(id(z))
####################### keLower case to string
from django.template.defaultfilters import upper, lower
name="Mohamed El Alami"
StrLen=len(name)
print(StrLen)
print(upper(name))
print(lower(name)) 