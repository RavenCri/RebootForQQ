from nonebot import on_command, CommandSession
import requests
import pyperclip,nonebot

myQQs = [2109241,857697474]
qqList = [2109241,857697474]
__plugin_name__ = '获取密令'
__plugin_usage__ = r"""
发送 1\token\获取token\密令 四者中的任意一个即可获取体育在线考试的密令
""".strip()
# on_command 装饰器将函数声明为一个命令处理器

@on_command('token', aliases=('1', 'token', '获取token','密令'))
async def token(session: CommandSession):
   
    qqNum = session.ctx["user_id"]
    weather_report = await getToken(qqNum)
    await session.send(weather_report)

   
async def getToken(qqNum) -> str:
   
    if qqNum in qqList:
        session = requests.session()
        auth = "9h6BGD624a273gm2FOJeeDeY5jKB7b5NR6b1LR75adQleqg8gfE8vyBq3abXY1eV090u5n6fR5RefEFyZ3jZH820NtuDc4HZ9Isz63IeDv6dPA0FeHU3P0TJ15O9mzf4d00ffMeaX8qvS2i8U3CX7Df9r5x00Fn2UJT3Q1btEa4X0kiy1c0L2P0ao4LB0J1RB17cJf6O17e84rc8M9pbcvuu01d2N1R6aW1FBMVS20c6A6cs5C586Tlc2dJFGxsB"
        resp = session.get("http://raven520.top/getToken?auth="+auth)
        res =  "点击该链接，输入您的学号和身份证后六位即可。(请用浏览器打开该链接。)"+resp.text
        pyperclip.copy(res)
        if qqNum not in myQQs:
            qqList.remove(qqNum)
        return res
    else:

        return "您还没有权限获取密令呢~,如果您需要体育在线答题密令,请联系 管理员 衣服架子，转账之后在与我联系。"

