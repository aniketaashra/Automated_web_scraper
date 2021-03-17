# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class UniversitiesItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    current_name = Field()
    former_name = Field()
    students = Field()
    location = Field()
    undergraduates = Field()
    postgraduates = Field()
