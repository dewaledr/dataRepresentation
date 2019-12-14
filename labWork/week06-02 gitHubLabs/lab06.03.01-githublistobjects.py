from github import Github

#g = Github("b55d312da577ba479f7dc4f8f3f5b1384bdf3b2e")
g = Github("da42a72bfa816f16ea6df0a84e5dcb9646073f48")
for repo in g.get_user().get_repos():
    print(repo.name)