s = input("Enter a string :")
result ="".join([ch for ch in s if not ch.isdigit()])
print("without digits :",result)
