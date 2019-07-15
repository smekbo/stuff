import requests
import urllib
import time
import re
from bs4 import BeautifulSoup

# For scraping a live site
#url = "https://tgchan.org/kusaba/questarch/res/692327.html"
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")

# http://192.168.88.234/woxcette/chapter1/tgchan.org/kusaba/questarch/res/692327.html

# Scrape a cached one for testing
with open("chapter1/tgchan.org/kusaba/questarch/res/692327.html") as fp:
  soup = BeautifulSoup(fp, "html.parser")

class Post:
  def __init__(self, poster, image, body):
    self.poster = poster
    self.image = image
    self.body = body


posts = soup.findAll('table')
postList = list()

for post in posts:
  fPoster = ""
  fImage = ""
  fBody = ""
  
  poster = post.find("span", class_="postername")
  if poster is not None:
    pass
    fPoster = poster.text
  image = post.find("span", class_="filesize")
  if image is not None:
    image = image.find("a")
    if image is not None:
      image = image.get("onclick")
      if image is not None:
        #print(image)
        regex = re.search(r",[^']*'([^']*)'", image)
        if regex is not None:
          fImage = regex.group(1)
  body = post.find("blockquote")
  if body is not None:
    fBody = body
    
  newPost = Post(fPoster, fImage, fBody);
  
  postList.append(newPost)
  
with open('/home/bob/comics/woxcette/chapter1/tgchan.org/kusaba/questarch/res/index.html', 'w') as f:
    f.write('<html>')
    f.write('<link rel="stylesheet" type="text/css" href="/woxcette/style.css" >')
    f.write("""
    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>""")    
    for post in postList:
      if post.image != "":
        f.write("<div class='container'>")
        f.write("<div class='row post'>")
        f.write("<div class='col s12 poster'><b>" + post.poster + "</b></div>")
        f.write("<img class='col s5 postimage' src=" + post.image + " >")
        f.write("<div class='col s7 postbody'>" + post.body.encode('utf-8').decode('ascii', 'ignore') + "</div>")
        f.write("</div></div>")
    f.write("</html")
      