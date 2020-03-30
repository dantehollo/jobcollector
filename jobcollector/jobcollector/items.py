# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobcollectorItem(scrapy.Item):
    position = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    pass
