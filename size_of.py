import sys # system module 

x = 10
print("get size of",sys.getsizeof(x))

# Ref count
y = 1
print("get ref count of",sys.getrefcount(y)) # 112 ref count coz of behind the scene uses like interpreter.
