# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsdbItem(scrapy.Item):
    pass

class JobItem(scrapy.Item):

    job_category = scrapy.Field()
    job_page = scrapy.Field()
    job_url = scrapy.Field()
    job_title = scrapy.Field()
    job_post_date = scrapy.Field()
    job_ref = scrapy.Field()
    job_EA_license = scrapy.Field()
    job_description = scrapy.Field()
    job_employment_type = scrapy.Field()
    job_salary = scrapy.Field()

    employee_career_level = scrapy.Field()
    employee_exp = scrapy.Field()
    employee_qualification = scrapy.Field()

    employer_ref=scrapy.Field()
    employer_name = scrapy.Field()


class EmployerItems(scrapy.Item):

    employer_ref = scrapy.Field()
    employer_location = scrapy.Field()
    employer_name = scrapy.Field()
    employer_industry = scrapy.Field()
    employer_description = scrapy.Field()
    employer_website = scrapy.Field()

