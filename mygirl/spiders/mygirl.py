# -*- coding: utf-8 -*-

"""
File: mygirl.py
Author: jackdan9
Date: 2018/8/31 10:05
"""

import scrapy
import smtplib
import datetime
from email.mime.text import MIMEText
from email.header import Header
import traceback

import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class MyGirlSpider(scrapy.Spider):
    name = "mygirl"
    start_urls = [
        "http://www.weather.com.cn/weather1d/101180101.shtml",
    ]

    def parse(self, response):
        Tod_Weather_Date = response.xpath('//*[@id="today"]/div[@class="t"]/ul/li[1]/h1/text()').extract()
        Tod_Weather_Wea = response.xpath('//*[@id="today"]/div[@class="t"]/ul/li[1]/p[1]/text()').extract()
        Tod_Weather_Tem = response.xpath('//*[@id="today"]/div[@class="t"]/ul/li[1]/p[2]/span/text()').extract()
        Tod_Weather_Wind_Con = response.xpath('//*[@id="today"]/div[@class="t"]/ul/li[1]/p[3]/span/@title').extract()
        Tod_Weather_Wind_Num = response.xpath('//*[@id="today"]/div[@class="t"]/ul/li[1]/p[3]/span/text()').extract()

        Tom_Weather_Date = response.xpath('//*[@id="today"]/div[@class="t"]/ul/li[2]/h1/text()').extract()
        Tom_Weather_Wea = response.xpath('//*[@id="today"]/div[@class="t"]/ul/li[2]/p[1]/text()').extract()
        Tom_Weather_Tem = response.xpath('//*[@id="today"]/div[@class="t"]/ul/li[2]/p[2]/span/text()').extract()
        Tom_Weather_Wind_Con = response.xpath('//*[@id="today"]/div[@class="t"]/ul/li[2]/p[3]/span/@title').extract()
        Tom_Weather_Wind_Num = response.xpath('//*[@id="today"]/div[@class="t"]/ul/li[2]/p[3]/span/text()').extract()

        today = datetime.datetime.today()
        anniversary = datetime.datetime(2018, 3, 14)
        loving_days = (today - anniversary).days

        location = '郑州-河南工业大学(呆瓜的大学)'
        loving_word = '爱你呦！！！'

        if((Tod_Weather_Wea[0].find(u'雨')) != -1):
            lst = [
                '<html><body>' +
                '<h3 style="font-family: cursive; font-weight: 500; font-size: 1，17em;">你好, 呆瓜:<br><br></h3>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天是' + today.strftime('%Y-%m-%d') +
                '，地点是' + str(location) +
                ':<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">首先，今天已经是我们相恋的第' + str(
                    loving_days) +
                '天了喔。然后大兵就要来播送天气预报了！！<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天日期:' + str(Tod_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天天气情况:' + str(
                    Tod_Weather_Wea[0]) +
                '(记得带伞哦)<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天温度:' + str(Tod_Weather_Tem[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风向:' + str(
                    Tod_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风的级数:' + str(
                    Tod_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天日期:' + str(Tom_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天天气情况:' + str(
                    Tom_Weather_Wea[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天温度:' + str(Tom_Weather_Tem[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风向:' + str(
                    Tom_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风的级数:' + str(
                    Tom_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; color: red; font-size: 1em;">' + loving_word +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">'
                '<br></h4>' +
                '</body></html>']


        elif((Tom_Weather_Wea[0].find(u'雨')) != -1):
            lst = [
                '<html><body>' +
                '<h3 style="font-family: cursive; font-weight: 500; font-size: 1，17em;">你好, 呆瓜:<br><br></h3>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天是' + today.strftime('%Y-%m-%d') +
                '，地点是' + str(location) +
                ':<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">首先，今天已经是我们相恋的第' + str(
                    loving_days) +
                '天了喔。然后大兵就要来播送天气预报了！！<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天日期:' + str(Tod_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天天气情况:' + str(
                    Tod_Weather_Wea[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天温度:' + str(Tod_Weather_Tem[0]) +
                '℃<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风向:' + str(
                    Tod_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风的级数:' + str(
                    Tod_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天日期:' + str(Tom_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天天气情况:' + str(
                    Tom_Weather_Wea[0]) +
                '(记得带伞哦)<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天温度:' + str(Tom_Weather_Tem[0]) +
                '℃<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风向:' + str(
                    Tom_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风的级数:' + str(
                    Tom_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; color: red; font-size: 1em;">' + loving_word +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '</h4>' +
                '</body></html>']


        elif(((Tod_Weather_Wea[0].find(u'雨')) != -1) and ((Tom_Weather_Wea[0].find(u'雨')) != -1)):
            lst = [
                '<html><body>' +
                '<h3 style="font-family: cursive; font-weight: 500; font-size: 1，17em;">你好, 呆瓜:<br><br></h3>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天是' + today.strftime('%Y-%m-%d') +
                '，地点是' + str(location) +
                ':<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">首先，今天已经是我们相恋的第' + str(
                    loving_days) +
                '天了喔。然后大兵就要来播送天气预报了！！<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天日期:' + str(Tod_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天天气情况:' + str(
                    Tod_Weather_Wea[0]) +
                '(记得带伞哦)<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天温度:' + str(Tod_Weather_Tem[0]) +
                '℃<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风向:' + str(
                    Tod_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风的级数:' + str(
                    Tod_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天日期:' + str(Tom_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天天气情况:' + str(
                    Tom_Weather_Wea[0]) +
                '(记得带伞哦)<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天温度:' + str(Tom_Weather_Tem[0]) +
                '℃<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风向:' + str(
                    Tom_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风的级数:' + str(
                    Tom_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; color: red; font-size: 1em;">' + loving_word +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '</h4>' +
                '</body></html>']


        elif(28 <= int(Tod_Weather_Tem[0]) < 50):
            lst = [
                '<html><body>' +
                '<h3 style="font-family: cursive; font-weight: 500; font-size: 1，17em;">你好, 呆瓜:<br><br></h3>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天是' + today.strftime('%Y-%m-%d') +
                '，地点是' + str(location) +
                ':<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">首先，今天已经是我们相恋的第' + str(
                    loving_days) +
                '天了喔。然后大兵就要来播送天气预报了！！<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天日期:' + str(Tod_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天天气情况:' + str(
                    Tod_Weather_Wea[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天温度:' + str(Tod_Weather_Tem[0]) +
                '℃(记得涂防晒霜哦)<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风向:' + str(
                    Tod_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风的级数:' + str(
                    Tod_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天日期:' + str(Tom_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天天气情况:' + str(
                    Tom_Weather_Wea[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天温度:' + str(Tom_Weather_Tem[0]) +
                '℃<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风向:' + str(
                    Tom_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风的级数:' + str(
                    Tom_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; color: red; font-size: 1em;">' + loving_word +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '</h4>' +
                '</body></html>']


        elif (-15 <= int(Tod_Weather_Tem[0]) < 10):
            lst = [
                '<html><body>' +
                '<h3 style="font-family: cursive; font-weight: 500; font-size: 1，17em;">你好, 呆瓜:<br><br></h3>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天是' + today.strftime('%Y-%m-%d') +
                '，地点是' + str(location) +
                ':<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">首先，今天已经是我们相恋的第' + str(
                    loving_days) +
                '天了喔。然后大兵就要来播送天气预报了！！<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天日期:' + str(Tod_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天天气情况:' + str(
                    Tod_Weather_Wea[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天温度:' + str(Tod_Weather_Tem[0]) +
                '℃(记得穿厚些)<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风向:' + str(
                    Tod_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风的级数:' + str(
                    Tod_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天日期:' + str(Tom_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天天气情况:' + str(
                    Tom_Weather_Wea[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天温度:' + str(Tom_Weather_Tem[0]) +
                '℃<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风向:' + str(
                    Tom_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风的级数:' + str(
                    Tom_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; color: red; font-size: 1em;">' + loving_word +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '</h4>' +
                '</body></html>']


        elif(28 <= int(Tom_Weather_Tem[0]) < 50):
            lst = [
                '<html><body>' +
                '<h3 style="font-family: cursive; font-weight: 500; font-size: 1，17em;">你好, 呆瓜:<br><br></h3>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天是' + today.strftime('%Y-%m-%d') +
                '，地点是' + str(location) +
                ':<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">首先，今天已经是我们相恋的第' + str(
                    loving_days) +
                '天了喔。然后大兵就要来播送天气预报了！！<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天日期:' + str(Tod_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天天气情况:' + str(
                    Tod_Weather_Wea[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天温度:' + str(Tod_Weather_Tem[0]) +
                '℃<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风向:' + str(
                    Tod_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风的级数:' + str(
                    Tod_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天日期:' + str(Tom_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天天气情况:' + str(
                    Tom_Weather_Wea[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天温度:' + str(Tom_Weather_Tem[0]) +
                '℃(记得涂防晒霜哦)<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风向:' + str(
                    Tom_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风的级数:' + str(
                    Tom_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; color: red; font-size: 1em;">' + loving_word +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '</h4>' +
                '</body></html>']


        elif(-15 <= int(Tom_Weather_Tem[0]) < 10):
            lst = [
                '<html><body>' +
                '<h3 style="font-family: cursive; font-weight: 500; font-size: 1，17em;">你好, 呆瓜:<br><br></h3>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天是' + today.strftime('%Y-%m-%d') +
                '，地点是' + str(location) +
                ':<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">首先，今天已经是我们相恋的第' + str(
                    loving_days) +
                '天了喔。然后大兵就要来播送天气预报了！！<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天日期:' + str(Tod_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天天气情况:' + str(
                    Tod_Weather_Wea[0]) +
                '(记得带伞哦)<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天温度:' + str(Tod_Weather_Tem[0]) +
                '℃<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风向:' + str(
                    Tod_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风的级数:' + str(
                    Tod_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天日期:' + str(Tom_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天天气情况:' + str(
                    Tom_Weather_Wea[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天温度:' + str(Tom_Weather_Tem[0]) +
                '℃(记得穿厚些哦)<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风向:' + str(
                    Tom_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风的级数:' + str(
                    Tom_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; color: red; font-size: 1em;">' + loving_word +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '</h4>' +
                '</body></html>']


        elif((28 <= int(Tod_Weather_Tem[0]) < 50) and (28 <= int(Tom_Weather_Tem[0]) < 50)):
            lst = [
                '<html><body>' +
                '<h3 style="font-family: cursive; font-weight: 500; font-size: 1，17em;">你好, 呆瓜:<br><br></h3>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天是' + today.strftime('%Y-%m-%d') +
                '，地点是' + str(location) +
                ':<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">首先，今天已经是我们相恋的第' + str(
                    loving_days) +
                '天了喔。然后大兵就要来播送天气预报了！！<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天日期:' + str(Tod_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天天气情况:' + str(
                    Tod_Weather_Wea[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天温度:' + str(Tod_Weather_Tem[0]) +
                '℃(记得涂防晒霜哦)<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风向:' + str(
                    Tod_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风的级数:' + str(
                    Tod_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天日期:' + str(Tom_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天天气情况:' + str(
                    Tom_Weather_Wea[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天温度:' + str(Tom_Weather_Tem[0]) +
                '℃(记得涂防晒霜哦)<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风向:' + str(
                    Tom_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风的级数:' + str(
                    Tom_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; color: red; font-size: 1em;">' + loving_word +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '</h4>' +
                '</body></html>']


        elif((-15 <= int(Tod_Weather_Tem[0]) < 10) and (-15 <= int(Tom_Weather_Tem[0]) < 10)):
            lst = [
                '<html><body>' +
                '<h3 style="font-family: cursive; font-weight: 500; font-size: 1，17em;">你好, 呆瓜:<br><br></h3>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天是' + today.strftime('%Y-%m-%d') +
                '，地点是' + str(location) +
                ':<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">首先，今天已经是我们相恋的第' + str(
                    loving_days) +
                '天了喔。然后大兵就要来播送天气预报了！！<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天日期:' + str(Tod_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天天气情况:' + str(
                    Tod_Weather_Wea[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天温度:' + str(Tod_Weather_Tem[0]) +
                '℃(记得穿厚些哦)<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风向:' + str(
                    Tod_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风的级数:' + str(
                    Tod_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天日期:' + str(Tom_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天天气情况:' + str(
                    Tom_Weather_Wea[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天温度:' + str(Tom_Weather_Tem[0]) +
                '℃(记得穿厚些哦)<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风向:' + str(
                    Tom_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风的级数:' + str(
                    Tom_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; color: red; font-size: 1em;">' + loving_word +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '</h4>' +
                '</body></html>']


        else:
            lst = [
                '<html><body>' +
                '<h3 style="font-family: cursive; font-weight: 500; font-size: 1，17em;">你好, 呆瓜:<br><br></h3>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天是' + today.strftime('%Y-%m-%d') +
                '，地点是' + str(location) +
                ':<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">首先，今天已经是我们相恋的第' + str(
                    loving_days) +
                '天了喔。然后大兵就要来播送天气预报了！！<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天日期:' + str(Tod_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天天气情况:' + str(
                    Tod_Weather_Wea[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天温度:' + str(Tod_Weather_Tem[0]) +
                '℃<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风向:' + str(
                    Tod_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">今天风的级数:' + str(
                    Tod_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天日期:' + str(Tom_Weather_Date[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天天气情况:' + str(
                    Tom_Weather_Wea[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天温度:' + str(Tom_Weather_Tem[0]) +
                '℃<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风向:' + str(
                    Tom_Weather_Wind_Con[0]) +
                '<br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; font-size: 1em;">明天风的级数:' + str(
                    Tom_Weather_Wind_Num[0]) +
                '<br><br></h4>' +
                '<h4 style="font-family: cursive; font-weight: 300; color: red; font-size: 1em;">' + loving_word +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/66.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/65.gif">' +
                '<img src="https://rescdn.qqmail.com/zh_CN/images/mo/DEFAULT2/52.gif">' +
                '</h4>' +
                '</body></html>']

        # # It is receiver email word.
        # mailto_list = "*********@qq.com"
        # mail_host = "smtp.qq.com"
        # # It is your email word.
        # mail_user = "********@qq.com"
        # # It is your password
        # mail_pass = "**********"
        # It is receiver email word.

        content = ''.join(lst)
        msg = MIMEText(content, _subtype='html', _charset='utf-8')
        msg['From'] = mail_user
        msg['To'] = mailto_list
        msg['Subject'] = Header('大兵男朋友的日常问候', 'utf-8')
        try:
            s = smtplib.SMTP_SSL(mail_host, 465)
            s.login(mail_user, mail_pass)
            s.sendmail(mail_user, mailto_list, msg.as_string())
            s.close()
        except Exception as e:
            print(e)

