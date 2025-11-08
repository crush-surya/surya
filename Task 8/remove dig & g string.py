s = input("Enter  a word :")
r=" "
for ch in s:
    if not ch.isdigit():
        r+=ch
print(r)
