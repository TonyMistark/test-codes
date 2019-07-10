# -*- coding: utf-8 -*-
import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}

def parse_douyin(url):
    r = requests.get(url, allow_redirects=True)
    redirecturl = r.url
    rct = requests.get(redirecturl, headers=headers)

    playurl = re.findall('playAddr:(.*?)\,', str(rct.text))[0]
    playurl = playurl.replace('playwm', 'play')
    playurl = playurl.replace("\"", "")
    print(playurl)
    # 请求要下载的url地址
    html = requests.get(playurl)
    # content返回的是bytes型也就是二进制的数据。
    html = html.content
    print(html)
    try:
        with open('douyin.mp4', 'wb') as f:
            f.write(html)
            f.flush()
        print("下载完成！！！！")
    except:
        print("下载失败！！！！")

if __name__ == '__main__':
    url = 'http://v.douyin.com/JkNaor/'
    parse_douyin(url)
