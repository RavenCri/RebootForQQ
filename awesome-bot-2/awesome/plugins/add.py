from nonebot import on_command, CommandSession
import requests
import pyperclip,nonebot
from awesome.plugins.token import myQQs
from awesome.plugins.select import getCurrQQList
from awesome.plugins.util.dao import getQQList,addQQUsedNum
import sqlite3
from nonebot.log import logger
__plugin_name__ = 'add'
__plugin_usage__ = r"""
添加获取密令权限，发送 add qq号码 即可
""".strip()
async def addQQ(qqNum,qqId) -> str:
   
   
    if qqNum in myQQs:
        try:
           
            qqInfo =  qqId.split(",")
          
            for i in qqInfo:
                if i == "":
                    continue
                try:
                    int(i.split("*")[0])#判断是不是数字
                    if len(i.split("*"))>1:#判断增加次数是不是数字
                        int(i.split("*")[1])
                except ValueError as identifier:
                    continue

                logger.info(i)
                num =    int(i.split("*")[1]) if len(i.split("*")) >1  else 1
                addQQUsedNum(i.split("*")[0],num)
        
            msg = getCurrQQList(getQQList())
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
    msg_report = await addQQ(qqNum,qqId)
    await session.send(msg_report)
    
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


