# noinspection PyUnresolvedReferences
import scrapy
# noinspection PyUnresolvedReferences
from w3lib.html import remove_tags
from scrapy.linkextractors import LinkExtractor 


#--------------follow
# class WikiSpider(scrapy.Spider):
# 	name = 'wiki'
# 	start_urls = [
# 		'https://www.bike-discount.de/en/bike',

# 	]

# 	def parse(self, response, **kwargs):
# 		for bike in response.css('div.product--box'):
# 			name = remove_tags(bike.css('a.product--title').get()).strip()
# 			price = remove_tags(bike.css('.product--price').get()).strip()

# 			yield {'name': name, 'price': price}
# 		next_page = response.css('a[title="Next page"]::attr(href)').get()
# 		if next_page:
# 			yield response.follow(next_page, callback=self.parse)
#---------------------	Resquest
# class WikiSpider(scrapy.Spider):
# 	name = 'wiki'
# 	start_urls = [
# 		'https://www.bike-discount.de/en/bike',

# 	]

# 	def parse(self, response, **kwargs):
# 		for bike in response.css('div.product--box'):
# 			link = bike.css('a.product--title::attr(href)').get()
# 			yield scrapy.Request(link,callback=self.parse_bike)
# 	def parse_bike(self,response,**kwargs):
# 		price = response.css('#netz-price::text').get()
# 		yield {'price':price}
#---------------------	
class WikiSpider(scrapy.Spider):
	name = 'wiki'
	start_urls = [
		'https://www.mongard.ir/',
	]
	li = LinkExtractor(deny='countact',allow='git',allow_domains='facebook')

	def parse(self, response, **kwargs):
		links = self.li.extract_links(response)
		for link in links:
			yield {'link':link}
		 



