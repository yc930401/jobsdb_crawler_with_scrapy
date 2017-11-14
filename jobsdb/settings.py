# -*- coding: utf-8 -*-

# Scrapy settings for jobsdb project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jobsdb'

SPIDER_MODULES = ['jobsdb.spiders']
NEWSPIDER_MODULE = 'jobsdb.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jobsdb (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'en-US,en;q=0.8,fr;q=0.6',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'NSC_wjq_kpctec.dpn_ttm2=14b5a3d9e9a059a69d137dda9e61d206db060add87cf365767e907ecf58f41a1dc04ea1d; AB.Key=5867; inLanding=https%3A%2F%2Fsg.jobsdb.com%2Fsg; spUID=15104618386979998c26ca1.a589b97e; ASP.NET_SessionId=tdvxfaaxvuzt1gb5la5p4ofl; JobsDB.IsAssignedDefaultSummaryMode2=0; OAID=794c986bf71181db07686d6a285f3bcf; s_vnum=1513149226337%26vn%3D5; __utmt=1; _gat_UA-2012489-10=1; RecentSearch=%7B%22JobFunction%22%3A%5B%223%22%2C%222%22%5D%7D; SolData.Search.Hash=5ae0df128702e7798456765dd486d8e8; SolData.SearchID=e26ed2fa-86b4-4a87-8c01-c079d841a302; JLP=True; HideShowBulletInfo=%7B%22DontShowPromoAgain%22%3Afalse%2C%22DefaultShow%22%3Anull%2C%22PromoBubbleShowTimes%22%3A2%7D; s_invisit=true; s_cc=true; s_sq=%5B%5BB%5D%5D; s_vi=[CS]v1|2D04A31605036C8E-40001193C0002B01[CE]; _ga=GA1.3.833630475.1510557226; _gid=GA1.3.1792777067.1510557227; JobsDB.IsCookieSupported=true; __utma=17118395.833630475.1510557226.1510567092.1510576396.5; __utmb=17118395.6.10.1510576396; __utmc=17118395; __utmz=17118395.1510557226.1.1.utmcsr=angryangmo.com|utmccn=(referral)|utmcmd=referral|utmcct=/uncategorized/10-top-job-portals-kick-career-singapore/; insdrSV=34; ins-gaSSId=37bf3748-65aa-a5d3-b4e4-617d440566a1_1510579997; current-currency=; scs=%7B%22t%22%3A1%7D',
    'Host':'sg.jobsdb.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jobsdb.middlewares.JobsdbSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jobsdb.download_middlewares.AddHeadersMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'jobsdb.pipelines.DropDuplicatePipeline': 100,
	'jobsdb.pipelines.SaveToDBPipeline': 200
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
