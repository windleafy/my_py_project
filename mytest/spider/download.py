#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 15:09
# @Author  : Wind
# @Des     : 
# @Site    : 
# @File    : download.py
# @Software: PyCharm
import requests
import re


base_url = 'https://www.bilibili.com/video/av6499012'

# 访问起始网页需添加的请求头，不加的话，得不到完整的源代码（反爬）
base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;'
              'q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q = 0.9'
}

# 请求视频下载地址时需要添加的请求头
download_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
    'Referer': 'https://www.bilibili.com/video/av6499012',
}

base_response = requests.get(base_url, headers=base_headers)
html = base_response.text
video_name = re.search('<span class="tit">(.*?)</span>', html, re.S).group(1) + '.flv'
download_url = re.search('window.__playinfo__={.*?"url":"(.*?)".*?}', html, re.S).group(1)
print(video_name)

with open(video_name, 'wb') as f:
    f.write(requests.get(download_url, headers=download_headers, stream=True, verify=False).content)
