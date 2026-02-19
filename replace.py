str1=input("Enter a String:")
print("Origina1 String:",str1)
char = str1[0]
str1 = str1.replace(char,'$')
str1 = char + str1[1:]
print("Replaced String:",str1)
