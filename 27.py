import requests
response = requests.get("https://api.github.com/users/avielb/repos")

repos_list = response.json()
print(repos_list[0].keys())
for repo in repos_list:
    print(repo["name"])










