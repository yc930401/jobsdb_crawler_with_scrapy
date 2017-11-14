# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from scrapy.exceptions import DropItem
from jobsdb.items import JobItem, EmployerItems

class DropDuplicatePipeline(object):
    def __init__(self):
        self.jobs_seen = set()
        self.companies_seen = set()

    def process_item(self, item, spider):
        if isinstance(item, JobItem):
            job = item['job_category'] + item['job_title'] + item['job_employment_type'] \
                + item['employee_career_level'] + item['employee_exp'] + item['employee_qualification'] \
                + item['employer_name']
            if job in self.jobs_seen:
                raise DropItem("Duplicate job found: %s" % item)
            else:
                self.jobs_seen.add(job)

        elif isinstance(item, EmployerItems):
            company = item['employer_name'] + item['employer_industry']
            if company in self.companies_seen:
                raise DropItem("Duplicate company found: %s" % item)
            else:
                self.companies_seen.add(company)
        return item


class SaveToDBPipeline(object):
    def open_spider(self, spider):
        db_path = 'Jobsdb.db'
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        if isinstance(item, JobItem):
            job_keys = ['job_category', 'job_page', 'job_url', 'job_title', 'job_post_date', 'job_ref',
                        'job_EA_license', 'job_description', 'job_employment_type', 'job_salary',
                        'employee_career_level', 'employee_exp', 'employee_qualification', 'employer_ref',
                        'employer_name']
            job_values = "','".join([item[key] for key in job_keys])
            print(item.values())
            query_str = "INSERT INTO job_info VALUES ('{}');".format(job_values)
            create_str = "CREATE TABLE if not exists job_info({});".format(",".join(job_keys))
            print(create_str)
            self.c.execute(create_str)


        elif isinstance(item, EmployerItems):
            print(item.keys())
            company_keys = ['employer_ref', 'employer_name', 'employer_industry', 'employer_location',
                            'employer_website', 'employer_description']
            company_values = "','".join([item[key] for key in company_keys])
            print(item.values())
            query_str = "INSERT INTO company_info VALUES ('{}');".format(company_values)
            create_str = "CREATE TABLE if not exists company_info({});".format(",".join(company_keys))
            print(create_str)
            self.c.execute(create_str)


        print(query_str)
        self.c.execute(query_str)
        return item
