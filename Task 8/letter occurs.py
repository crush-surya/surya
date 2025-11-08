s = input("Enter a sentence: ")
s = s.replace(" ", "")   

for ch in s:
    if ch.isalpha():
        print(ch, "=", s.count(ch))




