import scrapy
from quotesauthors.items import AuthorsItem


class AuthorsSpider(scrapy.Spider):
    name = "authors"

    custom_settings = {
        "FEED_URI": f'json_data/{name}.json',
        "FEED_FORMAT": 'json'
    }

    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response, **kwargs):

        links = response.xpath("/html//div[@class='quote']/span/a/@href").getall()

        for link in links:
            page = scrapy.Request(url=self.start_urls[0] + link, callback=self.parse_page)
            yield page

    def parse_page(self, response):
        details_for_authors = response.xpath("//div[@class='author-details']")
        for info in details_for_authors:
            authors = AuthorsItem()

            authors['fullname'] = info.xpath(".//h3[@class='author-title']/text()").get()
            authors['born_date'] = info.xpath(".//span[@class='author-born-date']/text()").get()
            authors['born_location'] = info.xpath(".//span[@class='author-born-location']/text()").get()
            description = info.xpath(".//div[@class='author-description']/text()").get().strip()
            authors['description'] = description.replace('\n', ' ').strip()

            yield authors
