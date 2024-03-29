import scrapy
import os
import re
import pandas as pd


class EmailFetcherSpider(scrapy.Spider):
    name = 'fetch_emails_us'
    def __init__(self, start_url_csv=None,
                *args, **kwargs):
        super(EmailFetcherSpider, self).__init__(*args, **kwargs)
        self.df = pd.read_csv(start_url_csv)
        

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
        for company_name, homepage, domain in zip(self.df['Name'], self.df['homepage'], self.df['domain']):
            yield scrapy.Request(homepage, self.parse, meta={'is_homepage': True, 'domain': domain, 'origin_url': homepage, 'company_name': company_name})
    def parse(self, response):
        """Parse the page for emails"""
        company_name = response.meta.get('company_name')
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
                "company_name": company_name,
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
                    yield response.follow(link, callback=self.parse, meta={'is_homepage': False, 'origin_url': response.url, 'domain': domain, 'company_name': company_name})

