#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 11:08
# @Author  : Wind
# @Site    : 
# @File    : py_lib_beautiful_soup.py
# @Software: PyCharm


import random
import time
import requests
from bs4 import BeautifulSoup, Comment

from requests.adapters import HTTPAdapter


def beautiful_soup_test():
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    <img src="/i/eg_tulip1.jpg" />
    <img src="/i/eg_tulip2.jpg" />
    <label>Do you like peas?
        <input type="checkbox" name="peas">
        <p>被你找到了</p>
    </label>
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(soup.prettify())
    '''指定标签'''
    for item in soup.find_all('a'):
        '''获取链接地址'''
        print(item.get('href'))

    '''指定标签，选中标签下指定属性'''
    for item in soup.find_all('p', {'class': 'story'}):
        print(item.text)
        print('-' * 20)

    '''指定属性'''
    for item in soup.findAll(attrs={"class": "story"}):
        print(item.text)

    for item in soup.find_all('img'):
        print(item.get('src'))

    '''.的应用'''
    print(soup.label.p.string)

    tmp = soup.find(class_="title")
    print(tmp)


beautiful_soup_test()

# url参数
url = 'http://www.baidu.com'
url_page = requests.get(url, timeout=10)
# html_dom = BeautifulSoup(url_page.text, "html.parser")


# 删除标签
html = '''
<script>a</script>
baba
<script>b</script>
<h1>hi, world</h1>
<label>hello</label>
'''
html_dom = BeautifulSoup(html, "html.parser")
[s.extract() for s in html_dom('label')]
print(type(html_dom))

# 删除注释
data = """<div class="foo">
cat dog sheep goat
<!--
<p>test</p>
-->
</div>"""

html_dom = BeautifulSoup(data, "html.parser")
for element in html_dom(text=lambda text: isinstance(text, Comment)):
    element.extract()
print(html_dom.prettify())
