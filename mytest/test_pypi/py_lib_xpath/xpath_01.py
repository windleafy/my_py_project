#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""xpath_01"""
# @Time    : 2019/10/26 18:12
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html">
         first item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">
         second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">
         third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">
         fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">
         fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
# html = etree.parse('./test.html', etree.HTMLParser())  # 加载html文件的写法


result = etree.tostring(html)
print(result.decode('utf-8'))

result = html.xpath('//*')
print(result)

result = html.xpath('//li')
print(result)

# 取指定子节点，结果非空
result = html.xpath('//li/a')
print(result)

# 取指定子节点，结果为空
result = html.xpath('//ul/a')
print(result)

# 取指定子孙节点，结果非空
result = html.xpath('//ul//a')
print(result)

# 取指定子孙节点，指定属性，属性值
result = html.xpath('//li/a/@href')
print(result)

# 取父节点指定属性
result = html.xpath('//a[@href="https://ask.hellobi.com/link4.html"]/../@class')
print(result)
result = html.xpath('//a[@href="https://ask.hellobi.com/link4.html"]/parent::*/@class')
print(result)

# 取指定属性值的指定节点
result = html.xpath('//li[@class="item-0"]')
print(result)

# 指定属性节点的文本值
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

# 属性多值匹配
text = '''
<li class="li li-first"><a href="https://ask.hellobi.com/link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

# 多个属性匹配
text = '''
<li class="li li-first" name="item"><a href="https://ask.hellobi.com/link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)


# 按序选择
text = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html">
         first item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">
         second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">
         third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">
         fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">
         fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)


# 节点轴选择
text = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html">
         <span>first item</span></a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">
         second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">
         third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">
         fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">
         fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="https://ask.hellobi.com/link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')
print(result)
result = html.xpath('//li[1]/following-sibling::*')
print(result)
