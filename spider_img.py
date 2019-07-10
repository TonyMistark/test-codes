#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
import requests
from bs4 import BeautifulSoup


def spid_img(path):
    _url = 'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
    urls = [_url.format(page=page) for page in range(1, 200+1)]
    count = 1
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        img_list = soup.find_all('img', class_='ui image lazy')
        for img in img_list:
            image = img.get('data-original')
            title = img.get('title')[:50]
            file_name = f"{title}{os.path.splitext(image)[-1]}"
            file_name = file_name.replace("/", "-")
            file_path = os.path.join(path, file_name)
            print(file_path, count)
            count += 1
            with open(file_path, 'wb') as f:
                img = requests.get(image).content
                f.write(img)

if __name__ == "__main__":
    print(sys.argv)
    spid_img(sys.argv[1])
