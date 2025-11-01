temperature =int(input("enter a temperature"))

if temperature>=30:
    message =("HOT")
elif temperature<30:
    message=("WARM")
elif temperature<20:
    message=("cool")
else:
    message=("cold")

print("the weather is" ,message)

num =int(input("enter a number :"))

if num >90:
    print("A grade")
elif num>75:
    print("B grade")
elif num>55:
    print("C grade")
elif num>40:
    print("D grade")
else:
    print("fail")

char =input("enter a single character")
if char.isalpha():
    print("This char alpha")
elif char.isdigit():
    print("This is digit")
else:
    print("single character")


day =int(input("enter a number :"))

if day==1:
    print("sunday")
elif day==2:
    print("monday")
elif day==3:
    print("tuesday")
elif day==4:
    print("wednesday")
elif day==5:
    print("thursday")
elif day==6:
    print("friday")
elif day==7:
    print("saturday")
else:
    print("invaild in a number")


age =int(input("Enter a age :"))
exp =input("work experience? (yes/no): ").strip().lower()

if age>=18 and exp =="yes":
    print("Eligiable")
else:
    print("not eligiable")
               
a =int(input("Enter a number :"))
b =int(input("Enter a number :"))
c =int(input("Enter a number :"))

if a>b and a>c :
    print("number a is largest")
elif b>a and b>c :
    print("number b is largest")
else:
    print("number c is largest")


a=int(input("enter a number :"))
b=int(input("enter a number :"))

if a>b:
    print("A number is largest")
elif b>a:
    print("B number is largest")
else:
    print("number is equal")


year =int(input("Enter a leap year :"))

if year %4==0:
    print(year,"is a leap year")
else:
    print(year, "not leap year")

login_name ="surya"
login_password ="2003"

username =input("enter a login_name :")

if username ==login_name:
    password =input("Enter a password :")
    if password==login_password:
        print("Login successful,",login_name)
    else:
        print("incorrect")
else:
    print("username not found")

num = int(input("enter a number : "))

if num%2==0:
    print("number is even")
else :
    print("number is odd")
num = int(input("enter a number : "))

mark =int(input("Enter a mark :"))

if  mark>=40:
    print("pass")
else:
    print("fail")

age =int(input("enter a number :"))

if age>=18:
    print("You eligiable for vote")
else:
    print("niot eligiable")


num =int(input("Enter a number :"))

if num>0:
         if num%2==0:
            print("the weather is positive,is even")
         else:
            print("the eather is positive,not even")
else:
    print("the num is not positive")


mark =int(input("Enter a mark :"))
attendance =int(input("Enter a attendance :"))

if mark>85 and attendance>90:
    print("Student qualifies for a scholarship")
else:
    print("not qualifies")


age =int(input("enter a number :"))

if age>=18:
    print("You eligiable for vote")
else:
    print("not eligiable")


