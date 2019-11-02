#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 13:00
# @Author  : Wind
# @Des     : PyQuery基本用法实例
# @Site    : 
# @File    : pq02.py
# @Software: PyCharm

from pyquery import PyQuery as Pq

html = '''
<div node-type="common_video_player" video-sources="xxxxxxxxxxxxx"</div>
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="white"><b>I'm trouble maker</b>first item</li>
             <li id="yellow">second item</li>
        </ul>
    </div>
    <li class="green">third item</a></li>
</div>
<li class="white">fourth item</a></li>
<div self-type="test_pypi" self-type1="I'm glad">Hello Wind</div>
'''

html_doc = Pq(html)

# 遍历指定标签的节点
# 用法：html_doc('标签名称')
print('遍历指定标签的节点', '-'*50)
for i in html_doc('li').items():
    print('节点内容：', str(i).replace("\n", ""))
    print('节点文本：', i.text())
    print('节点属性值：', i.attr('self-type1'), '\n')

# 遍历指定class的节点，"."表示class与css相同
# 用法：html_doc('.标签class')
print('遍历指定class的节点', '-'*50)
for i in html_doc('.white').items():
    print('节点内容：', str(i).replace("\n", ""))
    print('节点文本：', i.text())
    print('节点属性值：', i.attr('self-type1'), '\n')

# 遍历指定id的节点，"#"表示id与css相同
# 用法：html_doc('#标签id')
print('遍历指定id的节点', '-'*50)
for i in html_doc('#yellow').items():
    print('节点内容：', str(i).replace("\n", ""))
    print('节点文本：', i.text())
    print('节点属性值：', i.attr('self-type1'), '\n')

# 遍历指定标签与属性的节点
# 用法：html_doc('标签名称[属性名称="属性值"]')
print('遍历指定标签与属性的节点', '-'*50)
for i in html_doc('div[self-type="test_pypi"]').items():
    print('节点内容：', str(i).replace("\n", ""))
    print('节点文本：', i.text())
    print('节点属性值：', i.attr('self-type1'), '\n')
