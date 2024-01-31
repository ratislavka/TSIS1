###
print(10>9)
#true

###
print(10 == 9)
#false

###
print(10<9)
#false

###
print(bool("abc"))
#true

###
print(bool(0))
#false

###
print(10*5)

###
print(10/2)

### LISTS
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!"

###
if 5 != 10:
  print("5 and 10 is not equal")

###
if(5 == 10) or 4 == 4
  print("At least one  of the statement is true")

###
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

###
fruits[0] = "kiwi"

###
fruits.append("Orange")

###
fruits.insert(1, "lemon")

###
fruits.remove("banana")

###
print(fruits[-1])

###
print(fruits[2:5])

###
print(len(fruits))

###TUPLES
fruits = ("apple", "banana", "cherry")
print(fruits[0])

###
print(len(fruits))

###
print(fruits[-1])

###
print(fruits[2:5])

###SETS
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

###
fruits = {"apple", "banana", "cherry"}
fruits.add("Orange")

###
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

###
fruits = {"apple", "banana", "cherry"}
fruts.remove("banana")

###
fruits = {"apple", "banana", "cherry"}
fruts.discard("banana")

###DICTIONARIES
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(cat.get("model"))

###
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
###
  car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  car["year"] = 2020
  car["color"] = "red"

###
car.pop("model")

###
car.clear()

###IF .. ELSE
a = 50
b = 10
 if a > b:
  print("Hello World")

###
a = 50
b = 10
 if a != b:
  print("Hello World")

###
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

###
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")

###
if a == b and c == d:
    print("Hello")

###
if a == b or c == d:
  print("Hello")

###
if 5 > 2:
  print ("YES")

###
a = 2
b = 5
print("YES") if a == b else print("NO")

###
a = 2
b = 50
c = 2
if a == c or b == c:
  print("YES")

###
i = 1
while(i < 6):
  print(i)
  i += 1

###
i = 1
while(i < 6):
  if(i == 3)
    break
  i += 1

###
i = 1
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

###
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

###
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

###
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

###
for x in range(6):
  print(x)

###
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

###


