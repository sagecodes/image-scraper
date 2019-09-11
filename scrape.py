import requests
from bs4 import BeautifulSoup
import os

query = "pepsi"
url =  f"https://www.google.co.in/search?q={query}&source=lnms&tbm=isch"


r = requests.get(url)
soup = BeautifulSoup(r.content)
tags=soup.findAll('img')

for image in tags:
    #print image source
    img_url = image['src']
    img = requests.get(img_url, timeout=30)

    # Define Path
    p = ''
    # p = os.path.sep.join([args["output"], "{}{}".format(
	# 			str(total).zfill(8), ext)])
    img_num = 1
    p = os.path.join('/output')


    # Save File to Folder
    folder = open(p, "wb")
    folder.write(img)
    folder.close()