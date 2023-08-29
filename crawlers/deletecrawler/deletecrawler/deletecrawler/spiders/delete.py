import scrapy


class DeleteSpider(scrapy.Spider):
    name = 'delete'
    allowed_domains = ['www.google.com']
    junk_urls = []
    def start_requests(self):
        """
        Here we get url via URLs Api and
        fill urls list with them
        """
        urls = [
            'https://bama.ir/car/detail-umwwe3z-renault-parstondar-1397',
            'https://bama.ir/car/detail-eh354nb-renault-tondar90-e2-1398',
            'https://ganje.ir/ads/car/582485867781204793',
            'https://divar.ir/aslkdnajksld',
            'https://divar.ir/v/%D9%BE%D8%B1%D8%A7%DB%8C%D8%AF-111-sx-%D9%85%D8%AF%D9%84-%DB%B1%DB%B3%DB%B9%DB%B1_%D8%B3%D9%88%D8%A7%D8%B1%DB%8C-%D9%88-%D9%88%D8%A7%D9%86%D8%AA_%DA%A9%D8%A7%D8%B4%D8%A7%D9%86__%D8%AF%DB%8C%D9%88%D8%A7%D8%B1/wYq4tE-k'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)            

    def parse(self,response):
        """
        Here we check does that request has content or not .
        if not so it should be add in to junk_urls list
        """
        url = response.request.url

        # Check Divar Urls
        if url.__contains__('divar.ir'):
            if response.status == 404 : self.junk_urls.append(response.request.url)
        
        # Check Sheypoor Urls
        elif url.__contains__('sheypoor.com'):
            if response.status == 410 : self.junk_urls.append(response.request.url)

        # Check Bama Urls
        elif url.__contains__('bama.ir'):
            if response.status == 500 : self.junk_urls.append(response.request.url)
        
        print(len(self.junk_urls))
        yield