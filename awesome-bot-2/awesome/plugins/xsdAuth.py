from nonebot import on_command, CommandSession
import requests
from awesome.plugins.token import myQQs
from awesome.plugins.util.httpUtil import httpGet
__plugin_name__ = 'xsdplus'
__plugin_usage__ = r"""
开通xsd码的插件功能,发送 '开权限  xsd码' 或者 'xsdplus xsd码' 即可
""".strip()
async def getplungeAuth(session,xsdId,qqNum) -> str:
      
     
      if qqNum  in myQQs:
          return httpGet(session.bot.config.localhost+"/openPower?key=vrHvaWTZ7JBxMYci&xsd="+xsdId).text
      else:
          return "你没有权限执行相关操作！"
# on_command 装饰器将函数声明为一个命令处理器



@on_command('plunge', aliases=('xsdplus', '开权限'))
async def plunge(session: CommandSession):
   
    xsdId = session.get('xsd', prompt='您想给哪个插件开通权限呢？')
    qqNum = session.ctx["user_id"]
    msg_report = await getplungeAuth(session,xsdId,qqNum)
    
    await session.send(msg_report)
   

@plunge.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将xsd吗跟在命令名后面，作为参数传入
            # 例如用户可能发送了：xsdplus  xxx
            session.state['xsd'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('插件id不能为空哦，请重新输入！')

    session.state[session.current_key] = stripped_arg


