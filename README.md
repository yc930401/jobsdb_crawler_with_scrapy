# jobsdb_crawler_with_scrapy

Crawl jobs in Singapore posted in JobsDB using scrapy framwwork.

## Introduction

This is my first time using scrapy framework to crawl data. It is a very powerful framework. Please find detailed scrapy introduction in the references below. </br>
![scrapy](/scrapy_framework.jpg) </br>
> Scrapy Engine: The engine is responsible for controlling the data flow between all components of the system, and triggering events when certain actions occur. </br>
> Scheduler: The Scheduler receives requests from the engine and enqueues them for feeding them later (also to the engine) when the engine requests them. </br>
> Downloader: The Downloader is responsible for fetching web pages and feeding them to the engine which, in turn, feeds them to the spiders. </br>
> Spiders: Spiders are custom classes written by Scrapy users to parse responses and extract items (aka scraped items) from them or additional URLs (requests) to follow. Each spider is able to handle a specific domain (or group of domains). </br>
> Item Pipeline: The Item Pipeline is responsible for processing the items once they have been extracted (or scraped) by the spiders. Typical tasks include cleansing, validation and persistence (like storing the item in a database). </br>
> Downloader middlewares: Downloader middlewares are specific hooks that sit between the Engine and the Downloader and process requests when they pass from the Engine to the Downloader, and responses that pass from Downloader to the Engine. They provide a convenient mechanism for extending Scrapy functionality by plugging custom code. </br>
> Spider middlewares: Spider middlewares are specific hooks that sit between the Engine and the Spiders and are able to process spider input (responses) and output (items and requests). They provide a convenient mechanism for extending Scrapy functionality by plugging custom code.

## Steps

1. Analyze the website we want to crawl, the htmls and the information we need.
2. Create a new scrapy project: scrapy startproject jobsdb
3. Create a spider: scrapy genspider jobsdb_spider https://sg.jobsdb.com/sg
4. Open project with Pycharm and write spiders, items, piplines and settings.
5. Run project: scrapy crawl jobsdb_spider.

## Result

Job Information </br>
![scrapy](/job_info.jpg)  </br>
</br> </br>
Company Information </br>
![scrapy](/company_info.jpg) </br>

## References
https://doc.scrapy.org/en/0.20/topics/architecture.html </br>
https://www.tutorialspoint.com/scrapy/scrapy_command_line_tools.htm
