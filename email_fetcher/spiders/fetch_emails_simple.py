import scrapy
import os
import re


class EmailFetcherSpider(scrapy.Spider):
    name = 'fetch_emails_simple'
    def __init__(self, start_url_csv=None,
                *args, **kwargs):
        super(EmailFetcherSpider, self).__init__(*args, **kwargs)
        with open(start_url_csv, 'r') as f:
            self.start_urls = f.read().splitlines()
            # apply strip to each element in the list
            self.start_urls = list(map(str.strip, self.start_urls))

        # self.country_css = country_css
        # self.country = country
        # if country_css:
            # self.country = None
        # 
        # self.company_block_css = company_block_css
        # self.company_name_css = company_name_css
        # self.website_link_css = website_link_css
        # self.category = category
    # def parse(self, response):
    #     company_block = response.css(self.company_block_css)
    #     for company in company_block:
    #         website_link = company.css(self.website_link_css).get()
    #         company_name = company.css(self.company_name_css).get()
    #         country = ' '.join(company.css(self.country_css).getall()).strip() if self.country_css else self.country
    #         yield response.follow(website_link, callback=self.parse_emails, meta={'company_name': company_name, 'is_homepage': True, 'country': country})
    def start_requests(self):
        for url in self.start_urls:
            domain = url if not url.startswith("http") else url.split("//")[-1]
            url = "https://" + url if not url.startswith("http") else url
            yield scrapy.Request(url, self.parse, meta={'is_homepage': True, 'domain': domain})
    def parse(self, response):
        """Parse the page for emails"""
        # company_name = response.meta.get('company_name')
        is_homepage = response.meta.get('is_homepage', True)
        domain = response.meta.get('domain', response.url)
        # country = response.meta.get('country')

        origin_url = response.meta.get('origin_url', response.url)

        text = response.body.decode(response.encoding)
        emails = re.findall('[a-zA-Z][a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
        emails = [email for email in emails if not email.endswith((".png", ".jpg", ".jpeg", ".pdf", ".gif", ".svg", ".webp" ))]
        emails = [email for email in emails if not "example" in email.lower() and not "sentry" in email.lower()]
        emails = [email for email in emails if not re.search(r'@\d+\.\d+', email)]
        emails = list(set(emails))
        yield {
                # "company_name": company_name,
                "domain": domain,
                "origin_url": origin_url,
                "url": response.url,
                "emails": emails,
                # "country": country,
                # "category": self.category,
            }
        
        if is_homepage:
            for link in set(response.css("a::attr(href)").getall()):
                link_lower = link.lower()
                if "contact" in link_lower or "about" in link_lower and not link.startswith("mailto:") and not link.startswith("tel:"):
                    yield response.follow(link, callback=self.parse, meta={'is_homepage': False, 'origin_url': response.url, 'domain': domain})

