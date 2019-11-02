#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""test03"""
# @Time    : 2019/10/28 20:34
# @Author  : Wind
# @Des     : 
# @Software: PyCharm

# [(False, <twisted.python.failure.Failure scrapy.pipelines.files.FileException: >)]
# [(True, {'url': 'https://p0.ssl.qhimgs1.com/t013092ddb9fe62a34a.jpg',
# 'path': 't013092ddb9fe62a34a.jpg', 'checksum': '51f96c86e394563db42d1e43dd8a5c75'})]
results = [(True, {'url': 'https://p0.ssl.qhimgs1.com/t013092ddb9fe62a34a.jpg',
                   'path': 't013092ddb9fe62a34a.jpg',
                   'checksum': '51f96c86e394563db42d1e43dd8a5c75'})]
image_paths = []
for ok, x in results:
    if ok:
        image_paths.append(x['path'])

print(image_paths)
