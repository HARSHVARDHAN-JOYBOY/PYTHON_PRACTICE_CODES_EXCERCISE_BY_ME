# <!-- Utilize Python's data structures and string manipulation functions to develop a program demonstrating proficiency in these concepts.

# Problem Statement
# Develop a Python program called Student Text Analyzer that demonstrates the use of Python data structures and string manipulation functions.

# The program should perform the following tasks:

# 1.Accept a paragraph of text from the user.

# 2.Clean the text by converting it to lowercase and removing punctuation.

# 3.Store all words in a suitable data structure.

# Display:

# 1.Total number of words

# 2.Unique words

# 3.Frequency of each word

# Identify:
# 1.The longest word

# 2.The shortest word

# The program should make effective use of: Lists, Sets, Dictionaries, String functions.

# Wtrite up Questions:

# 1. Discuss how Python data structures and built-in functions are utilized in the given program to analyze textual data.
# 2. Explain the role of lists, sets, and dictionaries in organizing the data, and describe the use of string functions such as lower(), replace(), and split(). Also explain how loops and functions like len(), max(), min() contribute to efficient text analysis. -->

import string

p1=input("Enter your full paragraph : ")
print(f"paragraph entered by you : {p1}")
# p1=paragraph.translate(paragraph.maketrans("","",string.punctuation))
for char in string.punctuation:
    p1=p1.replace(char, "")


print(f"After removing punctuation : {p1}")
p2=p1.lower().split()
print(f"After converting to lower case and spliting into list of words : {p2}")
print(f"Type of p2 is : {type(p2)}")

total_no_of_words=len(p2)
print(f"total number of words in paragraph : {total_no_of_words}")
unique=set(p2)
print(f"Unique Words : {unique}")
# print(len(unique))
freq=dict()
for word in p2:
    freq[word]=freq.get(word,0)+1
for key,val in freq.items():
    print(f"Total \'{key}\' are : {val} times in this String \n")
# print(freq)
longest=max(p2,key=lambda x:len(x))
shortest=min(p2,key=lambda x: len(x))
print(f"Longest word: \'{longest}\' \nShortest word : \'{shortest}\'")




