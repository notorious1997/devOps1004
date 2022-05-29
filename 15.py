# def get_age():
#     age = int(input("put your age: "))
#     if age < 0:
#         raise ValueError("age can not be negative")
#
# try:
#     get_age()
# except ValueError as e:
#     print(e.args)
#


# a = input("enter number: ")
# def check_number(num):
#     a = ""
#     try:
#         a = int(num)
#     except ValueError
#         return False
#     if str(num).isdigit() and str(num).isdecimal():
#         return True
#     return False


import requests
try:
    requests.get("http://qjwerhnjqwkhrekqwrjqwkjrkqwrjqwkrjqkrjqkerjhqkern.com")
except requests.exceptions.HTTPError:
    print("mission schema in url")
except requests.exceptions.InvalidURL:
    print("invalid url")














