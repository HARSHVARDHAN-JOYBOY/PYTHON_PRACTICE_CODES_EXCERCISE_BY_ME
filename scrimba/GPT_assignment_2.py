# 2️⃣ Character Frequency Analyzer

# Problem Statement:
# Accept a sentence and:

# Remove spaces

# Convert to lowercase

# Count frequency of each character

# Display:

# Total characters

# Unique characters

# Most frequent character

# Least frequent character

# Hint:
# Use:

# replace() to remove spaces

# dict.get() for counting

# max(freq, key=freq.get)

# Concepts practiced:
# Dictionary counting, string manipulation, max() with key

from collections import defaultdict

class CFA:
    def __init__(self,p1):
        self.__p1=p1
    def Character_Frequency_Analyzer(self):
        p_s=self.__p1.lower().strip()
        p_one=p_s.split()#replace(" ","")
        print(p_one)

        freq=defaultdict(int)
        for word in p_one:
            freq[word]+=1
        print(f"Frequencies : {freq.items()}")



p1=input("Enter a paragraph : ")

s1=CFA(p1)
s1.Character_Frequency_Analyzer()
# d = {"a": None}
# print(d.get("a", 5))
