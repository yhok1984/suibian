#!/usr/bin/python
#coding:utf-8
from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import time
import  schedule
#windows运行
#bot = Bot(cache_path=True)
# linux执行登陆
bot = Bot(console_qr=2,cache_path="botoo.pkl")
def get_news():
    url = "http://t.weather.sojson.com/api/weather/city/101281502"
    r = requests.get(url)
    content = '当前城市：' + r.json()['cityInfo']['city'] + '\n今日温度：' + r.json()['data']['wendu'] + '\n' + r.json()['data']['yesterday']['high'] + '\n' + r.json()['data']['yesterday']['low'] + '\n空气湿度：' + r.json()['data']['shidu'] + \
              '\n空气质量：' + r.json()['data']['quality'] + '\n感冒指数：' + r.json()['data']['ganmao'] + '\n天气提醒：' + r.json()['data']['yesterday']['notice'] + '\n发送时间：' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return content
def send_news():
    try:
        content = get_news()
        my_friend = bot.friends().search(u'老婆')[0]
        my_friend.send(content)
        my_friend.send(u"老公每日温馨提醒")
        schedule.every().day.at("07:15").do(send_news)
        while True:
            time.sleep(58)
            schedule.run_pending()

        #t = Timer(5, send_news)
        #t.start()


    except:
        my_friend = bot.friends().search('忙碌的余先森')[0]
        my_friend.send(u"今天的天气预报推送失败")
if __name__ == "__main__":
    send_news()