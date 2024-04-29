import scrapy
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags





class WikiSpider(scrapy.Spider):
    name = "github"
    start_urls = ["https://github.com/login/"]
    

    def parse(self, response):
        data = {'login':'','password':''}
        # for hidden in response.css('input[type="hidden"]'):                                                       
        #     data[hidden.attrib['name']] = hidden.attrib.get('value','unknown')
        return scrapy.FormRequest.from_response(response,url='https://github.com/session/', formdata=data,callback=self.after_login)

    def after_login(self,response):
        yield response.follow('https://github.com/Homayounpi',self.profile)

    def profile(self,response):

        yield {'name':response.css('.p-nickname::text').get().strip()}

    