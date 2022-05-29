from datetime import datetime
import requests

def url_caller(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is ok")


for url in ["http://github.com",
            "http://google.com",
            "http://moshe.com"]:
    url_caller(url)

















































