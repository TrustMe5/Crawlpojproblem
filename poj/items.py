# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PojItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    link=scrapy.Field()
    Time_Limit=scrapy.Field()
    Memory_Limit=scrapy.Field()
    Description=scrapy.Field()
    Input=scrapy.Field()
    Output=scrapy.Field()
    Sample_Input=scrapy.Field()
    Sample_Output=scrapy.Field()
    pass
