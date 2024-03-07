# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AuthorsItem(scrapy.Item):
    # define the fields for your item here like:
    fullname = scrapy.Field()
    born_date = scrapy.Field()
    born_location = scrapy.Field()
    description = scrapy.Field()


class QuotesItem(scrapy.Item):
    tags = scrapy.Field()
    author = scrapy.Field()
    quote = scrapy.Field()
