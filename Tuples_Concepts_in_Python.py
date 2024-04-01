# Tuples Concepts in Python

# Very similar to Lists, but you can't modify the internal elements

# Tuples can be initialized with ()
languages = ("python", "c", "c++")

# Also Tuples can be initialized without (), because if you don't use (), [], or {} to initialize, Python will assume Tuple as the default
languages_2 = "java", "basic", "php"

# When you try to modify the value of an element inside the Tuple, you get an error
languages = ("python", "c", "c++")
languages
#    ('python', 'c', 'c++')

languages[0] = "css"
#    Traceback (most recent call last):
#    File "<pyshell#2>", line 1, in <module>
#    languages[0] = "css"
#    TypeError: 'tuple' object does not support item assignment


# The rest of functions are similar to Lists, so check the doc of Lists Concepts
