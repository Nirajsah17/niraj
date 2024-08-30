import sys
# Integer
x = 10
print(type(x))  # Output: <class 'int'>

# Float
y = 3.14
print(type(y))  # Output: <class 'float'>

# Complex
z = 2 + 3j
print(type(z))  # Output: <class 'complex'>

# Big Integer
a = 123456789012345678901234567890
print(type(a))  # Output: <class 'int'>

# Big Float
b = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
print(type(b))  # Output: <class 'float'>

print(sys.getsizeof(x))  # Output: 28
print(sys.getsizeof(y))  # Output: 24
print(sys.getsizeof(z))  # Output: 32
