import requests

i = input('enter website with .com and without https')
#this requests.get will open the website 
response = requests.get('https://www.'+i)
#it checks status code 200 means ok 404 not found 

code = response.status_code

res = response.text

con = response.content

hed = response.headers

url = response.url

print('status code is:', code)

print('response is :',res)

print('contents are:',con)

print('headers are :',hed)

print(url)
#not for preffosonal programers and hackers 
# only for students 

