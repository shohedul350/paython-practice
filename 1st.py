# print
print("hello");

# condition
if 5 > 2:
 print("Five greater then two");
# variable
x = 5
y = "shohedul"
print(x)
print(y)

# multiline comments
"""
This is a comment
written in
"""

# types
a =  str(3)  # x will be '3'
b = int(3)    # y will be 3
c= float(3)    # z will be 3.0

print(a)
print(b)
print(c)

# multiples variables
d,e,f = "a", "b", "c"
print(d)
print(e)
print(f)


x1 = "Python"
y1 = "is"
z1 = "awesome"
print(x1, y1, z1)

# global variable
x2 = "awesome"
def myfunc():
  print("python is: " + x2)
myfunc()
print("python is: " + x2)

x3 = "Hello, World!"
print(x3[2:5])
print(x3[:5])
print(x3[2:])