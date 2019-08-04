import os
import requests
import urllib
import time
import re
import json
import hashlib
from bs4 import BeautifulSoup


CHAPTER = 14 # 0 = all
DOWNLOAD_IMAGES = True
JSON_DIR = "/home/bob/comics/woxcette/src/assets"
IMG_DIR = "/home/bob/comics/woxcette/src/assets/img"
URLS = [
  "https://tgchan.org/kusaba/questarch/res/692327.html",
  "https://tgchan.org/kusaba/questarch/res/696969.html",
  "https://tgchan.org/kusaba/questarch/res/715522.html",
  "https://tgchan.org/kusaba/questarch/res/727645.html",
  "https://tgchan.org/kusaba/questarch/res/736166.html",
  "https://tgchan.org/kusaba/questarch/res/743488.html",
  "https://tgchan.org/kusaba/questarch/res/754011.html",
  "https://tgchan.org/kusaba/questarch/res/759736.html",
  "https://tgchan.org/kusaba/questarch/res/768999.html",
  "https://tgchan.org/kusaba/questarch/res/784444.html",
  "https://tgchan.org/kusaba/questarch/res/812307.html",
  "https://tgchan.org/kusaba/quest/res/833755.html",
  "https://tgchan.org/kusaba/quest/res/875642.html",
  "https://tgchan.org/kusaba/quest/res/939120.html"
]

def downloadImage(link, filename, chapter):
  if DOWNLOAD_IMAGES:
    r = requests.get(link)
    imgDir = os.path.join(IMG_DIR, 'chapter' + str(chapter))
    open(os.path.join(imgDir, filename), 'wb').write(r.content)
    print('Image ' + os.path.join(imgDir, filename) + ' downloaded...')
    time.sleep(1)

def scrape(url, chapter):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  posts = soup.findAll('table')
  postList = list()

  # Get first post
  authorId = soup.find("span", class_="uid").text
  poster = soup.find("span", class_="postername").text
  pColor = hashlib.md5(poster).hexdigest()[0:6]
  body = soup.find("blockquote")
  body['style'] = "border-left:5px solid #" + pColor
  image = soup.find("span", class_="filesize").find("a").get("href")
  dlLink = "http://tgchan.org" + image
  image = image[image.rfind('/')+1:len(image)]

  # Download the image and wait a bit
  downloadImage(dlLink, image, chapter)

  newPost = {
    "poster" : poster,
    "isAuthor" : True,
    "pColor" : pColor,
    "image" : image,
    "spoiler" : False,
    "body" : body.encode("utf-8")
  }
  postList.append(newPost)

  for post in posts:
    fPoster = ""
    isAuthor = False
    pColor = ""
    fImage = ""
    fBody = ""
    spoiler = False

    poster = post.find("span", class_="postername")
    if poster is not None:
      fPoster = poster.text
      try:
        pColor = hashlib.md5(fPoster).hexdigest()[0:6]
      except:
        pass
    postId = post.find("span", class_="uid")
    if postId is not None:
      if postId.text == authorId:
        isAuthor = True
    image = post.find("span", class_="filesize")
    if image is not None:
      image = image.find("a")
      if image is not None:
        image = image.get("href")
        dlLink = "http://tgchan.org" + image
        image = image[image.rfind('/')+1:len(image)]

        # Download the image and wait a bit
        downloadImage(dlLink, image, chapter)

    if post.find("img") is not None:
      if "spoiler" in post.find("img").get("src"):
        spoiler = True
    body = post.find("blockquote")
    if body is not None:
      spoilerTag = body.find("span", class_="spoiler")
      if spoilerTag is not None:
        del(spoilerTag['onmouseover'])
        del(spoilerTag['onmouseout'])
        del(spoilerTag['style'])
      body['style'] = "border-left:5px solid #" + pColor
      fBody = body

    #newPost = Post(fPoster, fImage, fBody);
    newPost = {
      "poster" : fPoster,
      "isAuthor" : isAuthor,
      "pColor" : pColor,
      "image" : image,
      "spoiler" : spoiler,
      "body" : fBody.encode("utf-8")
    }

    postList.append(newPost)

  fileName = "chapter" + str(chapter) + ".json"
  with open(os.path.join(JSON_DIR, fileName), 'w') as f:
    f.write(json.dumps(postList))
    print("Wrote " + os.path.join(JSON_DIR, fileName))
    
if CHAPTER == 0:
  for i, link in enumerate(URLS):
    scrape(link, i + 1)
else:
  scrape(URLS[CHAPTER - 1], CHAPTER)