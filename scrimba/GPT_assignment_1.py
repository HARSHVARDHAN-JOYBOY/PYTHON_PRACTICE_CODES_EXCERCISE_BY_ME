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
    p_one=p1.lower().translate(str.maketrans("","",string.punctuation)).split()
    p_two=p2.lower().translate(str.maketrans("","",string.punctuation)).split()
    print(p_one,p_two)
    s1=set(p_one)
    s2=set(p_two)
    # print(f"{s1} \n {s2}")
    intsec=s1.intersection(s2)
    print(f"Common words : {intsec}")
    print(f"Unique words : {s1.symmetric_difference(s2)}")
    freq=dict()
    for word in p_one+p_two:
        freq[word]=freq.get(word,0)+1
    print(freq)
    print(f"Words unique to paragraph 1: {s1-s2}")
    print(f"Words unique to paragraph 2: {s2-s1}")
    commonfreq=dict()
    for word in p_one+p_two:
        if word in intsec:
            commonfreq[word]=commonfreq.get(word,0)+1
    print(f"Common word frequency : {commonfreq.items()}")

p1=input("Enter first paraghaph :")
p2=input("Enter second paraghaph :")

clean(p1,p2)
















