# Scrapy settings for email_fetcher project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# import pandas as pd
# import requests
# from io import StringIO
# from shutil import which
# def get_proxies():
#     url = 'https://free-proxy-list.net'
#     header = {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
#     "X-Requested-With": "XMLHttpRequest"}
#     df = pd.read_html(StringIO(requests.get(url, headers=header).text))[0]
#     df = df[df['Https']=='yes']
#     proxies = df['IP Address'] + ':' + df['Port'].astype(str)
#     proxies = proxies.tolist()
#     print("proxies", proxies)
#     return proxies

# ALL_PROXIES = get_proxies()
BOT_NAME = "email_fetcher"

SPIDER_MODULES = ["email_fetcher.spiders"]
NEWSPIDER_MODULE = "email_fetcher.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "email_fetcher.middlewares.EmailFetcherSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "email_fetcher.middlewares.EmailFetcherDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "email_fetcher.pipelines.EmailFetcherPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.selectreactor.SelectReactor"
FEED_EXPORT_ENCODING = "utf-8"



# DOWNLOADER_MIDDLEWARES = {
#     "rotating_proxies.middlewares.RotatingProxyMiddleware": 610,
#     "rotating_proxies.middlewares.BanDetectionMiddleware": 620,
#     # "scrapy_selenium.SeleniumMiddleware": 800 # scrapy-selenium middleware
# }
# SELENIUM_DRIVER_NAME = "chrome" # driver name
# SELENIUM_DRIVER_ARGUMENTS = ["--headless=new", '--ignore-certificate-errors', '--ignore-ssl-errors=yes'] # selenium arguments 
# SELENIUM_DRIVER_EXECUTABLE_PATH = which("chromedriver") # driver path


# ROTATING_PROXY_BACKOFF_BASE = 100
# # ROTATING_PROXY_LIST =  ['104.234.157.100:21278']
# ROTATING_PROXY_LIST =  ALL_PROXIES

