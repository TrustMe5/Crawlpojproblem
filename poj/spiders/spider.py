#!/usr/bin/env python
# coding=utf-8
from scrapy.spiders import Spider
from poj.items import PojItem
from bs4 import BeautifulSoup
from scrapy.http import Request
from scrapy.selector import Selector

class PojSpider(Spider):
    name='poj'
    allowed_domains=['poj.org']
    download_delay=0.1
    start_urls=['http://poj.org/problemlist?volume=1']
   # def start_requests(self):
   #     headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'}
   #     print 'here'*10
   #     yield Request('http://poj.org/problemlist?volume=1',headers=headers,callback=self.parse)


#    def parse(self,response):
#    #    item=PojItem()
#    #    item['title']='hello word'
#    #    item['link']='www.'
#    #    item['content']='wdcwdc'
#    #    return item
#        soup=BeautifulSoup(response.body)
#        tags=soup.findAll("td",attrs={"align":"left"})
#        print 'tags:',tags
#        print '!'*10
#        for tag in tags:
#            item=PojItem()
#            item['title']=tag.text
#            item['link']=tag.find('a').get('href')
#            next_url='http://poj.org/'+item['link']
#            print next_url
#            yield Request(url=next_url,meta={'item':item},callback=self.parse2)

    def parse(self,response):
        sel=Selector(response)
        sites=sel.xpath('//tr[@align="center"]/td[@align="left"]/a')
        for site in sites:
            item=PojItem()
            item['title']=site.xpath("text()").extract()
            item['link']=site.xpath("@href").extract()
            next_url="http://poj.org/"+item['link'][0]
            item['link']=next_url
            print next_url
            yield Request(url=next_url,meta={'item':item},callback=self.parse2)



   # def parse2(self,response):
   #     soup=BeautifulSoup(response.body)
   #     tag=soup.find("div",attrs={"class":"rich_media_content","id":"js_content"})
   #     content_list=[tag_i.text for tag_i in tag.findAll('p')]
   #     content="".join(content_list)
   #    # content='wdc'
   #     item=response.meta['item']
   #     item['content']=content
   #     return item

    def parse2(self,response):
        sel=Selector(response)
        tags=sel.xpath('//div[@class="ptx"]')
        #content_list=tags[0].xpath("text()").extract()
        content_list=[''.join(tag.xpath("text()").extract()) for tag in tags]
        print type(content_list)
        print 'content_list:',content_list
       # print 'content_list:',content_list
        content="".join(content_list)
        item=response.meta['item']
        item['content']=content
        return item
