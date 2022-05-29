isTrue = False
a = 2
b = 2
c = [1, 2, 3]
d = [1, 2, 3]
strOne = "One"
strThree = "Three"
my_names = ["adi", "ben", "noam", "arthur", "ron"]
my_list = []
age = int(input("enter your age: "))

if a == b:
    print("a equal b")
if c == d:
    print("c equal d")
if a is b:
    print("a is b")
if c is d:
    print("c is d")

#-----------------------------------------------------

if my_list:
    print("my_list is not empty")
if my_names:
    print("my_names is not empty")
if len(my_names) > 2:
    print("i remember enough names")
if 0 < age < 120:
    print("ok")

#-----------------------------------------------------

if a < b and strThree == 3 or isTrue == 4:
    print("a is less than b")
elif a == b:
    print("a is equal b")
elif strOne != strThree:
    print("hello")
else:
    print("a is greater than b")

#-----------------------------------------------------

if a < b and not (strThree == 3 or isTrue == 4):
    print("a is less than b")
elif a == b:
    print("a is equal b")
elif strOne != strThree:
    print("hello")
else:
    print("a is greater than b")

#-----------------------------------------------------

if "zohar" in my_names:
    print("found it!")
else:
    print("not found!")

#-----------------------------------------------------

a = "hello world"
print(list(range(1, 10, 3)))
for i in range(1, 6):
    print(f"hello #{i}")

my_names = ["adi", "ben", "noam", "arthur", "ron"]
for name in my_names:
    print(f"hello {name}")
    if name == "arthur":
        break
else:
    print("printed all names")
#-----------------------------------------------------

for i in range(len(my_names)):
    print(my_names[i])

a = 0
while a < 5:
    print(a)
    a = a + 1
    if a == 2:
        continue


l = []
current_input = input("enter letter: ")
while current_input != "q":
    l.append(current_input)
    current_input = input("enter letter: ")
print(f"input are {l}")

n = [1, 2, 3, 4, 5]
result = [num * 2 for num in n]
for num in n:
    if num > 2:
        result.append(num * 2)
        print(result)

for i in range(1, 101):
    if i % 7 != 0 and "7" not in str(i):
        print(i)












































