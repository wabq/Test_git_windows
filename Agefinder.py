# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 21:10:26 2017

@author: User
"""
import datetime
dateNaissance=input("rentrez votre date de naisssance") # the input est un string
maintenant = datetime.datetime.today().year #int
print("votre age est ",maintenant-int(dateNaissance)) 
print("your age is {}".format(maintenant-int(dateNaissance))) #autre façon de printer


