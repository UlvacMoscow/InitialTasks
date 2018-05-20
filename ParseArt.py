# -*- coding: utf-8 -*-
import shutil
import requests
from BeautifulSoup import BeautifulSoup


url = ""
page = requests.get(url).text
soup = BeautifulSoup(page)
divs = soup.findAll('div', {'class': 'shortpost'})


def find_content():
    for div in divs:
        div_title = div.find('div', {'class': 'postitle'})
        link_text = div_title.find('a').text
        print(link_text)

        img = div.find('div', {'class': 'postcover'})
        img_src = img.find('img').get('src')

        response = requests.get(img_src, stream=True)
        with open(link_text + '.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

    return

print(find_content())