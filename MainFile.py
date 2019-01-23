import datetime #les imports toujours la , jamais dans le main ou dans une fonction

def main():
    #main code function  #
    DOB=input("Enter your DOB:")
    CurrentYear=datetime.datetime.now().year
    Age=CurrentYear-int(DOB)
    print("Your age is {}".format(Age))




if __name__ == '__main__':main() #fire this methode which name is main()


#process , il a commencer par importer 