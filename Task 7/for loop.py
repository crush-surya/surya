for i in range(1,100):
    if i%6==0 and i%9!=0:
        print(i)
print()
 
s =0
for i in range(1,50):
    if i%2!=0:
        s+=i
        print(i)
print()

c =0
for i in range(1,200):
    if i%4==0 and i%6==0:
        c+= 1
print(c)
print()

n =int(input("Enter a number :"))
for i in range(1,11):
    print(f"{i} x {n} = {i*n}")
print()


n = int(input("Enter a number :"))
f =1
for i in range(1,n+1):
    f*=i
print(f)
print()



for n in range(2,50):
    f =0
    for i in range(2,n):
        if n%i==0:
            f =1
            break
    if f==0:
        print(n)
print()


n = int(input("Enter a number :"))
s =0
for i in str(n):
    s+=int(i)
print(s)
print()

c =0
for i in range(1,501):
    for j in range(1,9):
        if j**3==i:
            c ++1
print(c)
print()


n=int(input("Enter a number :"))
r =0
for i in range(len(str(n))):
    r=r*10 +n%10
    n//=10
print(r)
print()

for i in range(1,101):
    if i%10==5:
        continue
    print(i)







