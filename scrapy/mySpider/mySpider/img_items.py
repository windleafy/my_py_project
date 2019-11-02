#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""img_items"""
# @Time    : 2019/10/27 17:07
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
from scrapy import Item, Field


class ImageItem(Item):
    collection = table = 'images'

    id = Field()
    url = Field()
    title = Field()
    thumb = Field()
