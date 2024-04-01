# Lists Concepts in Python

# Lists can be initialized with []
languages = ["python", "java", "golang"]

#>>>languages = ["python", "java", "golang"]
#>>>languages
#   ['python', 'java', 'golang']


# They may contain any kind of type of data, and repeat vaules
anyData = [1, 2.0, True, "python", 1]

#>>>anyData = [1, 2.0, True, "python", 1]
#>>>anyData
#   [1, 2.0, True, 'python', 1]


# Lists can be accesed by index starting by 0 or even using negative numbers
languages[0]

#>>>languages[0]
#   'python'

languages[-1]
#>>>languages[-1]
#   'golang'


# Also multiple and continuos values can be accesed setting the starting index and the final index, excluding the lastone

anyData[1:2]
#   [2.0]
anyData[0:2]
#   [1, 2.0]
anyData[1:3]
#   [2.0, True]
anyData[0:1]
#   [1]
anyData[0:0]
#   []


# Lists can contain another Lists inside

develop = [languages, "learning", "practice"]

#>>>develop = [languages, "learning", "practice"]
#>>>develop
#   [['python', 'java', 'golang'], 'learning', 'practice']

# Also Lists in Lists can de accesed with multiples[][]

develop[0][1]

#>>>develop[0][1]
#   'java'


# Values in Lists can be modified just setting the new value

languages[0] = "php"

#>>>languages[0] = "php"
#>>>languages[0]
#   'php'


# Lists accept new values at the end using Append Function

languages.append("python")

#>>>languages.append("python")
#>>>languages
#   ['php', 'java', 'golang', 'python']


# To concatenate two Lists just use the Entend Function

otherLanguages = ["c", "c++"]
languages.extend(otherLanguages)

#>>>otherLanguages = ["c", "c++"]
#>>>languages.extend(otherLanguages)
#>>>languages
#   ['php', 'java', 'golang', 'python', 'c', 'c++']
