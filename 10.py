def square(num):
    result = num * num
    return result


a = square(4)
print(a)
square(10)


# b = int(input("enter amount of pets: "))
# if 0 < b < 4:
#     print("ok")
# else:
#     print("not ok")


def validate(prompt, low, high, ok, not_ok):
    input_from_user = int(input(prompt))
    if low < input_from_user < high:
        return ok
    else:
        return not_ok


print(validate("enter your age: ", 0, 120, "age is good", "age is bad"))
print(validate("enter amount of pets: ", 0, 4, "you are a good person", "you are a better person"))
