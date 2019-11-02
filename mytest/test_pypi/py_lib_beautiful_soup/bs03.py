#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 10:51
# @Author  : Wind
# @Des     : 
# @Site    : 
# @File    : bs03.py
# @Software: PyCharm

from bs4 import BeautifulSoup

html = '''
<div>
    <h1>hi, world</h1>
</div
<div>
    <label>hello world</label>
</div>
<li>
    <div aria-label="5星, 747 份评分" class="rating" role="img"></div>
</li>
<div>
    <div class="test_pypi"><p class="first" name="first_p"><b>first content</b>hello test_pypi</p><h2>this is h2</h2></div>
    <div class="test_pypi's brother"></div>
</div>
'''

soup = BeautifulSoup(html, "html.parser")

print('\nfind_class', '-' * 50)
tmp = soup.find(class_="test_pypi")
print(tmp)

# 子节点，返回结果是列表形式，包含节点和文本
print('\ncontents', '-' * 50)
print(tmp.contents)

# 子节点，返回结果是生成器，需要遍历输出
print('\nchildren', '-' * 50)
for i in tmp.children:
    print(i)

# 子孙节点，返回结果是生成器，需要遍历输出
print('\ndescendants', '-' * 50)
for i in tmp.descendants:
    print(i)

# 父节点
print('\nparent', '-' * 50)
print(tmp.parent)

# 祖先节点
print('\nparents', '-' * 50)
for i in tmp.parents:
    print(i)

# 兄弟节点
print('\nnext_siblings', '-' * 50)
for i in tmp.next_siblings:
    print(i)
