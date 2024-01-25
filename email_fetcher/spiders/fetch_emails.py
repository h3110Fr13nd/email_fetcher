import scrapy
import os
import re


class EmailFetcherSpider(scrapy.Spider):
    name = 'fetch_emails'
    def __init__(self, start_url=None, country_css=None, country=None,
                company_block_css="ul.directory-providers__list >li.provider-card",
                company_name_css="div.provider-header > h3::attr(title)",
                website_link_css="a.provider-card__visit-btn.provider-visit.track-website-visit::attr(href)",
                *args, **kwargs):
        super(EmailFetcherSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.country_css = country_css
        if country_css:
            self.country = None
        self.company_block_css = company_block_css
        self.company_name_css = company_name_css
        self.website_link_css = website_link_css
    def parse(self, response):
        company_block = response.css(self.company_block_css)
        for company in company_block:
            website_link = company.css(self.website_link_css).get()
            company_name = company.css(self.company_name_css).get()
            country = company.css(self.country_css).get() if self.country_css else self.country
            yield response.follow(website_link, callback=self.parse_emails, meta={'company_name': company_name, 'is_homepage': True, 'country': country})

    def parse_emails(self, response):
        """Parse the page for emails"""
        company_name = response.meta.get('company_name')
        is_homepage = response.meta.get('is_homepage', False)
        country = response.meta.get('country')
        text = response.body.decode(response.encoding)
        emails = re.findall('[a-zA-Z][a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
        emails = [email for email in emails if not email.endswith((".png", ".jpg", ".jpeg", ".pdf", ".gif", ".svg", ".webp" ))]
        emails = [email for email in emails if not "example" in email.lower() and not "sentry" in email.lower()]
        emails = [email for email in emails if not re.search(r'@\d+\.\d+', email)]
        emails = list(set(emails))
        yield {
                "company_name": company_name,
                "url": response.url,
                "emails": emails,
                "country": country
            }
        if is_homepage:
            for link in set(response.css("a::attr(href)").getall()):
                link_lower = link.lower()
                if "contact" in link_lower or "about" in link_lower and not link.startswith("mailto:") and not link.startswith("tel:"):
                    yield response.follow(link, callback=self.parse_emails, meta={'origin_url': response.url, 'company_name': company_name, 'country': country})

