# Program to downlaod image from url

import urllib.request
import random

url = "https://s3-us-west-1.amazonaws.com/powr/defaults/image-slider1.jpg"


def downloadImage(url):
    name = random.randrange(1, 1000)
    fileName = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fileName)


downloadImage(url)
