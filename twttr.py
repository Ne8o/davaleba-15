#list for volwels
vowels = ["a", "A", "E", "e", "I", "i", "o", "O", "u", "U"]
#input txt
txt = input("input: ")
txt1 = ""
#find and remove vowels
for char in txt:
    if char not in vowels:
        txt1 += char
print("output:", txt1)




