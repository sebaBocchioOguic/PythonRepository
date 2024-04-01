# Conditional Sentences in Python

# Logical Conditionals

# == Equal
# != Different
# > Mayor than
# < Minor than
# >= Mayor or equal than
# <= Minor or equal tham

# is - it compares if the variables are the same obkject
# and - returns true if all conditions are true
# or - returns true if any of the conditions are true
# not - it verifies if an element doesn't pass some condition

# IF Sentence
# if <condition>:
#    If Block
# elif <condition>:
#    Elif Block
# else <condition>:
#    Else Block

a = 10
b = 20

if a > b:
    print("A es mayor a B")
elif a == b:
    print("A es igual a B")
else:
    print("A es menor a B")

c = True
if c:
    print("C es Verdadero")
else:
    print("C es Falso")


if type(c) is bool:
    print("C es Booleano")
else:
    print("C no es Booleano")


d = 10
e = 5
f = 1
if d > e and e > f:
    print("Las condiciones son Verdaderas")
else:
    print("Alguna de las condiciones no es verdadera")

