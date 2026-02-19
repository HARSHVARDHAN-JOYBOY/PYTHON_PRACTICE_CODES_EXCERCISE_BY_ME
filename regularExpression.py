import re
text="This is the simple text exmple for serching the word which can be found in different forms such as The THE tHE ThE thE tHe"

#  lets search the word using search method

match= re.search("the",text)
# print(match.start(),match.end())
# if match:
#     print("Match found!")
#     print("Starting index:",match.start())
#     print("Ending index:",match.end())

# lets found all occruences at once

# matchs= re.findall("the",text,re.IGNORECASE)#case insensitive search
# print("All Matches :",matchs)


# lets change the word by cat word using sub method

# matchess= re.sub("the","cat",text)
# print("New texts : ", matchess)
