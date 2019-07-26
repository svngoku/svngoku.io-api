import requests
import json

userame = 'Svngoku'
token = 'a65cdcc7c1325a529efbe1ae08e49473ff00326a'

gh_session = requests.Session()
gh_session.auth = (userame, token) 

repos_url = 'https://api.github.com/user/repos'
followers_url = 'https://api.github.com/user/followers'

# get list of my repos
repos = json.loads(gh_session.get(repos_url).text)

# 
followers = json.loads(gh_session.get(followers_url).text)
# print repo by names
def getRepoByName():
    # dict of repos
    repositories = []
    for repo in repos:
        repositories.append(repo['name'])
        
    return repositories


print(followers)

