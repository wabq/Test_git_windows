
def main():
    try:
        ReadFile=open("test.txt","r") 
        # imaginons que le fichier test.txt est  est introuvable,suppr.. 
        # on fais ça pour au cas ou le fichierl'application ne crache pas 
        for line in ReadFile:
            print(line)
        ReadFile.close()
    except IOError: 
        #le nom de l'erreur il faut aller voir le site python correspondant a l"erreur , on faisant ça 
        #le programme ne va pas cracher et il va aller jusqu'au bour donc printer app is done 
        print("File not found")
    print("app is done")
if __name__ == '__main__':main()
