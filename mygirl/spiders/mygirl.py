# -*- coding: utf-8 -*-

import scrapy
import smtplib
import datetime
from email.mime.text import MIMEText
from email.header import Header
import traceback

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

        # if('雨' in Tod_Weather_Wea[0]):
        if((Tod_Weather_Wea[0].find(u'雨')) != -1):
            lst = [u'你好，呆瓜:\n\n\t'
                   u'今天是%s\n\t '
                   u'首先，今天已经是我们相恋的第%s天了喔。然后大兵就要来播送天气预报了！！\n\n\t'
                   u'今天日期:%s\n'
                   u'今天天气情况:%s(记得带伞哦)\n'
                   u'今天温度:%s℃\n'
                   u'今天风向:%s\n'
                   u'今天风的级数:%s\n\n'
                   u'明天日期:%s\n'
                   u'明天天气情况:%s\n'
                   u'明天温度:%s℃\n'
                   u'明天风向:%s\n'
                   u'明天风的级数:%s\n\n' % (
                   today.strftime('%Y-%m-%d'), loving_days, Tod_Weather_Date[0], Tod_Weather_Wea[0], Tod_Weather_Tem[0],
                   Tod_Weather_Wind_Con[0], Tod_Weather_Wind_Num[0], Tom_Weather_Date[0], Tom_Weather_Wea[0],
                   Tom_Weather_Tem[0], Tom_Weather_Wind_Con[0], Tom_Weather_Wind_Num[0])]
        # elif('雨' in Tom_Weather_Wea[0]):
        elif((Tom_Weather_Wea[0].find(u'雨')) != -1):
            lst = [u'你好，呆瓜:\n\n\t'
                   u'今天是%s\n\t '
                   u'首先，今天已经是我们相恋的第%s天了喔。然后大兵就要来播送天气预报了！！\n\n\t'
                   u'今天日期:%s\n'
                   u'今天天气情况:%s\n'
                   u'今天温度:%s℃\n'
                   u'今天风向:%s\n'
                   u'今天风的级数:%s\n\n'
                   u'明天日期:%s\n'
                   u'明天天气情况:%s(记得带伞哦)\n'
                   u'明天温度:%s℃\n'
                   u'明天风向:%s\n'
                   u'明天风的级数:%s\n\n' % (
                       today.strftime('%Y-%m-%d'), loving_days, Tod_Weather_Date[0], Tod_Weather_Wea[0],
                       Tod_Weather_Tem[0],
                       Tod_Weather_Wind_Con[0], Tod_Weather_Wind_Num[0], Tom_Weather_Date[0], Tom_Weather_Wea[0],
                       Tom_Weather_Tem[0], Tom_Weather_Wind_Con[0], Tom_Weather_Wind_Num[0])]
        # elif(('雨' in Tod_Weather_Wea[0]) and ('雨' in Tom_Weather_Wea[0])):
        elif(((Tod_Weather_Wea[0].find(u'雨')) != -1) and ((Tom_Weather_Wea[0].find(u'雨')) != -1)):
            lst = [u'你好，呆瓜:\n\n\t'
                   u'今天是%s\n\t '
                   u'首先，今天已经是我们相恋的第%s天了喔。然后大兵就要来播送天气预报了！！\n\n\t'
                   u'今天日期:%s\n'
                   u'今天天气情况:%s(记得带伞哦)\n'
                   u'今天温度:%s℃\n'
                   u'今天风向:%s\n'
                   u'今天风的级数:%s\n\n'
                   u'明天日期:%s\n'
                   u'明天天气情况:%s(记得带伞哦)\n'
                   u'明天温度:%s℃\n'
                   u'明天风向:%s\n'
                   u'明天风的级数:%s\n\n' % (
                       today.strftime('%Y-%m-%d'), loving_days, Tod_Weather_Date[0], Tod_Weather_Wea[0],
                       Tod_Weather_Tem[0],
                       Tod_Weather_Wind_Con[0], Tod_Weather_Wind_Num[0], Tom_Weather_Date[0], Tom_Weather_Wea[0],
                       Tom_Weather_Tem[0], Tom_Weather_Wind_Con[0], Tom_Weather_Wind_Num[0])]
        elif(28 <= int(Tod_Weather_Tem[0]) < 50):
            lst = [u'你好，呆瓜:\n\n\t'
                   u'今天是%s\n\t '
                   u'首先，今天已经是我们相恋的第%s天了喔。然后大兵就要来播送天气预报了！！\n\n\t'
                   u'今天日期:%s\n'
                   u'今天天气情况:%s\n'
                   u'今天温度:%s℃(记得涂防晒霜哦)\n'
                   u'今天风向:%s\n'
                   u'今天风的级数:%s\n\n'
                   u'明天日期:%s\n'
                   u'明天天气情况:%s\n'
                   u'明天温度:%s℃\n'
                   u'明天风向:%s\n'
                   u'明天风的级数:%s\n\n' % (
                   today.strftime('%Y-%m-%d'), loving_days, Tod_Weather_Date[0], Tod_Weather_Wea[0], Tod_Weather_Tem[0],
                   Tod_Weather_Wind_Con[0], Tod_Weather_Wind_Num[0], Tom_Weather_Date[0], Tom_Weather_Wea[0],
                   Tom_Weather_Tem[0], Tom_Weather_Wind_Con[0], Tom_Weather_Wind_Num[0])]
        elif (-15 <= int(Tod_Weather_Tem[0]) < 10):
            lst = [u'你好，呆瓜:\n\n\t'
                   u'今天是%s\n\t '
                   u'首先，今天已经是我们相恋的第%s天了喔。然后大兵就要来播送天气预报了！！\n\n\t'
                   u'今天日期:%s\n'
                   u'今天天气情况:%s\n'
                   u'今天温度:%s℃(记得穿厚些哦)\n'
                   u'今天风向:%s\n'
                   u'今天风的级数:%s\n\n'
                   u'明天日期:%s\n'
                   u'明天天气情况:%s\n'
                   u'明天温度:%s℃\n'
                   u'明天风向:%s\n'
                   u'明天风的级数:%s\n\n' % (
                       today.strftime('%Y-%m-%d'), loving_days, Tod_Weather_Date[0], Tod_Weather_Wea[0],
                       Tod_Weather_Tem[0],
                       Tod_Weather_Wind_Con[0], Tod_Weather_Wind_Num[0], Tom_Weather_Date[0], Tom_Weather_Wea[0],
                       Tom_Weather_Tem[0], Tom_Weather_Wind_Con[0], Tom_Weather_Wind_Num[0])]
        elif(28 <= int(Tom_Weather_Tem[0]) < 50):
            lst = [u'你好，呆瓜:\n\n\t'
                   u'今天是%s\n\t '
                   u'首先，今天已经是我们相恋的第%s天了喔。然后大兵就要来播送天气预报了！！\n\n\t'
                   u'今天日期:%s\n'
                   u'今天天气情况:%s\n'
                   u'今天温度:%s℃\n'
                   u'今天风向:%s\n'
                   u'今天风的级数:%s\n\n'
                   u'明天日期:%s\n'
                   u'明天天气情况:%s\n'
                   u'明天温度:%s℃(记得涂防晒霜哦)\n'
                   u'明天风向:%s\n'
                   u'明天风的级数:%s\n\n' % (
                       today.strftime('%Y-%m-%d'), loving_days, Tod_Weather_Date[0], Tod_Weather_Wea[0],
                       Tod_Weather_Tem[0],
                       Tod_Weather_Wind_Con[0], Tod_Weather_Wind_Num[0], Tom_Weather_Date[0], Tom_Weather_Wea[0],
                       Tom_Weather_Tem[0], Tom_Weather_Wind_Con[0], Tom_Weather_Wind_Num[0])]
        elif(-15 <= int(Tom_Weather_Tem[0]) < 10):
            lst = [u'你好，呆瓜:\n\n\t'
                   u'今天是%s\n\t '
                   u'首先，今天已经是我们相恋的第%s天了喔。然后大兵就要来播送天气预报了！！\n\n\t'
                   u'今天日期:%s\n'
                   u'今天天气情况:%s\n'
                   u'今天温度:%s℃\n'
                   u'今天风向:%s\n'
                   u'今天风的级数:%s\n\n'
                   u'明天日期:%s\n'
                   u'明天天气情况:%s\n'
                   u'明天温度:%s℃(记得穿厚一些哦)\n'
                   u'明天风向:%s\n'
                   u'明天风的级数:%s\n\n' % (
                       today.strftime('%Y-%m-%d'), loving_days, Tod_Weather_Date[0], Tod_Weather_Wea[0],
                       Tod_Weather_Tem[0],
                       Tod_Weather_Wind_Con[0], Tod_Weather_Wind_Num[0], Tom_Weather_Date[0], Tom_Weather_Wea[0],
                       Tom_Weather_Tem[0], Tom_Weather_Wind_Con[0], Tom_Weather_Wind_Num[0])]
        elif((28 <= int(Tod_Weather_Tem[0]) < 50) and (28 <= int(Tom_Weather_Tem[0]) < 50)):
            lst = [u'你好，呆瓜:\n\n\t'
                   u'今天是%s\n\t '
                   u'首先，今天已经是我们相恋的第%s天了喔。然后大兵就要来播送天气预报了！！\n\n\t'
                   u'今天日期:%s\n'
                   u'今天天气情况:%s\n'
                   u'今天温度:%s℃(记得涂防晒霜)\n'
                   u'今天风向:%s\n'
                   u'今天风的级数:%s\n\n'
                   u'明天日期:%s\n'
                   u'明天天气情况:%s\n'
                   u'明天温度:%s℃(记得涂防晒霜)\n'
                   u'明天风向:%s\n'
                   u'明天风的级数:%s\n\n' % (
                       today.strftime('%Y-%m-%d'), loving_days, Tod_Weather_Date[0], Tod_Weather_Wea[0],
                       Tod_Weather_Tem[0],
                       Tod_Weather_Wind_Con[0], Tod_Weather_Wind_Num[0], Tom_Weather_Date[0], Tom_Weather_Wea[0],
                       Tom_Weather_Tem[0], Tom_Weather_Wind_Con[0], Tom_Weather_Wind_Num[0])]
        elif((-15 <= int(Tod_Weather_Tem[0]) < 10) and (-15 <= int(Tom_Weather_Tem[0]) < 10)):
            lst = [u'你好，呆瓜:\n\n\t'
                   u'今天是%s\n\t '
                   u'首先，今天已经是我们相恋的第%s天了喔。然后大兵就要来播送天气预报了！！\n\n\t'
                   u'今天日期:%s\n'
                   u'今天天气情况:%s\n'
                   u'今天温度:%s℃(记得穿厚一点哦)\n'
                   u'今天风向:%s\n'
                   u'今天风的级数:%s\n\n'
                   u'明天日期:%s\n'
                   u'明天天气情况:%s\n'
                   u'明天温度:%s℃(记得穿厚一点哦)\n'
                   u'明天风向:%s\n'
                   u'明天风的级数:%s\n\n' % (
                       today.strftime('%Y-%m-%d'), loving_days, Tod_Weather_Date[0], Tod_Weather_Wea[0],
                       Tod_Weather_Tem[0],
                       Tod_Weather_Wind_Con[0], Tod_Weather_Wind_Num[0], Tom_Weather_Date[0], Tom_Weather_Wea[0],
                       Tom_Weather_Tem[0], Tom_Weather_Wind_Con[0], Tom_Weather_Wind_Num[0])]
        else:
            lst = [u'你好，呆瓜:\n\n\t'
                   u'今天是%s\n\t '
                   u'首先，今天已经是我们相恋的第%s天了喔。然后大兵就要来播送天气预报了！！\n\n\t'
                   u'今天日期:%s\n'
                   u'今天天气情况:%s\n'
                   u'今天温度:%s℃\n'
                   u'今天风向:%s\n'
                   u'今天风的级数:%s\n\n'
                   u'明天日期:%s\n'
                   u'明天天气情况:%s\n'
                   u'明天温度:%s℃\n'
                   u'明天风向:%s\n'
                   u'明天风的级数:%s\n\n' % (today.strftime('%Y-%m-%d'), loving_days, Tod_Weather_Date[0], Tod_Weather_Wea[0], Tod_Weather_Tem[0], Tod_Weather_Wind_Con[0], Tod_Weather_Wind_Num[0], Tom_Weather_Date[0], Tom_Weather_Wea[0], Tom_Weather_Tem[0], Tom_Weather_Wind_Con[0], Tom_Weather_Wind_Num[0])]

        # It is receiver email word.
        mailto_list = "*********@qq.com"
        mail_host = "smtp.qq.com"
        # It is your email word.
        mail_user = "********@qq.com"
        # It is your password
        mail_pass = "**********"


        content = ''.join(lst)
        msg = MIMEText(content, _subtype='plain', _charset='utf-8')
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

