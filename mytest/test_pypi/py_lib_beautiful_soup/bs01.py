#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 19:23
# @Author  : Wind
# @Des     : 
# @Site    : 
# @File    : bs01.py
# @Software: PyCharm
from bs4 import BeautifulSoup

# 删除标签  方法一
html = '''
<script>a</script>
baba
<script>b</script>
<h1>hi, world</h1>
<div>
<label>hello</label>
</div>
'''

html_dom = BeautifulSoup(html, "html.parser")
tag = html_dom.find('div')
# print(tag)
tag.clear()
print('测试一===================================')
print(html_dom)


# 删除标签  方法二
html = '''
<script>a</script>
baba
<script>b</script>
<h1>hi, world</h1>
<div>
<label>hello</label>
</div>
'''
html_dom = BeautifulSoup(html, "html.parser")
[s.extract() for s in html_dom("label")]
print('测试二===================================')
print(html_dom)


# 删除标签  方法三
html = '''
<script>a</script>
baba
<script>b</script>
<h1>hi, world</h1>
<div>
<label>hello</label>
</div>
<div>
<h1></h1>
</div>
<div>
<h2></h2>
</div>
'''
html_dom = BeautifulSoup(html, "html.parser")
tmp = html_dom.find_all('div')
for i in tmp:
    [s.extract() for s in i("label")]
print('测试三===================================')
print(tmp)


# 删除标签  方法四
html = '''
<script>a</script>
baba
<script>b</script>
<h1>hi, world</h1>
<div>
<label>hello</label>
</div>
<div>
<h1></h1>
</div>
<div>
<h2></h2>
</div>
'''
html_dom = BeautifulSoup(html, "html.parser")
tag = html_dom.find('div')
print('测试四===================================')
print(tag)
[s.extract() for s in tag("label")]
print(tag)
