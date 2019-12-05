from nonebot import on_command, CommandSession
from awesome.plugins.token import myQQs,qqList
@on_command('select', aliases=('select'))
async def select(session: CommandSession):
    
    qqNum = session.ctx["user_id"]
    if qqNum in myQQs:
       msg = "当前可用列表："+(",".join('%s' %id for id in qqList))
    else:
       msg = "您没有权限查看当前可用列表"
    await session.send(msg)