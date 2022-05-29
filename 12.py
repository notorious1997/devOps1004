# my_file = open("urls.txt")
# for line in my_file.readlines():
#     print(line, end="")


# my_file = open("name.txt", "w")
# for i in range(5):
#     current_name = input("enter your name: ")
#     my_file.write(f"{current_name}\n")
# my_file.close()


import requests
def save_name():
    n = input("put your name: ")
    my_file = open("names.txt", "a")
    my_file.write(f"{n}\n")

def show_names():
    with open("names.txt") as my_file:
        for line in my_file.readlines():
            print(f"hello {line}", end='')

def url_caller(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is ok")

def call_urls():
    with open("urls.txt") as urls:
        for line in urls.readlines():
            url_caller(line.strip())





