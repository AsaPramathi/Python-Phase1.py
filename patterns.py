for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print()


     
for i in range(1,5):
    for j in range (1,i+1):
        print("*",end=" ")
    print()

print()
for i in range(1,6):
    for j in range (1,7-i):
        print("*",end=" ")
    print()


for i in range(1,6):
    #spaces
    for s in range (1,6-i):
        print(" ",end=" ")
    #pattern
    for j in range (1,i+1):
        print("*",end=" ")
    print()


for i in range(1,6):
    #spaces
    for s in range (1,6-i):
        print("",end=" ")
    #pattern
    for j in range (1,i+1):
        print("*",end=" ")
    print()


for i in range(1,5):
    for j in range (1,i+1):
        print(j,end=" ")
    print()

n=1
for i in range(1,5):
    for j in range (1,i+1):
        print(n,end=" ")
        n=n+1
    print()

for i in range(1,5):
    for j in range(1,5):
        if i==1 or i==4 or j==1 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    

    
r=int(input("enter num of rows:"))
c=int(input("enter num of columns:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or i==(r) or j==1 or j==(c):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 


for i in range(1,5):
    #spaces
    for s in range (1,5-i):
        print(" ",end=" ")
    #pattern
    for j in range (1,2*i):
        print("*",end=" ")
    print()

for i in range(1,6):
    for j in range (1,i+1):
        print(i,end=" ")
    print()
for i in range(1,5):
    for j in range (1,6-i):
        print(5-i,end=" ")
    print()


for i in range (1,5):
    for j in range(1,8):
        if i==4 or i+j==5 or j-i==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

