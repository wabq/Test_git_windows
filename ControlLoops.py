
word="Python" #il va tout printer sauf t 
for  letter in word:
    if(letter=='t'):
        continue;
    print(letter)





word="Python" #il va s'arreter quand letter =  t  et donc va printer que pet y 
for  letter in word:
    if(letter=='t'):
        break;
    print(letter) 

l =[1,33,45,32,55,22,23,100]
for item in l:
    if(item==55):
        print("number is found")
        break;

print("App is done")
