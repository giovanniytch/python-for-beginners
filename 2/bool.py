python = True
java = False

print(f'is python great?\n- {python}')
print(f'is java great?\n- {java}')

print(type(python))
print(type(java))

# primary operations:
# - Boolean AND: and
# - Boolean OR: or
# - Boolean NOT: not

# and
print(f'False and False is {False and False}')
print(f'False and True is {False and True}')
print(f'True and False is {True and False}')
print(f'True and True is {True and True}')

# or
print(f'False or False is {False or False}')
print(f'False or True is {False or True}')
print(f'True or False is {True or False}')
print(f'True or True is {True or True}')

# not
print(f'not False is {not False}')
print(f'not True is {not True}')

# secondary operations:
# - Boolean XOR: xor
# - Boolean EQUIVALENCE: equiv
# - Boolean IMPLICATION: imply

# xor
print(f'False xor False is {(False or False) and not (False and False)}')
print(f'False xor True is {(False or True) and not (False and True)}')
print(f'True xor False is {(True or False) and not (True and False)}')
print(f'True xor True is {(True or True) and not (True and True)}')

# equiv
print(f'False equiv False is {not ((False or False) and not (False and False))}')
print(f'False equiv True is {not ((False or True) and not (False and True))}')
print(f'True equiv False is {not ((True or False) and not (True and False))}')
print(f'True equiv True is {not ((True or True) and not (True and True))}')

# imply
print(f'False imply False is {not False or False}')
print(f'False imply True is {not False or True}')
print(f'True imply False is {not True or False}')
print(f'True imply True is {not True or True}')
