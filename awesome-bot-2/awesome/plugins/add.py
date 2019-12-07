from nonebot import on_command, CommandSession
import requests
import pyperclip,nonebot
from awesome.plugins.token import myQQs,qqTokeNumChange
from awesome.plugins.select import getCurrQQList,getQQTokenNum
import sqlite3
from nonebot.log import logger
__plugin_name__ = 'add'
__plugin_usage__ = r"""
添加获取密令权限，发送 add qq号码 即可
""".strip()
async def addQQ(qqNum,qqId) -> str:
   
   
    if qqNum in myQQs:
        try:
            qqId = qqId.replace(" ", "")
            if qqId.find("*")  > 0 and qqId.find(",") < 0:
                qqInfo =  qqId.split("*")
                addQQgetTokenNum(qqInfo[0],int(qqInfo[1]))
            elif qqId.find(",")  > 0:
                qqInfo =  qqId.split(",")
                for i in qqInfo:
                    logger.info(i)
                    num =    int(i.split("*")[1]) if len(i.split("*")) >1  else 1
                    addQQgetTokenNum(i.split("*")[0],num)
            else:
               
                 addQQgetTokenNum(qqId,1)
            msg = getCurrQQList(getQQTokenNum())
            #return "添加成功！当前可用列表："+(",".join('%s' %id for id in qqList))
            return "添加成功！当前可用列表：\n"+msg
        except (ValueError):
            
            return "QQ只能是数字哦~"
       
    else:
        return "您没有权限添加!"

# on_command 装饰器将函数声明为一个命令处理器

@on_command('add', aliases=('add'))
async def add(session: CommandSession):
    qqId = session.get('qq', prompt='您想给哪个QQ添加获取密令的权限呢？')
    qqNum = session.ctx["user_id"]
    weather_report = await addQQ(qqNum,qqId)
    await session.send(weather_report)
    
@add.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
         
            session.state['qq'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('QQ号不能为空哦')

    session.state[session.current_key] = stripped_arg

# 添加QQ
def addQQgetTokenNum(QQNum,num):
    conn = sqlite3.connect('C:/Users/raven/Desktop/reboot/test.db')
    #创建一个cursor：
    cursor = conn.cursor()
    #如果QQ 已经存在数据表中
    if QQNum in getQQTokenNum():
        # 次数 改变 为原有次数 + 要增加的次数
        qqTokeNumChange(QQNum,getQQTokenNum().get(QQNum)+num)
        return
    cursor.execute('insert into token (QQNum, num) values (\''+QQNum+'\','+str(num)+')')
    cursor.close()
     #提交事务：
    conn.commit()
    #关闭connection：
    conn.close()
