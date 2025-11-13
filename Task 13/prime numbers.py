count=0
for num in range(2,101):
    for i in range(2,num):
        if num%i==0:
          break
    else:
        print(num)
        count+=1
print("Total all prime numbers :",count)

        
