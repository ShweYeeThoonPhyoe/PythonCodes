"""
interger
"""

num_in_dec = 23 #literal or immediate value
print(num_in_dec)

num_in_bin = 0b10 #2
print(num_in_bin)

num_in_oct = 0O17 #15
print("Num in Octal", num_in_oct)

num_in_hexa = 0X10 #16
print("Num in Hexadecimal", num_in_hexa)

print("32 in hexa", hex(32)) #0x20

x= 0x20 #32
y= 0o40 #32
print("x+y", x+y)

"""
Floating point number
"""
my_float = 1.1e2
print ("my float",my_float, type(my_float))

my_float = 0.0
print("my float",my_float) # +0.0 due to float representation

my_float = -0.0
print("my float", my_float) # -0.0 due to float represntation

"""
In Python, the data type of zero is assigned in three types: 0 (int), +0.0, -0.0.
"""
flag = True
print("flag is",flag)

x = 10
print("x + flag", x + flag)

my_str = 'Hello "How are you" I\'am fine' #single line string single quote or doule quote
my_str = '''This is mutli-line string
Another line''' # multi-line string ''' or """

my_str2 = "Hello \"How are you\" I'm fine"

# Type Casting
my_num = 10
my_string = '123'
print("my num + my string", int(my_string) + my_num) # int()

# To see memory address of var 
x = 10
y = 20

print("ID of x",hex(id(x)))
print("ID of y",hex(id(y)))

# To check variables are in same memory location, use API "is"
print("x is y", x is y)

# Bytes Data Types: bytes(var_name). permitted value are 0~255.
x = [0,10,25,200]
my_bytes = bytes(x)
print("my bytes", my_bytes)
print("type my bytes", type(my_bytes))
print(my_bytes[1]) # cannot mutate

# Bytes Array Data Type: bytearray()  CAN MUTATE

x = [3,6,8,10]
my_bytes_array = bytearray(x)
my_bytes_array[0] = 1

# List [] (1.2.2021) a collection of varaibles in a linear form (mutable)
ages = [12,7,21,33,44]
print("sum of ages",sum(ages))
print("average",sum(ages)/len(ages)) #list.append list.remove

# Tuple () # immutable and used only for read only purpose. can't store numerous items.
ages = (0,10)
print(len(ages))
print(type(ages))

# range() range(start,end,increment)
x = range(3,7)
for i in x:
    print(i)

# Set {}   sets are mutable but the elements contains in sets must be of an immutable type
# Tuple(immutable) can be set elements but list and dict (mutable) cannot be.

s = 'Hello'
list(s)
set(s)

# two set definition
set("foo") # {'f','o'}
x = {"foo"} # {"foo"}
x = {12,"foo",3.12,(1,2,3)} 
x.add()
x.remove()



