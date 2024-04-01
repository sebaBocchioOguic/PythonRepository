# Sets Concepts in Python

# Sets are unordered structured of data
# You can't access values by using index, and is initialized by {}

language = {1,2,3}
language
#    {1, 2, 3}

language[0]
#    Traceback (most recent call last):
#      File "<pyshell#21>", line 1, in <module>
#        language[0]
#    TypeError: 'set' object is not subscriptable


# Sets can only storage unique values of any type of data
language2 = {1, 2.0, "text"}
language2
#    {1, 2.0, 'text'}


# Sets only accepts unique values
language3 = {1,2,3,3,3,4,4,5}
language3

#    {1, 2, 3, 4, 5}


# To add an element, you can use Add Function
language.add(4)
language

#    {1, 2, 3, 4}


# You also can add values using Update Function
language.update([4,5,6])
language

#    {1, 2, 3, 4, 5, 6}


# To obtain de amount of elements in Set, you can use Len Function
len(language)

#    6


# To delete an element, you can use Discard o Remove Function
language.discard(2)
language
#    {1, 3, 4, 5, 6}

language.remove(1)
language
#    {3, 4, 5, 6}


# To empty a Set, use Clear Function

language.clear()
language
#    set()
