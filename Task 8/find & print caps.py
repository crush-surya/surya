s=input("Enter a sentence :")
for word in s.split():
    if word[0].isupper():
        print(word)
