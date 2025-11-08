s = input("Enter a sentence: ")

pun = ".,!?;:-'\"()[]{}"
result = ""

for ch in s:
    if ch not in pun:
        result += ch
print(result)
