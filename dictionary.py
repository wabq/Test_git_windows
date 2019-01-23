# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 15:11:40 2017

@author: User
"""

person=dict(Name="3atma",Age=23,Salary=100)#mutable
print(person)
person["Name"]="3atma bezoho"
print(person["Name"])
person["rwijel"]="yes"
print(person)
del person["Age"]
print(person)


#object type:
# mutable : list et dictionnaire
#si je declare une liste ou un dictionnaire et je le change , il va changer cette liste la ou 
# ce dictionnaire . preuve id(dic)

##############################
# immutable :
# int,float,string,tuple (si je declare x=10 ensuite je fais 
#   x=11 il ne va pas changer la meme variable mais va supprimer la premieer variable ainsi que son adress 
# en memoire et créer uen nouvelle variable aevc une nouvelle adresse de memoire .preuv id(x))


########## Math operations 
# x=0b101 , y=0b111 ; x and b = 7 ; x & y = 5
# 0b111 ( chiffre binaire = 7 )
# False, True avec capital Letter
# 