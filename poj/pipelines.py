# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import pandas as pd
import csv
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class PojPipeline(object):
    def __init__(self):
        self.file=open('poj.csv','a')
    def process_item(self, item, spider):
        open_file_object=csv.writer(self.file)
        open_file_object.writerow([item["title"],item["link"],item["Time_Limit"],item["Memory_Limit"],item["Description"],item["Input"],item["Output"],item["Sample_Input"],item["Sample_Output"]])
        #line=json.dumps(dict(item))+"\n"
        #self.file.write(line.decode('unicode_escape'))
        return item
