from os import path

import nonebot
import os
import config
import pathlib
 #导入SQLite驱动：
import sqlite3
# 启动这个脚本就ok  python -u "c:\Users\raven\Desktop\reboot\awesome-bot-2\bot.py"
if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'plugins'),
        'awesome.plugins'
    )
   
 
    #数据库文件是test.db，不存在，则自动创建
    conn = sqlite3.connect('C:/Users/raven/Desktop/reboot/test.db')
    #创建一个cursor：
    cursor = conn.cursor()
  
    cursor.execute(' CREATE TABLE IF NOT EXISTS  token(QQNum varchar(20) primary key,num Integer)')

    cursor.close()
    #提交事务：
    conn.commit()
    #关闭connection：
    conn.close()  

    nonebot.run()
