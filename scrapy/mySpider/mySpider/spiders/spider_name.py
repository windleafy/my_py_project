# -*- coding: utf-8 -*-
import scrapy


class SpiderNameSpider(scrapy.Spider):
    name = 'spider_name'
    allowed_domains = ['des_url.com']
    start_urls = ['http://des_url.com/']

    def parse(self, response):
        pass
