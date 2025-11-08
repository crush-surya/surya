for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()

for i in range(1,6):
    for s in range(5-i):
        print(" ",end=" ")
    for j in range (1,i+1):
        print(j,end=" ")
    print()
print()

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()

ch=65
for i in range(1,7):
    print(chr(ch)*i)
    ch+=1
print()

ch=65
for i in range(1,6):
    for j in range(i):
        print(chr(ch),end="")
        ch+=1
    print()
print()

ch=65
for i in range(1,6):
    print(chr(ch)*i)
    ch+=1
print()

ch=65
for i in range(1,6):
    for j in range(65,65+i):
        print(chr(j),end="")
    print()
print()



 
