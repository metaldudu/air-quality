#!/usr/bin/python3
#coding=utf-8
# 抓取 iqair.cn 空气质量和天气

import urllib.request
import requests
from bs4 import BeautifulSoup  

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

linkurl = 'https://www.iqair.cn/cn/china/hebei/shijiazhuang/xinhua' #url对应空气监测站点
#air_site = linkurl.split('/')[-1] #获取唯一的站点名称

res = requests.get(linkurl, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')


def PmOutput(): 
    air_aqi = soup.find("p", class_="aqi-value__value").string #aqi
    
    air_all = soup.find("table", class_="aqi-overview-detail__other-pollution-table") #空气质量table

    pm25 = air_all.find_all('tr')[1]  # 第二个tr
    pm25_num = pm25.find_all('td')[2].select('span')[0].string #pm2.5

    pm10 = air_all.find_all('tr')[2]
    pm10_num = pm10.find_all('td')[2].select('span')[0].string #pm10

    weather = soup.find("div", class_="weather") #天气部分
    temperature = weather.table.find_all('tr')[1].find_all('td')[1].string #温度
    humidity = weather.table.find_all('tr')[2].find_all('td')[1].string #湿度

    air_output = str(temperature) + ' | ' + str(humidity) + '\nAQI: ' + str(air_aqi) + ' | PM2.5: ' + str(pm25_num) + ' | PM10: ' + str(pm10_num)

    print(air_output) 

PmOutput()


