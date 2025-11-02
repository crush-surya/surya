#11
a =9
if a%2==0:
    print("even")
else:
    print("odd")
print()

#12
#a =float(input("Enter a number :" ))
a =3.14
if a>0:
    print("positive")
elif a<0:
    print("Negative")
else:
    print("Zero")
print()

#13
mark = 90

if mark>=90 and mark<=100:
    print("A grade")
elif mark>=75 and mark<=89:
    print("B grade")
elif mark>=50 and mark<=74:
    print("C grade")
else:
    print("Fail")
print()

#14
year =int(input("Enter a leap year :"))

if (year %400==0) or(year %4==0 and year%100!=0):
    print(year,"is a leap year")
else:
    print(year, "not leap year")

#15

age = int(input("Enter a age :"))

if age>=18:
    print("Eligiable for vote")
else:
    years_left = 18-age
    print(f"Not Eligiable. you wait for year {years_left} more year(s).")
print()

#16
a =18
b =28
c =29
print("The largest number of :", max(a,b,c)) 
print()

#17
num = int(input("Enter a number :"))

if num>0:
    print("The number is positive")
    if num%2==0:
        print("Even")
    else:
        print("Odd")
else:
    if num==0:
        print("The number is Zero")
    else:
        print("The number is negative")
print()


#18
age = 61
if age<13:
    print("child")
else:
    if age<=19:
        print("teen")
    else:
        if age<=59:
            print("Adult")
        else:
            if age>=60:
                print("Senior Citizen")
print()


#19
letter = input("Enter a letter :")

if letter in 'aeiouAEIOU':
    print("vomel")
elif letter.alpha():
    print("consonant")
else:
    print("Not a letter")
print()

#20
a =int(input("Enter a number :"))
b =int(input("Enter a number :"))
c =int(input("Enter a number :"))

avg =(a+b+c)/3

if a>=40 and b>=40 and c>=40:
    print("pass")
    if avg>=90:
        print("outstanding")
else:
    print("Fail")

               







