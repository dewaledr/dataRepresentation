import requests
import json
from github import Github

g = Github("da42a72bfa816f16ea6df0a84e5dcb9646073f48")  #dewale
repo = g.get_repo("dewaledr/aPrivateOne")
# print("Repo is cloned as: ")
# print(repo.clone_url)
fileInfo = repo.get_contents("testPkg.txt")
urlOfFile = fileInfo.download_url
# print(urlOfFile)
response = requests.get(urlOfFile)
contentOfFile = response.text
print(contentOfFile)
newContentOfFile = contentOfFile +  "\nAdditional input from python...\nprint('Amazing stuff')"
#print(newContentOfFile)

# update
# repo.update_file("/your_file.txt", "your_commit_message", "your_new_file_content", file.sha)
gitHubResponse = repo.update_file(fileInfo.path, "updated by FA", newContentOfFile, fileInfo.sha)
print(gitHubResponse)
