# frozenset()
my_set = {1,2,3}
my_frozen_set = frozenset(my_set)
print(my_frozen_set)
print(type(my_frozen_set))

# ditionary - store key, value

student = {"roll-1":"Mg Mg","roll-2":"Kyaw Kyaw","roll-3":"Aung Aung"}
print(student.get("roll-1"))
student["roll-2"] = "Hla Mg" # change value
#student["roll-4"] = student.pop["roll-3"]
print(student)

d = {} # empty dictionary
d [1] = 'one'
d [2] = 'two'

# Input function
x = int(input("Enter x:")) # need Typecst because input value is string

x1,x2 = [int(i) for i in input("enter 2 input:").split(',')]

# Argument
'''def multiply (x,y):  # x,y is parameter
    print(x*y)
    multiply(3,4)    # 3,4 is argument'''

# Parameters are the values that are declared in the function.
# Arguments are the values that are  passed to the function when calling it.
# 
#Eval() consider input string as parameter. return as python codes
equation = input(" Enter the equation")
z = eval(equation)

# Enter two input in a single sentence
s1,s2 = [int(i) for i in input("Enter two inputs:").split(',')]
