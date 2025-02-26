# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VacancyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    name = scrapy.Field()
    min_salary = scrapy.Field()
    max_salary = scrapy.Field()
    salary = scrapy.Field()
    link = scrapy.Field()
    source = scrapy.Field()
    pass
