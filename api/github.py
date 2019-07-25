import requests
import json

userame = 'Svngoku'
token = 'ec9eaf66c1be2e1666d78d86ba51e6c92d67a026'

gh_session = requests.Session()
gh_session.auth = (userame, token) 

repos_url = 'https://api.github.com/user/repos'

# get list of my repos
repos = json.loads(gh_session.get(repos_url).text)

# print repo by names
def getRepoByName():
    # dict of repos
    repositories = []
    for repo in repos:
        repositories.append(repo['name'])
        
    return repositories


