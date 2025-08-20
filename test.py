
# -------------------------------
# 1. Variables
# -------------------------------
x = 10          # integer variable
name = "Siva"   # string variable
pi = 3.1415     # float variable
is_dev = True   # boolean variable

print("Variables:", x, name, pi, is_dev)


# -------------------------------
# 2. Data Types
# -------------------------------
a_int = 100                # int
a_float = 10.5             # float
a_str = "Python"           # str
a_bool = False             # bool
a_list = [1, 2, 3, "hi"]   # list
a_tuple = (10, 20, 30)     # tuple
a_set = {1, 2, 3, 3}       # set (removes duplicates)
a_dict = {"key": "value"}  # dictionary

print("Data types:")
print(type(a_int), type(a_float), type(a_str), type(a_bool))
print(type(a_list), type(a_tuple), type(a_set), type(a_dict))


# -------------------------------
# 3. Operators
# -------------------------------

# 3a. Arithmetic Operators
print("\nArithmetic Operators:")
print("10 + 5 =", 10 + 5)
print("10 - 5 =", 10 - 5)
print("10 * 5 =", 10 * 5)
print("10 / 3 =", 10 / 3)   # float division
print("10 // 3 =", 10 // 3) # floor division
print("10 % 3 =", 10 % 3)   # modulus
print("2 ** 3 =", 2 ** 3)   # exponentiation

# 3b. Relational Operators
print("\nRelational Operators:")
print("10 > 5:", 10 > 5)
print("10 < 5:", 10 < 5)
print("10 == 10:", 10 == 10)
print("10 != 5:", 10 != 5)

# 3c. Logical Operators
print("\nLogical Operators:")
print("True and False:", True and False)
print("True or False:", True or False)
print("not True:", not True)


# -------------------------------
# 4. Python Tokens
# -------------------------------
# Keywords (reserved words like if, else, for, while, def, return)
# Identifiers (user-defined names like x, name, my_function)
# Literals (values like 10, "Hello", 3.14, True)
# Operators (+, -, *, /, etc.)

# Example:
if x > 5:   # 'if' is keyword, x is identifier, 5 is literal, '>' is operator
    print("\nPython Tokens Example: x is greater than 5")


# -------------------------------
# 5. Strings
# -------------------------------
my_string = "Hello Python"
print("\nStrings:")
print(my_string)
print("First character:", my_string[0])
print("Substring [0:5]:", my_string[0:5])
print("Last character:", my_string[-1])


# -------------------------------
# 6. String Functions
# -------------------------------
print("\nString Functions:")
print("Length:", len(my_string))
print("Lowercase:", my_string.lower())
print("Uppercase:", my_string.upper())
print("Title Case:", my_string.title())
print("Replace:", my_string.replace("Python", "World"))
print("Split:", my_string.split(" "))
print("Join:", "-".join(["Python", "Rocks"]))
print("Find:", my_string.find("Python"))
print("Count 'l':", my_string.count("l"))
print("Starts with 'Hello':", my_string.startswith("Hello"))
print("Ends with 'Python':", my_string.endswith("Python"))


# -------------------------------
# 1. Variables (extra concepts)
# -------------------------------
print("\nExtra Variable Concepts:")
a, b, c = 1, 2, 3   # multiple assignment
print("Multiple assignment:", a, b, c)

x = 10
print("Before type change:", x, type(x))
x = "Now I'm a string"  # dynamic typing
print("After type change:", x, type(x))

global_var = "I am global"
def demo_scope():
    local_var = "I am local"
    print("Inside function:", global_var, local_var)
demo_scope()


# -------------------------------
# 2. Data Types (extra concepts)
# -------------------------------
none_type = None
complex_num = 3 + 4j

print("\nExtra Data Types:")
print("NoneType:", none_type, type(none_type))
print("Complex:", complex_num, type(complex_num))

# Type casting
num_str = "100"
print("Casting str to int:", int(num_str))
print("Casting int to str:", str(123))
print("Casting string to list:", list("abc","hello"))


# -------------------------------
# 3. Operators (extra concepts)
# -------------------------------

# Assignment operators
x = 5
x += 3  # x = x + 3
print("\nAssignment Operator (+=):", x)

# Membership operators
print("Membership Operator:")
print("'a' in 'cat':", 'a' in 'cat')
print("5 not in [1,2,3]:", 5 not in [1,2,3])

# Identity operators
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print("\nIdentity Operator:")
print("list1 is list2:", list1 is list2)     # same object
print("list1 == list3:", list1 == list3)     # same value
print("list1 is list3:", list1 is list3)     # different objects


# -------------------------------
# 4. Python Tokens (extra)
# -------------------------------

# Comments
# This is a single-line comment
"""
This is a multi-line
comment in Python
"""

# Indentation (Python enforces indentation instead of {} )
for i in range(3):
    print("Indented loop:", i)


# -------------------------------
# 5. Strings (extra concepts)
# -------------------------------
print("\nExtra String Concepts:")
# Escape characters
# \n = newline → moves text to the next line
print("Line1\nLine2")   
# \t = tab space → inserts horizontal spacing
# (\t) = 8 spaces in standard Python output
print("Tab\tSpace")     

# Raw string
# Prefixing with r"..." tells Python NOT to treat backslashes as escape sequences
# Useful for file paths, regex, etc.
print(r"Raw string: C:\new_folder\test")   
# f-strings (formatted strings)
# Allow embedding variables and expressions directly inside {} brackets
name = "Siva"
print(f"Hello {name}, 2+3={2+3}")   # Inserts value of variable & evaluates expression

# -------------------------------
# 6. String Functions (extra)
# -------------------------------
# Sample string with leading and trailing spaces
sample = "   Python123   "  
print("\nExtra String Functions:")

# Removes whitespace from both ends of string
print("Strip:", sample.strip())        
# Removes whitespace only from the left side
print("LStrip:", sample.lstrip())      
# Removes whitespace only from the right side
print("RStrip:", sample.rstrip())      

# Checks if all characters are letters or digits (Alphanumeric)
print("isalnum:", "Python123".isalnum())   # True → contains only letters+numbers
# Checks if all characters are alphabetic
print("isalpha:", "Python".isalpha())      # True → only letters
# Checks if all characters are digits
print("isdigit:", "12345".isdigit())       # True → only numbers
# Checks if all characters are spaces
print("isspace:", "   ".isspace())         # True → only spaces
# Pads the number with zeros on the left, until string becomes length 5
print("zfill:", "42".zfill(5))             # Output: 00042

