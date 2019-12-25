from nonebot import on_command, CommandSession
import requests
import pyperclip,nonebot
from awesome.plugins.util.dao import selectNumByQQId,updateNum
from awesome.plugins.token import myQQs
from awesome.plugins.util.httpUtil import httpGet,httpPost
__plugin_name__ = '体考'
__plugin_usage__ = r"""
可以进行体育考试，只需要向我发送 'test 学号 密码' 即可
""".strip()
@on_command('autoTest', aliases=('体考','test'))
async def autoTest(session: CommandSession):
    msg = session.get('msgInfo', prompt='请输入学号和密码（ps:学号和密码用空格分隔开，密码为身份证后6位）')
    qqNum = session.ctx["user_id"]
    useNum = selectNumByQQId(qqNum)
    msgsplit = msg.split(' ')
  
    #if (useNum is not None and useNum > 0 ) or qqNum in myQQs:
    if len(msgsplit) != 2:
        sendMsg = "账号密码格式不正确！"
    else:
        auth = "9h6BGD624a273gm2FOJeeDeY5jKB7b5NR6b1LR75adQleqg8gfE8vyBq3abXY1eV090u5n6fR5RefEFyZ3jZH820NtuDc4HZ9Isz63IeDv6dPA0FeHU3P0TJ15O9mzf4d00ffMeaX8qvS2i8U3CX7Df9r5x00Fn2UJT3Q1btEa4X0kiy1c0L2P0ao4LB0J1RB17cJf6O17e84rc8M9pbcvuu01d2N1R6aW1FBMVS20c6A6cs5C586Tlc2dJFGxsB"
        resp = httpGet("http://raven520.top/getToken?auth="+auth)
        data = {"username":msgsplit[0],"password":msgsplit[1],"token":resp.text}
        sendMsg = httpPost("http://raven520.top/sportfull",data).json()['msg']
    #else:
        #sendMsg = "您还未获得相关权限！"
    await session.send(sendMsg)
    
@autoTest.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
         
            session.state['msgInfo'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要输入学号密码，我才能帮你考哦~')

    session.state[session.current_key] = stripped_arg