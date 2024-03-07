import scrapy
from quotesauthors.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    custom_settings = {
        "FEED_URI": f"json_data/{name}.json",
        "FEED_FORMAT": "json",
    }
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def compose_data(self, raw_quote):
        quote = QuotesItem()

        quote["tags"] = raw_quote.xpath("div[@class='tags']/a/text()").getall()
        quote["author"] = raw_quote.xpath("span/small[@class='author']/text()").get()
        quote["quote"] = raw_quote.xpath("span[@class='text']/text()").get()
        return quote

    def parse(self, response, **kwargs):
        quotes = response.xpath("/html//div[@class='quote']")

        for quote in quotes:
            yield self.compose_data(quote)

        next_page = response.xpath("/html//li[@class='next']/a/@href").get()

        if next_page is not None:
            yield scrapy.Request(url=self.start_urls[0] + next_page)
