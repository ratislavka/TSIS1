#1
print('Hello')
#2
if 5 > 2:
    print("YES")
#3
 #This is a comment
#4
'''
This is a comment
written in 
more than just one line
'''
#5
carname = 'Volvo'
#6
x=50
#7
x=5
y=10
print(x+y)
#8
x=5
y=10
z=x+y
print(z)
#9
x,y,z = 'Orange', "Banana", "Cherry"
#10
x = y = z = "Orange"
#11
def myfunc():
  global x
  x = "fantastic"
#12
x = 5
print(type(x))
#int

#13
x = "Hello World"
print(type(x))
#str

#14
x = 20.5
print(type(x))
#float

#15
x = ["apple", "banana", "cherry"]
print(type(x))
#list

#16
x = ("apple", "banana", "cherry")
print(type(x))
#tuple

#17
x = {"name" : "John", "age" : 36}
print(type(x))
#dict

#18
x = True
print(type(x))
#bool

#19
x=5
x=float(x)

#20
x=5.5
x=int(5.5)

#21
x=5
x=complex(x)

#22
x = "Hello World"
print(len(x))

#23
txt = "Hello World"
x = txt[0]

#24
txt = "Hello World"
x = txt[2:5]

#25
txt = "Hello World"
x = txt.strip()

#26
txt = "Hello World"
txt = txt.upper()

#27
txt = "Hello World"
txt = txt.lower()

#28
txt = "Hello World"
txt = txt.replace("H", "J")

#29
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
