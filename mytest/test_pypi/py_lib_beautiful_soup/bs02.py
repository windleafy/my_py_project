#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 20:13
# @Author  : Wind
# @Des     : 
# @Site    : 
# @File    : bs02.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import re

html = '''
<h1>hi, world</h1>

<div>
    <label>hello world</label>
</div>
<li>
    <div aria-label="5星, 747 份评分" class="rating" role="img"></div>
</li>
<div>
    <p class="first" name="first_p"><b>first content</b>hello test_pypi</p>
</div>
'''

soup = BeautifulSoup(html, "html.parser")

tmp1 = soup.div

tmp2 = soup.find(class_='rating')
tmp3 = soup.find(attrs={'class': 'rating'})

tmp4 = soup.find('div', class_='rating')
tmp5 = soup.find('div', attrs={'class': 'rating'})

tmp6 = soup.li.div.get('aria-label')

# print(soup.p.attrs['name'])

# 返回所有匹配正则的节点文本组成的列表
tmp7 = soup.find_all(string=re.compile('hello'))
print(tmp7)

print(soup.p.string)
[s.extract() for s in soup.p("b")]
print(soup.p.string)
print(soup.p.get_text())

print(soup.li.div.get('aria-label'))
print(soup.li.div['aria-label'])
