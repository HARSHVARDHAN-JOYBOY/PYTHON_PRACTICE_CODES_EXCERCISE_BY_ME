from collections import Counter

def rc(s):
    counter=Counter(s)
    repchar={char: count for char,count in counter.items() if count >1}
    return repchar

s="theharshvardhanisdtudentoftybca"
result=rc(s)

for char,count in result.items():
    print(f"{char}-{count}")
