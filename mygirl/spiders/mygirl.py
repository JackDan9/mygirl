# -*- coding: utf-8 -*-

"""
File: mygirl.py
Author: jackdan9
Date: 2018/8/31 10:07
"""

import scrapy
import smtplib
import datetime
from email.mime.text import MIMEText
from email.header import Header
import traceback

import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class MyGirlSpider(scrapy.Spider):
    name = "mygirl"
    start_urls = [
        "http://forecast.weather.com.cn/town/weather1dn/101260409003.shtml", # 贵州省-平塘县-大塘镇
    ]


    def parse(self, response):
        Tod_Weather_Wea = response.xpath('//*[@class="weather dis"]/text()').extract()
        Tod_Weather_Tem = response.xpath('//*[@class="tempDiv"]/span[1]/text()').extract()
        Tod_Weather_Tem_Max = response.xpath('//*[@id="maxTempDiv"]/span/text()').extract()
        Tod_Weather_Tem_Min = response.xpath('//*[@id="minTempDiv"]/span/text()').extract()
        Tod_Weather_Con_Num = response.xpath('//*[@class="todayLeft"]/p[1]/span/text()').extract()
        Tod_Weather_Hum = response.xpath('//*[@class="todayLeft"]/p[2]/span/text()').extract()

        Tod_Weather_Ult_Ray = response.xpath('//*[@class="weather_shzs weather_shzs_1d"]/div[@class="lv"]/dl[1]/dt/em/text()').extract()
        Tod_Weather_Ult_Ray_Sug = response.xpath('//*[@class="weather_shzs weather_shzs_1d"]/div[@class="lv"]/dl[1]/dd/text()').extract()
        Tod_Weather_Cold = response.xpath('//*[@class="weather_shzs weather_shzs_1d"]/div[@class="lv"]/dl[2]/dt/em/text()').extract()
        Tod_Weather_Cold_Sug = response.xpath('//*[@class="weather_shzs weather_shzs_1d"]/div[@class="lv"]/dl[2]/dd/text()').extract()
        Tod_Weather_Dress = response.xpath('//*[@class="weather_shzs weather_shzs_1d"]/div[@class="lv"]/dl[3]/dt/em/text()').extract()
        Tod_Weather_Dress_Sug = response.xpath('//*[@class="weather_shzs weather_shzs_1d"]/div[@class="lv"]/dl[3]/dd/text()').extract()
        Tod_Weather_Exercise = response.xpath('//*[@class="weather_shzs weather_shzs_1d"]/div[@class="lv"]/dl[5]/dt/em/text()').extract()
        Tod_Weather_Exercise_Sug = response.xpath('//*[@class="weather_shzs weather_shzs_1d"]/div[@class="lv"]/dl[5]/dd/text()').extract()
        Tod_Weather_Pollute = response.xpath('//*[@class="weather_shzs weather_shzs_1d"]/div[@class="lv"]/dl[6]/dt/em/text()').extract()
        Tod_Weather_Pollute_Sug = response.xpath('//*[@class="weather_shzs weather_shzs_1d"]/div[@class="lv"]/dl[6]/dd/text()').extract()
        # Hum(Humidity)

        today = datetime.datetime.today()
        anniversary = datetime.datetime(2018, 3, 14)
        loving_days = (today - anniversary).days

        location = '平塘县-大塘镇(西关中学和西关小学)'
        loving_word = '爱你呦！！！'

        lst = [u'你好，呆瓜:\n\n\t'
               u'今天是%s, 地点是%s\n\t'
               u'首先，今天已经是我们相恋的第%s天了喔。然后大兵就要来播送天气预报了！！\n\n\t'
               u'今天日期:%s\n'
               u'今天天气情况:%s\n'
               u'今天温度:%s℃\n'
               u'今天最高气温:%s\n'
               u'今天最低气温:%s\n'
               u'今天风向和风的级数:%s\n'
               u'今天相对湿度:%s\n\n'
               
               u'大兵的生活小贴士:\n'
               u'紫外线:%s\n'
               u'小贴士:%s\n'
               u'感冒:%s\n'
               u'小贴士:%s\n'
               u'穿衣:%s\n'
               u'小贴士:%s\n'
               u'运动:%s\n'
               u'小贴士:%s\n'
               u'空气污染扩散:%s\n'
               u'小贴士:%s\n\n'
        
               u'%s'
               % (
                    today.strftime('%Y-%m-%d'),
                    location,
                    loving_days, 
                    today.strftime('%Y-%m-%d'), 
                    Tod_Weather_Wea[0], 
                    Tod_Weather_Tem[0], 
                    Tod_Weather_Tem_Max[0], 
                    Tod_Weather_Tem_Min[0], 
                    Tod_Weather_Con_Num[0], 
                    Tod_Weather_Hum[0], 
                    Tod_Weather_Ult_Ray[0], 
                    Tod_Weather_Ult_Ray_Sug[0], 
                    Tod_Weather_Cold[0], 
                    Tod_Weather_Cold_Sug[0], 
                    Tod_Weather_Dress[0], 
                    Tod_Weather_Dress_Sug[0], 
                    Tod_Weather_Exercise[0], 
                    Tod_Weather_Exercise_Sug[0], 
                    Tod_Weather_Pollute[0], 
                    Tod_Weather_Pollute_Sug[0],
                    loving_word
                )
            ]
        # It is receiver email word.
        mailto_list = "**********@qq.com"
        mail_host = "smtp.qq.com"
        # It is your email word.
        mail_user = "**********@qq.com"
        # It is your password
        mail_pass = "****************"


        content = ''.join(lst)
        print(content)
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