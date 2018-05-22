# -*- coding: utf-8 -*-
import shutil
import requests
from bs4 import BeautifulSoup


count = 1
while count <= 3:

    url = "http://bazkino.club/page/{}".format(count)
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    divs = soup.findAll('div', {'class': 'th-in'})
    print('Count', count, url)

    def find_content():
        for div in divs:
            div_title = div.find('div', {'class': 'th-desc'})
            link_text = div_title.find('a').text
            print(link_text)

            img = div.find('a')
            img_src = img.find('img').get('src')
            img_src = 'http://bazkino.club' + img_src

            response = requests.get(img_src, stream=True)
            with open(link_text.replace('/', '') + '.jpg', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

        return

    count += 1

    print(find_content())