import requests
from bs4 import BeautifulSoup
import os
import urllib
import urllib.request

# Set Query | In future use Arg arse
query = "pepsi"

# Set URL to google search
url =  f"https://www.google.co.in/search?q={query}&source=lnms&tbm=isch"
img_num = 1

r = requests.get(url)
soup = BeautifulSoup(r.content)
tags=soup.findAll('img')

for image in tags:
    #print image source
    img_url = image['src']
    img = requests.get(img_url, timeout=30)
    print(image['src'])
    p = os.path.join(f"output/{img_num}.jpg")


    #Save File to Folder
    # f = open(f'{p}/{img_num}.jpg', "wb")
    f = open(p, "wb")
    f.write(img.content)
    f.close()
    img_num = img_num + 1