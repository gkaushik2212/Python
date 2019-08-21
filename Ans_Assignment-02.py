#1
x = [1,2,3,4,[10,20,30,40,[100,200,300,400],"rishabh_",5+5j],4000]
print (x[4][0:2])
print (x[4][6:7])
print (x[4][4][2:4])
print (x[4][3:6])

#2
for i in range(1,22):
    for j in range(1,22):
        if (i+j)%2==0:
            print((i,j))

#3
from collections import Counter

x = "hello&*$$world"
y = Counter(x)
print ("count of & = " + str(y['&']) + (" count of $ = " + str(y['$']))) 


#4
for i in range(1,50):
    if (i**3)%2 !=0:
        print(i)

#5
l = [1,2,3,4,5]
b = []
for i in l:
    b.append(i*3)
print(b)

#6
x = "Hello world i am learning python"
[len(x) for x in x.split()]
