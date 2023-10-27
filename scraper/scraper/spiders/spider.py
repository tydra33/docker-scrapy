import scrapy
import json
import re


class ApartmentSpider(scrapy.Spider):
    name = "scraper"
    # check the api
    start_urls = [
        "https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page=0&per_page=500"
    ]

    def parse(self, response):
        response_json = json.loads(response.body)

        for flat in response_json.get("_embedded").get("estates"):
            image_urls = [img.get("href") for img in flat.get("_links").get("images")]

            yield (
                {
                    "title": re.sub(r"\s", " ", flat.get("name")),
                    # "name": flat,
                    "image_urls": ";".join(image_urls),
                }
            )
