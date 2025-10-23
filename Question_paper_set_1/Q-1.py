# 1. Expression evaluation
print([] * 3)
print(('a', 'b', 'c') * 2)
print((2) ** 2)
print([{}] * 2)
print({3:1} * 2)
# Error: unsupported operand type(s) for *: 'dict' and 'int'
print('123' + 2)
# Error: can only concatenate str (not "int") to str
print(['a', 'b', 'c'] + 'rf')
# Error: can only concatenate list (not "str") to list
print((2, 4) ** 2)
# Error: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'
Z = ['P', 'L', ']']
Z += 'SE'  # adds 'S' and 'E' as separate elements
print(Z)  # → ['P', 'L', ']', 'S', 'E']
