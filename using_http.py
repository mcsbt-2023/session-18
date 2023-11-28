#%%

import requests

response = requests.get("http://wikipedia.org")

print(response.text)
# %%

import requests

response = requests.get('https://swapi.dev/api/starships/9')

json = response.json()

for film in json["films"]:
    print(film)








# %%

import requests

response = requests.get("https://api.github.com/orgs/mcsbt-2023/repos")

parsed_response = response.json()

for repo in parsed_response:
    print(repo["name"])
# %%
