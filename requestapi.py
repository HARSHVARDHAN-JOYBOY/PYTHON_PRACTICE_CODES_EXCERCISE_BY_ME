import requests

r = requests.get('https://api.github.com/users/HARSHVARDHAN-JOYBOY')

# print(r.text)
with open("requestapitextonline.txt",'w') as f:
    f.write(r.text)





