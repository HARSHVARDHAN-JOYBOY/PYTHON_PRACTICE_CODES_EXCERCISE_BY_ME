# Word Occurrence Comparator

# Problem Statement:
# Accept two paragraphs from the user and:

# Clean both texts (lowercase + remove punctuation)

# Store words in lists

# Find:

# Common words (use sets)

# Words unique to paragraph 1

# Words unique to paragraph 2

# Frequency of common words (use dictionary)

# Concepts practiced:
# Lists, Sets (intersection & difference), Dictionary, string methods, loops
import string

def clean(p1,p2):
    p_one=p1.lower().translate(p1.maketrans("","",string.punctuation)).split()
    p_two=p2.lower().translate(p2.maketrans("","",string.punctuation)).split()
    print(p_one,p_two)
    s1=set(p_one)
    s2=set(p_two)
    print(f"{s1} \n {s2}")
    print(f"Common words : {s1.intersection(s2)}")
    print(f"Unique words : {s1.symmetric_difference(s2)}")
    freq=dict()
    for word in zip(p_one,p_two):
        freq[word]=freq.get(word,0)+1




p1=input("Enter first paraghaph :")
p2=input("Enter second paraghaph :")

clean(p1,p2)
















