# Print Values
print("Hello World")
print("How are You")
print("My name is Syed Huzaifa Zaidi")

# Assign and Print Value
_a = 10
b = 15
print("Sum of a and b is = ", (_a))
print(type(_a))

# Find Type of Variable
age = '''23'''
old = False
a = None
print(type(age))
print(type(old))
print(type(a))

# Print Sum
a = 2
b = 16
sum = a + b
print(sum)

"""Arithmetic Operators"""

a = 2
b = 4
sum = a + b
diff = a - b
divide = a / b
multiply = a * b
module = a % b # To find Reminider
power = a ** b # its like that a^b
print("Sum is = ",sum)
print("diff is = ",diff)
print("divide is =",divide)
print("multiply is = ",multiply)
print("module is = ",module)
print("power is = ", power)

# Relational Operator

a = 50
b = 20

print(a == b) # False
print(a != b) # True
print(a > b) # True
print(a >= b) # True
print(a < b) # False
print(a <= b) # False

# Assignment Operator
num = 10
#num += 10 # num = num + 10
#num -= 10 # num = num - 10
#num *= 10 # num = num * 10
#num /= 10 # num = num / 10
#num %= 10 # num = num % 10
num **= 10 # num = num ** 10
print("num : ",num)

# Logical Operator

# not operator convert True into False and False into True

num1 = True
num2 = False
print(not num1) # False
print(not num2) # True

# and Operator Both must be True otherwise answer is False

num1 = True
num2 = True
a = 20 
b = 10
print(num1 and num2)
print((a > b) and (a < b))

# or Operator one at least be True and if both False than answer is False

num1 = False
num2 = False
a = 20 
b = 10
print(num1 or num2)
print((a > b) or (a < b))

# Type Conversion
#float is superior they convert int into float automatically converter
a = 2 
b = 4.25
sum = a + b # 2.0 + 4.25 = 6.25
print(sum)

# Type Casting  Only Number not Name
# Manually converter int(value) , float(value)
a = "2"
b = "4" # string value
c = 3.14 # Float value convert into String value
d = int("4") # string convert into int value
e = float("2") # string convert into float value
f = str(c) # float convert into string value

print(type(f))
print(c + d)

# Take Input from User

name = input("Enter your Name here: ") # always give string value 
#even decimal and float
print("Welcome ", name)

num = int(input("Enter your age: "))
print("Your age is: ",num)

num1 = int(input("Enter int value: "))
num2 = float(input("Enter float value: "))
sum = num1 + num2
print(sum)
print(type(num1))
print(type(num2))