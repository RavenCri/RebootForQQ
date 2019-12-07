from nonebot import on_command, CommandSession
from awesome.plugins.token import myQQs
import sqlite3
__plugin_name__ = 'select'
__plugin_usage__ = r"""
查看当前有权限的用户列表 发送 select 即可
""".strip()
@on_command('select', aliases=('select'))
async def select(session: CommandSession):
    
    qqNum = session.ctx["user_id"]
    if qqNum in myQQs:
       #msg = "当前可用列表："+(",".join('%s' %id for id in qqList))
      qqList = getQQTokenNum()
      msg = getCurrQQList(qqList)
      if msg == "":
         msg = "null"
      msg = "当前可用列表：\n"+ msg
    else:
       msg = "您没有权限查看当前可用列表"
    await session.send(msg)

# 获取当前可获取token的QQ列表
def getCurrQQList(qqList):
   msg =""
   myset = set(qqList) 
   for item in myset:
    
      
      msg += ("%s-->%d (次)\n" %(item,qqList.get(item)))
     
   #msg = msg[0:-1]
   return msg

# 获取所有QQ的可用次数
def getQQTokenNum():
   qqList = {}
   conn = sqlite3.connect('C:/Users/raven/Desktop/reboot/test.db')
   #创建一个cursor：
   cursor = conn.cursor()
  
   c =  cursor.execute('select QQNum, num from token')
   
   for row in c:
      qqList[row[0]] =int(row[1])
   cursor.close()
   #提交事务：
   conn.commit()
   #关闭connection：
   conn.close()
   return qqList