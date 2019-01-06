
import itchat
import pandas as pd
itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)[0:]
male = female = other = 0
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other +=1
total = len(friends[1:])
#打印性别比例
print("Login successfully as 忙碌的余先森：\n"
      "男性好友：%.2f%%" % (float(male)/total*100) + "\n" +
      "女性好友：%.2f%%" % (float(female) / total * 100) + "\n" +
      "不明性别好友：%.2f%%" %(float(other) / total * 100))
print('好友总人数：',total)
import itchat
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
from collections import Counter
itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)
sexs = list(map(lambda x: x['Sex'], friends[1:]))
counts = list(map(lambda x: x[1], Counter(sexs).items()))
labels = ['女性','男性',  '不明性别']
colors = ['red', 'yellowgreen', 'lightskyblue']
plt.figure(figsize=(8, 5), dpi=80)
plt.axes(aspect=1)
plt.pie(counts, labels=labels, colors=colors, labeldistance=1.1, autopct='%3.1f%%', shadow=False, startangle=90, pctdistance=0.6 )
plt.legend(loc='upper right',)
plt.title('%s的微信好友性别组成' % friends[0]['NickName'])
plt.show()
df_friends = pd.DataFrame(friends)
City = df_friends.City
City_count = City.value_counts()
City_count = City_count[City_count.index != '']
print(City_count)
def getFriendsInfo():
    itchat.auto_login(hotReload=True)
    friends=itchat.get_friends(update=True)[1:]
    province=[]
    signature=[]
    for friend in friends:
        print('****************')
        print('昵称：',friend['NickName'])
        print('所在省份：',friend['Province'])
        print('个人签名：',friend['Signature'])
        province.append(friend['Province'])
        signature.append(friend['Signature'])
    return(province,signature)
if __name__=='__main__':
    province,signature=getFriendsInfo()