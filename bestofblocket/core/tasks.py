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
    title = soup.find("h1", {"itemprop": "name"}).string.encode("utf-8")

    content = soup.find("div", {"itemprop": "description"})
    text = ""

    # Get contents of each P tag.
    for paragraph in content:
        for line in paragraph:
            if not '<strong>' in line.encode('utf-8'):
                if line.encode("utf-8") != '<br/>':
                    text+=line
                elif line.encode("utf-8") == '<br/>':
                    text+='\n'

        # Add a newline after each paragraph
        text+='\n'


    content = text.encode('utf-8')

    ad = Ad(title=title, generation=3, text=content)
    ad.link = orginalurl.split('?')[0]
    ad.save()

    img_tags = soup.find("span", {'class': 'image'})

    if img_tags:
        imageurl = img_tags['data-src']
        imageurl = 'http://cdn.blocket.com/static/1/640x480/%s' % imageurl

        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(urllib2.urlopen(imageurl).read())
        img_temp.flush()

        img_filename = imageurl.split('/')[-1]
        ad.image.save(img_filename, File(img_temp))

    return ad
