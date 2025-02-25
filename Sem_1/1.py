# Complex Numbers
# Definition: A complex number is a number that can be expressed in the form a + bj, where a and b are real numbers and j is the imaginary unit, satisfying j^2 = -1.
# Syntax: complex_number = a + bj
Complex = 2 + 3j
real = int(Complex.real)
imaginary = int(Complex.imag)
print(real)
print(imaginary)

# Tuples
# Definition: A tuple is a collection of objects that can be of any data type, including strings, integers, floats, and other tuples.
# Syntax: tuple_name = (element1, element2, ..., elementN)
tup = (1, 2, 'abc')
print(tup)
print(type(tup))

# Lists
# Definition: A list is a collection of objects that can be of any data type, including strings, integers, floats, and other lists.
# Syntax: list_name = [element1, element2, ..., elementN]
lis = [1, 2, 'tejas']
print(lis)
print(type(lis))

# Variable Assignment and Identity
# Definition: Variable assignment is the process of assigning a value to a variable.
# Syntax: variable_name = value
# Identity: In Python, the "is" operator checks if both variables point to the same object in memory.
X = 22
Y = X
print("X =", X, " Id of x is ", id(X), "\nY =", Y, " Id of y is ", id(Y))
Y = 21
print("X =", X, " Id of x is ", id(X), "\nY =", Y, " Id of y is ", id(Y))
Z = 22

# Membership Operator
# Definition: The membership operator checks if a value is present in a sequence (such as a list, tuple, or string).
# Syntax: value in sequence
x = [1, 2, 3, 4, 5]
print(10 not in x)
print(10 in x)
print("\n")

# Identity Operators
# Definition: The identity operators check if both variables point to the same object in memory.
# Syntax: variable1 is variable2
a = 1
b = a
c = 1
print(a is b)
print(a is not c)

# String Operations
# Definition: Strings are sequences of characters.
# Syntax: string_name = "string_value"
t = "I am Yash Borude"
print(t[-1:-16:-1])  # Reverse string
print(t[-11:-16:-1])  # Reverse string from index -11 to -16
print(t.capitalize())  # Capitalize the first letter
print(t.upper())  # Convert to uppercase
print(t.lower())  # Convert to lowercase
print(t)
print(len(t))  # Get the length of the string
E = t.split()  # Split the string into a list
print(E)
t = t.replace('Chaudhari', ' From Dharangaon')  # Replace a substring
print(t)

# File Operations
# Definition: File operations involve creating, opening, writing, reading, and closing files.
# Syntax:
#   - Create: file_name = open("file_name.txt", "w")
#   - Open: file_name = open("file_name.txt", "r")
#   - Write: file_name.write("content")
#   - Read: file_name.read()
#   - Close: file_name.close()
# Lifespan of file: When the file is created

# Error Handling in Python
# Definition: Error handling involves catching and handling exceptions that occur during the execution of a program.
# Syntax: try - except block
# Types of files:
#   - Standard input file: sys.stdin
#   - Standard output file: sys.stdout
#   - Standard error file: sys.stderr