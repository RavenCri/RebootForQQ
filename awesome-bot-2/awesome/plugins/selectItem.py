import requests
from nonebot import on_command, CommandSession
from nonebot.log import logger
import re
@on_command('selectItem', aliases=('查题','查',))
async def selectItem(session: CommandSession):
   
    getItem  = session.get('msgInfo', prompt='请问你要查询的题目是？')
    data ={'topic[0]':getItem}
    resp =  requests.session().post('https://cx.icodef.com/v2/answer', data=data, verify=False, timeout=5)
    logger.info(resp.json()) 
    result = []
    for each in resp.json():
        for answ in each['result']:
            temp = {}
            temp['题目'] = answ['topic']
            temp['答案'] = ''
            for option in answ['correct']:
                temp['答案'] = temp['答案'] + str(option['content'])
            isAdd = True
            for i in result:
                if  removeSign(i).find(removeSign(temp['题目'])) > 0:
                    isAdd = False
            if isAdd:
                result.append(str("题目："+temp['题目']+"\n答案："+temp['答案']+"\n"))
 
    if len(result) > 0:
        resultMsg = "查询结果如下：\n"+"\n".join(result)
    else:
        resultMsg = "没有该题目的答案"
    await session.send(resultMsg)
def removeSign(str):
    return re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，．。？、：.:()“”~@#￥%……&*（）]+", "", str)
@selectItem.args_parser
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