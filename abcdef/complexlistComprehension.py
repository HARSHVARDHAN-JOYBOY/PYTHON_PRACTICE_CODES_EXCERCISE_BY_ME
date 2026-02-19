# Complex list Comprehension
# Given a list of words, return a dictionary with each word as a key and its length as value, but only for words longer than 4 characters.

words=list(input("Enter words by seperating with Space  [____] : ").split())

WORDSwithLENGTHS= {word: len(word)for word in words if len(word)>4}

print(WORDSwithLENGTHS)

