# -*- coding: utf-8 -*-
import re
import scrapy
from jobsdb.items import JobItem, EmployerItems

class JobsdbSpiderSpider(scrapy.Spider):
    name = 'jobsdb_spider'
    allowed_domains = ['jobsdb.com/sg'] #domains allowed
    start_urls = ['https://sg.jobsdb.com/sg/en/browse']

    def parse(self, response):
        sel = scrapy.Selector(response)
        category = sel.xpath('//div[@class="card"][3]/dl/dd/div/a')
        category_hrefs = category.xpath('@href').extract()
        category_titles = category.xpath('text()').extract()
        for href, title in zip(category_hrefs, category_titles):
            job_item = JobItem()
            job_item['job_category'] = title
            print('111111111------------------------------', href)
            yield scrapy.Request(url=href, callback=self.parse_job_list, dont_filter=True, meta={'job_item': job_item})


    def parse_job_list(self, response):
        job_item_old = response.meta['job_item']
        sel = scrapy.Selector(response)
        jobs = sel.xpath('//div[@class="result-sherlock-cell    branded"]/div[@class="job-main"]/h3/a')
        job_hrefs = jobs.xpath('@href').extract()
        job_titles = jobs.xpath('text()').extract()
        try:
            job_page = sel.xpath('//a[@class="pagebox current"]/span/text()').extract()[0]
        except:
            job_page = '1'
        for href, title in zip(job_hrefs, job_titles):
            job_item = JobItem()
            job_item['job_category'] = job_item_old['job_category']
            job_item['job_url'] = href
            job_item['job_title'] = title
            job_item['job_page'] = job_page
            print('222222222------------------------------', href)
            yield scrapy.Request(url=href, callback=self.parse_info, dont_filter=True, meta={'job_item': job_item})
        next = sel.xpath('//a[@class="pagebox pagebox-next"]/@href').extract()
        if next:
            yield scrapy.Request(url=next[0], callback=self.parse_job_list, dont_filter=True, meta={'job_item': job_item_old})

    def parse_info(self, response):
        job_item = response.meta['job_item']
        print(job_item['job_url'])
        employer_item = EmployerItems()
        sel = scrapy.Selector(response)

        if sel.xpath('//div[@class="primary-general-box general-data"]/p/@title').extract():
            job_post_date = sel.xpath('//div[@class="primary-general-box general-data"]/p/@title').extract()[0]
        else:
            job_post_date = ''
        if sel.xpath('//p[@class="data-ref ref-employer"]/text()').extract():
            employer_ref = str(sel.xpath('//p[@class="data-ref ref-employer"]/text()').extract()[1]).strip()
        else:
            employer_ref = ''
        if sel.xpath('//p[@class="data-ref ref-ea"]/text()').extract():
            job_EA_license = str(sel.xpath('//p[@class="data-ref ref-ea"]/text()').extract()[1]).strip()
        else:
            job_EA_license = ''
        if sel.xpath('//p[@class="data-ref ref-jobsdb"]/text()').extract():
            if len(sel.xpath('//p[@class="data-ref ref-jobsdb"]/text()').extract()) == 2:
                job_ref = str(sel.xpath('//p[@class="data-ref ref-jobsdb"]/text()').extract()[1]).strip()
            else:
                job_ref = str(sel.xpath('//p[@class="data-ref ref-jobsdb"]/text()').extract()[0]).strip()
        else:
            job_ref = ''

        employee_info = sel.xpath('//div[@class="primary-meta-box row meta-group"]')
        if employee_info.xpath('div[@class="primary-meta-box row meta-employmenttype"]/p/text()'):
            job_employment_type = str(employee_info.xpath('div[@class="primary-meta-box row meta-employmenttype"]/p/text()').extract()[0]).strip()
        else:
            job_employment_type = ''
        if employee_info.xpath('div[@class="primary-meta-box row meta-salary"]/p/span/text()').extract():
            job_salary = str(employee_info.xpath('div[@class="primary-meta-box row meta-salary"]/p/span/text()').extract()[0]).strip()
        else:
            job_salary = ''
        if employee_info.xpath('div[@class="primary-meta-box row meta-lv"]/p/span/b/text()').extract():
            employee_career_level = str(employee_info.xpath('div[@class="primary-meta-box row meta-lv"]/p/span/b/text()').extract()[0]).strip()
        else:
            employee_career_level = ''
        if employee_info.xpath('div[@class="primary-meta-box row meta-exp"]/p/span/b/text()').extract():
            employee_exp = str(employee_info.xpath('div[@class="primary-meta-box row meta-exp"]/p/span/b/text()').extract()[0]).strip()
        else:
            employee_exp = ''
        if employee_info.xpath('div[@class="primary-meta-box row meta-edu"]/p/span/text()').extract():
            employee_qualification = str(employee_info.xpath('div[@class="primary-meta-box row meta-edu"]/p/span/text()').extract()[0]).strip()
        else:
            employee_qualification = ''
        if employee_info.xpath('div[@class="primary-meta-box row meta-industry"]/p/a/text()').extract():
            employer_industry = str(employee_info.xpath('div[@class="primary-meta-box row meta-industry"]/p/a/text()').extract()[0]).strip()
        else:
            employer_industry = ''

        if sel.xpath('//a[@class="loc-link"]/@href').extract():
            employer_location = sel.xpath('//a[@class="loc-link"]/text()').extract()[0]
        else:
            employer_location = ''
        if sel.xpath('//h2[@class="jobad-header-company ad-y-auto-txt1"]/text()').extract():
            employer_name = str(sel.xpath('//h2[@class="jobad-header-company ad-y-auto-txt1"]/text()').extract()[0]).strip()
        else:
            employer_name = ''
        if sel.xpath('string(//span[@itemprop="description"])').extract():
            job_description = ' '.join(re.findall('[\w,.:;]+', sel.xpath('string(//span[@itemprop="description"])').extract()[0]))
        else:
            job_description = ''
        if sel.xpath('string(//div[@class="secondary-profile-detail"])').extract():
            employer_description = ' '.join(re.findall('[\w,.:;]+', sel.xpath('string(//div[@class="secondary-profile-detail"])').extract()[0]))
        else:
            employer_description = ''
        if sel.xpath('//p[@class="meta-link"]/a/@href').extract():
            employer_website = sel.xpath('//p[@class="meta-link"]/a/@href').extract()[0]
        else:
            employer_website = ''

        job_item['job_post_date'] = job_post_date
        job_item['job_ref'] = job_ref
        job_item['job_EA_license'] = job_EA_license
        job_item['job_description'] = job_description
        job_item['job_employment_type'] = job_employment_type
        job_item['job_salary'] = job_salary
        job_item['employee_career_level'] = employee_career_level
        job_item['employee_exp'] = employee_exp
        job_item['employee_qualification'] = employee_qualification
        job_item['employer_ref'] = employer_ref
        job_item['employer_name'] = employer_name

        employer_item['employer_ref'] = employer_ref
        employer_item['employer_location'] = employer_location
        employer_item['employer_name'] = employer_name
        employer_item['employer_industry'] = employer_industry
        employer_item['employer_description'] = employer_description
        employer_item['employer_website'] = employer_website

        yield job_item
        yield employer_item



