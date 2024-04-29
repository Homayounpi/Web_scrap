from scrapy import signals
from itemadapter import is_item, ItemAdapter
import random
class ScrDownloaderMiddleware:
    def process_request(self, request, spider):
        print('-!-'*30)
        print(request.headers)
    def process_response(self, request, response, spider):
        print('-#-'*30)
        print(response.headers)
        return response
class RotateUserAgenatMiddleware:
    def process_request(self, request, spider):
        user_agent = random.choice([
            'Mozilla/5.0 (Windows NT 10.0; rv:40.0) Gecko/20100101 Firefox/40.0',
            'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
            'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0',
        ])
        request.headers['User-Agent']=user_agent