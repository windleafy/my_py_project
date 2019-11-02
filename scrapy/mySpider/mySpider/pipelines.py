# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline():
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(
            self.host, self.user, self.password, self.database,
            charset='utf8', port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        print(item['title'])
        data = dict(item)

        keys = ', '.join(data.keys())  # (id, thumb, title, url)
        values = ', '.join(['%s'] * len(data))  # (%,%,%,%)
        # sql = insert into table_name (id, thumb, title, url) values (%s, %s, %s, %s)
        sql = 'insert into %s (%s) values (%s)' % (item.table, keys, values)
        # tuple(data.values()) = (item[id],item[url],item[title],item[thumb])

        # 执行sql
        self.cursor.execute(sql, tuple(data.values()))
        # 提交数据
        self.db.commit()
        return item


class ImagePipeline(ImagesPipeline):
    # 将图片链接结尾作为文件名
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        # [(False, <twisted.python.failure.Failure scrapy.pipelines.files.FileException: >)]
        # [(True, {'url': 'https://p0.ssl.qhimgs1.com/t013092ddb9fe62a34a.jpg',
        # 'path': 't013092ddb9fe62a34a.jpg', 'checksum': '51f96c86e394563db42d1e43dd8a5c75'})]
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            # 如果下载失败，则抛出此异常，不会返回item，即不会保存至数据库
            raise DropItem('Image Downloaded Failed')
        # 如果下载成功，则返回item，后续将item存入数据库
        return item

    # 生成request对象，等待被调度，执行下载
    def get_media_requests(self, item, info):
        yield Request(item['url'])
