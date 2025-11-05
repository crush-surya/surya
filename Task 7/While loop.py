i =10
while i>= 1:
    print(i)
    i=i-1
    print()

num =48293
sum =0
for i in str(num):
    if int(i)%2==0:
     sum+=int(i)
     print(sum)
print()
    

num = 6381718345
count =0
while num>0:
    count+=1
    num//=10
    print(count)
print()

n =int(input("Enter a number :"))
t=n
r=0
while n>0:
    r=r*10 + n%10
    n//=10
if t==r:
    print("palindrome")
else:
    print("not palidrome")
print()

num =6381718345
rev =0
while num>0:
    digit = num%10
    rev = rev *10+digit
    num = num//10
    print("Reversed number :", rev)
    print()

a,b =0,1
while a<=100:
    print(a)
    a,b=b,a+b
print()

a = 2
b =5

result=1
count =0
while count<b:
    result =result*a
    count = count+1
    print ("Result =",result)
print()


n =28
count =0
while n>=1:
    n = n/2
    count+=1
    print("number of divisions :",count)
print()

n = 786
while n>0:
    print(n%10)
    n =n//10
print()

n =int(input())
s =0
while n>0:
    d=n%10
    s+=d*d
    n//=10
    print(s)
print()







