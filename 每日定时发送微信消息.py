#!/usr/bin/python
#coding:utf-8
from __future__ import unicode_literals
from wxpy import *
import requests
import datetime
import time

#windows运行
#bot = Bot(cache_path=True)
# linux执行登陆
bot = Bot(console_qr=2,cache_path="botoo.pkl")
def get_news():
    url = "http://t.weather.sojson.com/api/weather/city/101281502"
    r = requests.get(url)
    content = '当前城市：' + r.json()['cityInfo']['city'] + '\n今日温度：' + r.json()['data']['wendu'] + \
              '\n' + r.json()['data']['yesterday']['high'] + '\n' + r.json()['data']['yesterday']['low'] + \
              '\n空气湿度：' + r.json()['data']['shidu'] + '\n空气质量：' + r.json()['data']['quality'] + \
              '\n感冒指数：' + r.json()['data']['ganmao'] + '\n天气提醒：' + r.json()['data']['yesterday']['notice']
    return content
#第二组消息
def get_news2():
    url2 = "http://v.juhe.cn/calendar/day"
    url3 = 'http://web.juhe.cn:8080/constellation/getAll'
    time = datetime.datetime.now().timetuple()
    VersionInfo = str(time.tm_year) + '-' + str(time.tm_mon) + '-' + str(time.tm_mday)
    y = str(VersionInfo)
    payload = {'date': y, 'key': '5c5905a23b61507d73c56182fd2046dd'}
    payload2 = {'consName': '狮子座', 'type' : 'today','key' : 'a0fe1635df9b5d1ae0f32f66b7285c55'}
    b = requests.get(url2,params=payload)
    c = requests.get(url3, params=payload2)
    content2 = b.json()['result']['data']['lunarYear'] + '(' + b.json()['result']['data']['animalsYear'] + ')' + b.json()['result']['data']['lunar'] + b.json()['result']['data']['weekday'] + \
               '\n' + c.json()['name'] + c.json()['summary'] + '\n今日财运指数：' + c.json()['money']
    return content2
def send_news():
    try:
        while True:
            a = int(datetime.datetime.now().strftime('%H%M'))
            b = int('0720')
            if a - b == 0 :
                content = get_news()
                content2 = get_news2()
                my_friend = bot.friends().search(u'老婆')[0]
                my_friend.send(content)
                my_friend.send(content2)
                time.sleep(60)

    except:
        my_friend = bot.friends().search('忙碌的余先森')[0]
        my_friend.send(u"今天的天气预报推送失败")
if __name__ == "__main__":
    send_news()