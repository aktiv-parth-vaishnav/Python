# a)
a = 10
b = 20
print(a and b)  # 20
print(a or b)  # 10

# b)
if False:
    print("It is False")
else:
    print("It is True")  # It is True

# c)
if []:
    print("It is Blank")
else:
    print("It is Something else")  # It is Something else

# d)
if [[]]:
    print("It is Blank")
else:
    print("It is Something else")

# e)
if [ False ]:
    print("It is Blank")
else:
    print("It is Something else")

# f)
print(type(range))