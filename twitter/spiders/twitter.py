# To use this code, first install and set up: https://scrapy-zyte-api.readthedocs.io/en/latest/

from scrapy import Request, Spider


class MySpider(Spider):
    name = "toscrape_com"

    def start_requests(self):
        yield Request(
            "https://x.com/ForeverScept",
            meta={
                "zyte_api_automap": {
                    "forumThread": True,  
                    "forumThreadOptions": {"extractFrom":"browserHtml"} 
                },
            },
        )

    def parse(self, response):
        forumThread = response.raw_api_response["forumThread"]
        yield forumThread
