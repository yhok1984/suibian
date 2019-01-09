import requests
import json
import time
s = 0.5
s10 = 1
while 1 > s:
    r = requests.get('http://api.zb.cn/data/v1/ticker?market=eth_qc')
    json_response = r.content.decode()
    dict = json.loads(json_response)
    p = float(dict['ticker']['last'])
    print('--------------------------------')
    list2 = [round(float(p - s10), 3)]
    if (float(list2[0])- 1000) / p > 0.01:
        print('  涨超过1%！！ ')
    else:
        print('  风平浪静： ')
    print('  一分钟内涨跌：', list2, '    (', int(float(p) / 6.958), '美元 )')
    print('  最新：',p)
    print('  上次：',s10,'    (',int(s10/6.958),'美元 )')
    print('  最高：', dict['ticker']['high'],'    (',int(float(dict['ticker']['high'])/6.958),'美元 )')
    print('  最低：', dict['ticker']['low'],'    (',int(float(dict['ticker']['low'])/6.958),'美元 )')
    print('  时间：',time.strftime('%H:%M:%S',time.localtime(time.time())))
    s10 = float(p)
    time.sleep(15)
