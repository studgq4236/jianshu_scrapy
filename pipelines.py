# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class AuthorPipeline(object):

#链接数据库

	def __init__(self):
		client = pymongo.MongoClient('localhost',27017)
		admin = client['admin']
		author = admin['author']
		self.post = author

#插入数据库

    def process_item(self, item, spider):
    	info = dict(item)
    	self.post.insert(info)
        return item
