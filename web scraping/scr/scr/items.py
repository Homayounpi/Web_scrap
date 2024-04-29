import scrapy
from w3lib.html import remove_tags
from itemloaders.processors import TakeFirst, MapCompose


# def to_string(value):
#     return value.strip()

class ScrItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
#     name = scrapy.Field(input_processor=MapCompose(remove_tags),output_processor=TakeFirst())
#     capital = scrapy.Field(input_processor=MapCompose(remove_tags, to_string), output_processor=TakeFirst())
#     population = scrapy.Field()
    