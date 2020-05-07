#code to obtain image from web
import urllib.request
import random


def download_web_image(url):
    imagename = random.randrange(1, 100)
    full_imagename = str(imagename) + ".jpeg"
    urllib.request.urlretrieve(url, full_imagename)

download_web_image("https://s1.yimg.com/lo/api/res/1.2/8kDc1ePayrgqE1gvOdHkdA--/YXBwaWQ9eW15O3E9NzU7dz02NDA7c209MQ--/http://media.zenfs.com/en-US/homerun/nbcsports.com/9799ebda5a531c3e8a11ba5be69e2f2d")
