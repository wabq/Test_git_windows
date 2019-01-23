

def Display():
    print("hello") #fonction qui ne retourne rien juste affiche 
    print("Welcome to Python")

def sum(n1,n2): #fonction qui retourn la somme
    z=n1+n2
    return z #on peut faire ici print est donc donc main pas la pein de sauvegarder le resultat dans une variable 

def main():
    Display()
    Results=sum(10,12) #il faut absolument sauvegarder resultat dans une variable car la fonction retourne qqchose
    print("sum={}".format(Results))
    Results=sum(12,133)
    print("sum={}".format(Results))
    Results=sum(140,122)
    print("sum={}".format(Results))





if __name__ == '__main__':main()
