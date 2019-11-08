# f = open("../week05-Curl-Ajax-Flask/carFA.html", "r")
# html = f.read()
# print(html)


#2 use the html2pdf.app api with key
import requests
import json

f = open("../week05-Curl-Ajax-Flask/carFA.html", "r")
html = f.read()
# print(html)
apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
url = 'https://api.html2pdf.app/v1/generate'

data = {'html': html, 'apiKey':apiKey}
response = requests.post(url, json=data)
print(response.status_code)
print("1...")
print(response.content)
print("2...")


# 3 modify the pgm above to write the binary data returned to a fille .pdf
newFile = open("lab06.02.01.htmlaspdf.pdf","wb")
print("3...")
newFile.write(response.content)
print("4...")

# use curl
# curl -i -H "Authorization: token f59b1cdb743ce0ab9b21a94ac246b02f06ee2d85" https://api.github.com/user/repos/datarepresentationstudents/aPrivateOne