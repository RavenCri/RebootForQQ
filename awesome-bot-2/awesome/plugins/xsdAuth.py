from nonebot import on_command, CommandSession
import requests


async def getplungeAuth(xsdId,qqNum) -> str:
      
      url = "http://raven520.top/openPower?key=vrHvaWTZ7JBxMYci&xsd="+xsdId
      if qqNum == 2109241 or qqNum == 857697474:
          return requests.session().get(url).text
      else:
          return "你没有权限执行相关操作！"
# on_command 装饰器将函数声明为一个命令处理器


@on_command('plunge', aliases=('开通插件权限', '开权限'))
async def plunge(session: CommandSession):
   
    xsdId = session.get('xsd', prompt='您想给哪个插件开通权限呢？')
    qqNum = session.ctx["user_id"]
    weather_report = await getplungeAuth(xsdId,qqNum)
    
    await session.send(weather_report)
   

@plunge.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['xsd'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('插件id不能为空哦，请重新输入！')

    session.state[session.current_key] = stripped_arg


