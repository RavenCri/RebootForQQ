from nonebot import on_command, CommandSession
from awesome.plugins.token import myQQs
from awesome.plugins.util.dao import getQQList
import sqlite3
__plugin_name__ = 'select'
__plugin_usage__ = r"""
查看当前有权限的用户列表 发送 select 即可
""".strip()

   # 如果list都是数字 必须这样做必须这么转换
   #msg = "当前可用列表："+(",".join('%s' %id for id in qqList))

@on_command('select', aliases=('select'))
async def select(session: CommandSession):
    # 获取当前发送消息的QQ
    qqNum = session.ctx["user_id"]
    # 获取可用列表
    qqList = getQQList()
    # 转换为要发送的消息
    msg = getCurrQQList(qqList)
    if msg == "":
      msg = "null"
    msg = "当前可用列表：\n"+ msg

    await session.send(msg)

# 获取当前可获取token的QQ列表
def getCurrQQList(qqList):
   msg =""
   myset = set(qqList) 
   for item in myset:
      msg += ("%s-->%d (次)\n" %(item,qqList.get(item)))
     
   return msg

