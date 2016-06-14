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
        print '*'*10
        print 'len(sites):',len(sites)
        for site in sites:
            item=PojItem()
            item['title']=site.xpath("text()").extract()[0]
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
        print response.body
        sel=Selector(response)
        Time_Limit=sel.xpath('//div[@class="plm"]/table/tr[1]/td[1]/text()').extract()[0]
       # Time_Limit=Time_Limit.xpath("text()").extract()[0]
        
        print "length of Time_Limit:",len(Time_Limit)
        Memory_Limit=sel.xpath('//div[@class="plm"]/table/tr[1]/td[3]/text()').extract()[0]
        print 'len(Memory_Limit)',len(Memory_Limit)
        DescriptionTag=sel.xpath('//div[@class="ptx"][1]')
        print '!'*20
        print 'length of Des:',len(DescriptionTag)
        Description=DescriptionTag.xpath('string(.)').extract()[0]
        InputTag=sel.xpath('//div[@class="ptx"][2]')
        Input=InputTag.xpath('string(.)').extract()[0]
        OutputTag=sel.xpath('//div[@class="ptx"]')
        if  OutputTag:
            print "*"*20
            print "length of OutputTag:",len(OutputTag)

        if OutputTag[2].xpath('string(.)').extract():
            Output=OutputTag[2].xpath('string(.)').extract()[0]
        else:
            Output='There is nothing!'
        Sample_InputTag=sel.xpath('//pre[@class="sio"][1]')
        Sample_Input=Sample_InputTag.xpath('string(.)').extract()[0]
        Sample_OutputTag=sel.xpath('//pre[@class="sio"][2]')
        Sample_Output=Sample_OutputTag.xpath('string(.)').extract()[0]

        print 'length of Sample_InputTag:',len(Sample_InputTag)
        item=response.meta['item']
        item['Time_Limit']=Time_Limit
        item['Memory_Limit']=Memory_Limit
        item['Description']=Description
        item['Input']=Input
        item['Output']=Output

        item['Sample_Input']=Sample_Input

        item['Sample_Output']=Sample_Output
        return item
