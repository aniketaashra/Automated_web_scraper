"""
    Author  :   Saurabh Jha
    email   :   saurabh.jha009@gmail.com
    Date    :   18th March,2021
    Time    :   12:48 am
    Place   :   Mumbai, India.
"""

import scrapy
from universities.items import UniversitiesItem


class University(scrapy.Spider):
    name = 'university'
    start_urls = ['https://en.wikipedia.org/wiki/List_of_universities_in_England']
    base_url = 'https://en.wikipedia.org'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers, callback=self.universities)

    def universities(self, response):
        links = response.css(
            '#mw-content-text > div.mw-parser-output > table > tbody > tr > td:nth-child(1) > a ::attr(href)').getall()
        for url in links:
            yield scrapy.Request(self.base_url + url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        postgrad_index = 0
        undergrad_index = 0
        student_index = 0

        # Name Of the University
        current_name = response.css(
            '#mw-content-text > div.mw-parser-output > table.infobox.vcard > caption ::text').get()

        # Former Name Of University
        former_name_list = response.css('[class*="nickname"] ::text').getall()
        former_name = ' '.join([str(elem) for elem in former_name_list if elem])

        # Location Of University
        location_list = response.css('[class*="adr"] div ::text').getall()
        location = ' '.join([str(elem) for elem in location_list if elem])
        all_data = response.css('#mw-content-text > div.mw-parser-output > table.infobox.vcard > tbody > tr').getall()
        for i in range(len(all_data)):
            if "Undergraduates" in all_data[i]:
                undergrad_index = i
            elif "Postgraduates" in all_data[i]:
                postgrad_index = i
            elif "Students" in all_data[i]:
                student_index = i
            if undergrad_index:
                undergraduates = response.css(
                    f'#mw-content-text > div.mw-parser-output > table.infobox.vcard > tbody > tr:nth-child({undergrad_index + 1}) td ::text').get()
            else:
                undergraduates = None
            if postgrad_index:
                postgraduates = response.css(
                    f'#mw-content-text > div.mw-parser-output > table.infobox.vcard > tbody > tr:nth-child({postgrad_index + 1}) td ::text').get()
            else:
                postgraduates = None
            if student_index:
                students = response.css(
                    f'#mw-content-text > div.mw-parser-output > table.infobox.vcard > tbody > tr:nth-child({student_index + 1}) td ::text').get()
            else:
                students = None
        item = UniversitiesItem()
        item['url'] = response.url
        item['current_name'] = current_name
        item['former_name'] = former_name
        item['location'] = location
        item['students'] = students
        item['undergraduates'] = undergraduates
        item['postgraduates'] = postgraduates
        yield item
