import random

list=[]
counter=0

#2 ile 101 arasındaki asal sayıları bulup liste oluşturduk.
for i in range(2,101):
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        list.append(i)

#oluşturulan asal sayı listesinden de rastgele sayılar çekerek 3X3 'lük matris oluşturduk.
while counter<3:
    list1=random.sample(list, 3)
    counter+=1
    print(list1)