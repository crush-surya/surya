u =int(input("Enter a units :"))
if u <=100:
    b = u *1.5
elif u <=200:
    b = u*1.5+(u - 100)*2.5
elif u <=300:
    b = 100 * 1.5 +100*2.5+(u -200)*4.0
else:
    b =100*1.5 +100*2.5+100*4.0+(u -300)*5.0
if b>1000:
    b+=b*0.10
print("Total electicity bill =",b)
