  #le processus marche aussi en remplaçant tout par if mais il va comparer
  #degree avec tout ces if .. d'ou l'avantage d'utiiser elif car dés qu'il 
  #trouver la solution il va directement passer les autres conditions

Degree=input("enter your degree:")
if( int(Degree)>=90):
    print("your Score is A")
elif(int(Degree)>=80 and int(Degree)<90): 
    print(" your score is B")             
elif(int(Degree)>=70 and int(Degree)<80):
    print(" your score is C")
elif(int(Degree)>=60 and int(Degree)<70):
    print(" your score is D")
else:
    print("you fail")
print("app is done") #pour voir le passage dans le debug
