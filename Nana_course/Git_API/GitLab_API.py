import requests

# look here for doc: https://docs.gitlab.com/ee/api/README.html

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
# print(response.json())

my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['http_url_to_repo']}\n")