# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class AuthorItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author_url = Field()
    author_name = Field()
    style = Field()
    focus = Field()
    fans = Field()
    article_num = Field()
    write_num = Field()
    like = Field()
    pass
