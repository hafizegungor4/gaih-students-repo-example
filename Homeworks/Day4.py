import random 

firstList=[]
secondList=[]

def primeFirst():

    for i in range(2,500):
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            firstList.append(i)

    print(firstList)
    return firstList


def primeSecond():
    
    for i in range(500,1000):
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            secondList.append(i)

    print(secondList)
    return secondList
print("\n\t\t\t\t***************First Lİst***************\n")
primeFirst()
print("\n\t\t\t\t***************Second Lİst***************\n")
primeSecond()
