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


print("experts")