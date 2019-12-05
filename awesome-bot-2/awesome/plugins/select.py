from nonebot import on_command, CommandSession
from awesome.plugins.token import myQQs,qqList

__plugin_name__ = '查看当前有权限的用户列表'
__plugin_usage__ = r"""
发送 select 即可
""".strip()
@on_command('select', aliases=('select'))
async def select(session: CommandSession):
    
    qqNum = session.ctx["user_id"]
    if qqNum in myQQs:
       msg = "当前可用列表："+(",".join('%s' %id for id in qqList))
    else:
       msg = "您没有权限查看当前可用列表"
    await session.send(msg)