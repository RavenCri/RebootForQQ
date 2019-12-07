from nonebot import on_command, CommandSession,on_natural_language,NLPResult,NLPSession
import requests
import pyperclip,nonebot
import sqlite3
from nonebot.log import logger
myQQs = [2109241,857697474]
__plugin_name__ = 'gettoken'
__plugin_usage__ = r"""
用来获取密令,发送 1\token\获取token\密令 四者中的任意一个即可获取体育在线考试的密令
""".strip()
@on_natural_language({'密令'}, only_to_me=False)
async def _(session: NLPSession):
    return NLPResult(100.0, ('token',), None)
@on_natural_language({'体育'}, only_to_me=False)
async def _(session: NLPSession):
    return NLPResult(100.0, ('token',), None)
# on_command 装饰器将函数声明为一个命令处理器

@on_command('token', aliases=('1', 'token', '获取token','密令'))
async def token(session: CommandSession):
   
    qqNum = session.ctx["user_id"]
    weather_report = await getToken(qqNum)
    await session.send(weather_report)

# 获取token  
async def getToken(qqNum) -> str:
    
    useNum = getTokenNum(qqNum)
 
    if (useNum is not None and useNum > 0 ) or qqNum in myQQs:
        session = requests.session()
        auth = "9h6BGD624a273gm2FOJeeDeY5jKB7b5NR6b1LR75adQleqg8gfE8vyBq3abXY1eV090u5n6fR5RefEFyZ3jZH820NtuDc4HZ9Isz63IeDv6dPA0FeHU3P0TJ15O9mzf4d00ffMeaX8qvS2i8U3CX7Df9r5x00Fn2UJT3Q1btEa4X0kiy1c0L2P0ao4LB0J1RB17cJf6O17e84rc8M9pbcvuu01d2N1R6aW1FBMVS20c6A6cs5C586Tlc2dJFGxsB"
        resp = session.get("http://raven520.top/getToken?auth="+auth)
        res =  "点击该链接，输入您的学号和身份证后六位登录即可。(请用浏览器打开该链接。"+resp.text+" )\n温馨提示：直接点击该私密链接不需要您输入密令（需浏览器里打开！），系统会帮你填好密令。初始可使用次数为5次，如果您对自己的分数不满意,您可以继续使用该链接，直至次数耗尽，最终成绩系统会取最高分哦。"
        pyperclip.copy(res)
        # 如果获取的QQ不是我的QQ
        if qqNum not in myQQs:
            #那么设置他的可用次数 -1
           qqTokeNumChange(qqNum,useNum-1)
           bot = nonebot.get_bot()
           await bot.send_private_msg(user_id=2109241, message=("<%s>刚刚获取了一次体育在线测试的Token,他还可以获取：%d 次" %(qqNum,useNum-1)))
        return res
    else:

        return "您还没有权限获取密令呢~,如果您需要体育在线答题密令,请联系管理员<衣服架子>,成功转账之后再与我联系,向我 发送 密令 即可。"

# 获取QQ的token可用次数
def getTokenNum(qqNum):
   
    conn = sqlite3.connect('C:/Users/raven/Desktop/reboot/test.db')
    #创建一个cursor：
    cursor = conn.cursor()
    #插入一条记录：
    c =  cursor.execute('select  num from token where QQNum = \''+str(qqNum)+'\'')
  
    for row in c:
        return row[0]
 
# 更新QQ 的token可用次数
def qqTokeNumChange(qqNum,useNum):
    conn = sqlite3.connect('C:/Users/raven/Desktop/reboot/test.db')
    
    cursor = conn.cursor()
    
    c =  cursor.execute('update token set num='+str(useNum)+'   where QQNum = \''+str(qqNum)+'\'')
    if useNum == 0:
        c =  cursor.execute('delete from token   where QQNum = \''+str(qqNum)+'\'')
    cursor.close()
     #提交事务：
    conn.commit()
    #关闭connection：
    conn.close()