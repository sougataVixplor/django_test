from distutils.log import info
from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.selector import Selector
import re
import os
import pandas as pd



pageCount=0
productarr=[]
actualPrice=[]
discountPrice=[]
prating=[]


def Flipkart(url,pageCount):
    
    domain="https://www.flipkart.com"

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    
    print(url)
    res=requests.get(url,headers=headers)

    response=Selector(res)
    res_n=response.css('body')
    
    for x in res_n[0].xpath(".//div[@class='_1AtVbE col-12-12']/div[@class='_13oc-S']"):
        gridFlag=False
        grid=x.xpath(".//div[@class='_4ddWXP']")


        data=x.xpath('.//a')
        if len(data)!=0:
            link=data[0].xpath('.//@href').extract()
            link=domain+link[0]
            # print('link:',link)
            details=x.xpath(".//div[@class='_3pLy-c row']")
            # print(price)
            dp=details[0].xpath('.//div[@class="_30jeq3 _1_WHN1"]//text()').extract()
            if len(dp)!=0:
                discount_price=dp[0]
            else:
                discount_price='-'

            ap=details[0].xpath('.//div[@class="_3I9_wc _27UcVY"]//text()').extract()
            if len(ap)==2:
                actual_price=ap[1]
            elif len(ap)==1:
                actual_price=ap[0]
            else:
                actual_price='-'
            
            productName=details[0].xpath('.//div[@class="_4rR01T"]//text()').extract()[0]
            rating=details[0].xpath('.//div[@class="_3LWZlK"]//text()').extract()
            # specip=data[0].xpath('.//')
            print('Product Name:',productName)
            print(discount_price)
            print(actual_price)
            productarr.append(productName)
            actualPrice.append(actual_price)
            discountPrice.append(discount_price)
            if len(rating)!=0:
                print('rating :',rating[0])
                prating.append(rating[0])
            else:
                prating.append('None')


    nextPage=res_n[0].xpath(".//div['_1AtVbE col-12-12']//nav[@class='yFHi8N']//a[@class='_1LKTO3']//@href").extract()
    if len(nextPage)!=0 and pageCount<=10:
        if len(nextPage)==1:
            nextPage=domain+nextPage[0]
        if len(nextPage)==2:
            nextPage=domain+nextPage[1]
        pageCount+=1
        
        Flipkart(nextPage,pageCount)
    
    df=pd.DataFrame()
    df['Product Name']=productarr
    df['Offer Price']=discountPrice
    df['Actual Price']=actualPrice
    df['Rating']=prating
    df.to_excel('flipkart_facewash.xlsx')

def searchProduct(searchword):
    url="https://www.flipkart.com/search?q=$searchword&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    url=url.replace('$searchword',searchword)
    
    pageCount=0
    Flipkart(url,pageCount)
    
searchProduct('facewash')

        