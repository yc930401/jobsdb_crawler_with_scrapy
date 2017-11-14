# jobsdb_crawler_with_scrapy

Crawl jobs in Singapore posted in JobsDB using scrapy framwwork.

## Introduction

This is my first time using scrapy framework to crawl data. It is a very powerful framework. Please find detailed scrapy introduction in the references below. </br>
![scrapy](/scrapy_framework.jpg)

## Steps

1. Analyze the website we want to crawl, the htmls and the information we need.
2. Create a new scrapy project: scrapy startproject jobsdb
3. Create a spider: scrapy genspider jobsdb_spider https://sg.jobsdb.com/sg
4. Open project with Pycharm and write spiders, items, piplines and settings.
5. Run project: scrapy crawl jobsdb_spider.

## Result

1. Job Information
</br>
![scrapy](/job_info.jpg) </br>
2. Company Information
</br>
![scrapy](/company_info.jpg) </br>

## References
https://doc.scrapy.org/en/0.20/topics/architecture.html </br>
https://www.tutorialspoint.com/scrapy/scrapy_command_line_tools.htm
