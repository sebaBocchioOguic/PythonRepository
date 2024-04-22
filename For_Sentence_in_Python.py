# For Iteration in Python

# There are two types of Iterations in Python: For and While

# FOR Sentence  
# for <element> in <object>:
# The object can be a List, Tuple, Dictionary or Set Structure
# Also you can iterate into String Objects


# A String can be iterated as a List, where each character is an element of the List

text = "This is a Text letter by letter"

for letter in text:
    print(letter)

print(" - - - - ")

languageList = ["python", "java", "golang"]
for element in languageList:
    print(element)

# Break Sentence allows to finish the cycle
for element in languageList:
    print(element)
    if element == "java":
        break

# Continue Sentence allows to continue to the next element
for element in languageList:
    if element == "java":
        continue
    print(element)



# Range Sentence can return all the elements in a Numeric List until the number into the parameter (exluding this lastone)

for element in range(5):
    print(element)

for element in range(2, 5):
    print(element)


# To use a For Sentence in Lists in Python, you can use index with Range function

for index in range(len(languageList)):
    print("Index", index)
    print("Value", languageList[index])
