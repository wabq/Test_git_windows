
x=10 #Global var
def Show():
     global x  # on rajoute ça pour etre sur qu'ilva prendre le x definit en global
     print(x)

def main():
    global x # on rajoute ça pour etre sur qu'ilva prendre le x definit en global
    print("x={}".format(x))
    Show()
if __name__ == '__main__':main()



################# variable local
def Show():
     
     print(x)

def main():
    x=10
    print("x={}".format(x))
    Show()
if __name__ == '__main__':main()
#ici il va afficher une erreur car x edefini dans main est local ( la fct show ne va pas connaitre le x)
#les deux fonction sont dans le meme niveau , et donc chaque bloque a ses propes variables ..


###### Lambda type of function 

def op(x): 
    return x*2
 
    
#ceci est equivalent a 

op1= lambda x:x*2 #(les parametres x,y...):puis l"expression que lambda va faire 
#matintenant si on fait op1