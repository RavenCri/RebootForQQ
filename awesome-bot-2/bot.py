from os import path

import nonebot

import config
# 启动这个脚本就ok  python -u "c:\Users\raven\Desktop\reboot\awesome-bot-2\bot.py"
if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'plugins'),
        'awesome.plugins'
    )
    nonebot.run()
