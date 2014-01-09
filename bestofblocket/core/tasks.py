# -*- coding: utf-8 -*-
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from bestofblocket.core.models import Ad
from bs4 import BeautifulSoup
import urllib2


def set_blocket_info(url):
    """
    Gets text and image from an Ad on blocket,
    saves to the database.
    """

    orginalurl = url
    uri = url.split('.se')[1]
    url = 'http://mobil.blocket.se%s' % uri

    data = urllib2.urlopen(url).read()
    soup = BeautifulSoup(data)
    title = soup.find("h2", {"class": "item_subject"}).string.encode("utf-8")

    content = soup.find("p", {"class": "item_body"}).contents
    text = ""
    for line in content:
        if not '<strong>' in line.encode('utf-8'): 
            if line.encode("utf-8") != '<br/>':
                text+=line
            elif line.encode("utf-8") == '<br/>':
                text+='\n'

    content = text.encode('utf-8')

    ad = Ad(title=title, generation=3, text=content)
    ad.link = orginalurl.split('?')[0]
    ad.save()

    img_tags = soup.find("li", {'class': 'li_mobile_img'})

    if img_tags:
        imageurl = img_tags.find('img')['src']

        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(urllib2.urlopen(imageurl).read())
        img_temp.flush()

        img_filename = imageurl.split('/')[-1]
        ad.image.save(img_filename, File(img_temp))

    return ad

