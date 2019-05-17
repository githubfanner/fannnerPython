# 导入模块
import requests
from wxpy import *
import md5sign


# 初始化机器人，扫码登陆
bot = Bot()
frend_name='asu'
friend_1 = bot.friends().search(frend_name)[0]
@bot.register(friend_1)
def print_group_msg(msg):
    print('收到'+frend_name+' 消息：' + msg.text)
    answer=get_content(msg.text)
    friend_1.send(answer)
    print('发送给' + frend_name + ' 消息：' + answer)



def get_content(plus_item):
    # 聊天的API地址    
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
    # 获取请求参数  
    plus_item = plus_item.encode('utf-8')
    payload = md5sign.get_params(plus_item)
    #r = requests.get(url,params=payload)
    r = requests.post(url, data=payload)
    print('ret:'+str(r.json()["ret"]))
    return r.json()["data"]["answer"]


if __name__ == '__main__':
     while True:
          comment = input('我：')
          if comment == 'q':
              break
          friend_1.send(comment)





