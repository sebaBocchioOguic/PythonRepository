# Dictionaries Concepts in Python

# Dictionaries storage data in couples of {key: value}

# To initialize a Dictionary you have to use {} setting key: value, and separate the couples with commas
language = {
    "name": "python",
    "dev": "Sebastian"
}

language
#>>> {'name': 'python', 'dev': 'Sebastian'}

# You can't use indexes to access data in Dictionaries. Instead you have to use the key-name
#>>> language[0]
#    Traceback (most recent call last):
#      File "<pyshell#10>", line 1, in <module>
#      language[0]
#    KeyError: 0

#>>> language["name"]
#    'python'


# To add new data, just set using the new key-name between []

language["year"] = 2010
language
#    {'name': 'python', 'dev': 'Sebastian', 'year': 2010}


# You can't store two values with the same key-name

# You can also store a List (or another structure) into a Dictionary

language["description"] = ["easy", "fast", "fun"]
language
#    {'name': 'python', 'dev': 'Sebastian', 'year': 2010, 'description': ['easy', 'fast', 'fun']}


# To access data you can use reserved word ITEMS, and you'll get the store of the Dictionary in a group of Tuples

language.items()
#    dict_items([('name', 'python'), ('dev', 'Sebastian'), ('year', 2010), ('description', ['easy', 'fast', 'fun'])])

# Keys will return the list of the keys of the Dictionary

language.keys()
#    dict_keys(['name', 'dev', 'year', 'description'])

# Values will do the same but with the values of the Dictionary

language.values()
#    dict_values(['python', 'Sebastian', 2010, ['easy', 'fast', 'fun']])
