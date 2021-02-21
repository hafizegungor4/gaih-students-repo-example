counter=0
names=[]
surnames=[]
midterms=[]
homeworks=[]
finals=[]
average=[]

for i in range(5):
    name=input("Please enter your name: ")
    names.append(name)
    surname=input("Please enter your surname: ")
    surnames.append(surname)
    midterm = int(input("Midterm Grade: "))
    midterms.append(midterm)
    final = int(input("Final Grade: "))
    midterms.append(midterm)
    homework = int(input("Homework Grade: "))
    midterms.append(midterm)
    ort = ((midterm+final+homework)/3) 
    average.append(ort)
    dicti = {"Name":name,"Surname":surname,"Midterm Grade":midterm,"Final Grade":final,"Homework Grade":homework,"Grade Point Average":ort}
    print(dicti)
    counter+=1

print(average)

for name,ort in names,average:
    print (name,"\t\t",ort)
