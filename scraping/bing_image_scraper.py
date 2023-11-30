from bs4 import BeautifulSoup
import requests
import re
import sys
import os
import http.cookiejar
import json
import urllib.request, urllib.error, urllib.parse

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(
        urllib.request.Request(url,headers=header)),
        'html.parser')

query = sys.argv[1]
query = query.split()
query = '+'.join(query)
url="http://www.bing.com/images/search?q=" + query + "&FORM=HDRSC2"

basedir="bing_images"
if not os.path.exists(basedir):
    os.mkdir(basedir)

full_dir = os.path.join(basedir, query.split()[0])
if not os.path.exists(full_dir):
    os.mkdir(full_dir)


header={'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
soup = get_soup(url,header)

images=[] # will be populated with image names and links
for a in soup.find_all("a",{"class":"iusc"}):
    m = json.loads(a["m"])
    murl = m["murl"] #full size image
    turl = m["turl"] #link to the thumbnail image, but not going to use it here

    image_name = urllib.parse.urlsplit(murl).path.split("/")[-1]

    images.append((image_name, murl))
    print(image_name, murl)


for i, (image_name, murl) in enumerate(images):
    try:
        raw_img = urllib.request.urlopen(murl).read()

        f = open(os.path.join(full_dir, image_name), 'wb')
        f.write(raw_img)
        f.close()
    except Exception as e:
        print("could not load : " + image_name)
        print(e)