# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TirolItem(scrapy.Item):
    date = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
