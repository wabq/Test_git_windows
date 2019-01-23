# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:10:23 2017

@author: User
"""

#Tuples ( Inchangeable;Inmutable)
age=(1,99,15,25,85,93,24)
#ages.add(23) ce n'est pas possible
print(age)
print(age[0:2])#indexation en python commence par 0 le dernier en le prend pas 
########################################
#Lists
ages=[1,99,15,25,85,93,24] #peuvent change,mutable
ages.append(100)
print(ages)
ages.insert(1,55) #inserer un element a un endroit précis
print(ages)

l[:]=range(10) #liste de 0 a 9 
print(l)
l[0:3]=(0,0,0) #remplacer les valeur de 0 1 et 2 par des 000
print(l)

 
#######
print("words split")
str="wa fayen chfiha dyanna"
words=str.split(' ')
print(words)
str="wa fayen$chfiha dyanna"
words=str.split('$')
print(words)