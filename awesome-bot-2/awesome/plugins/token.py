from nonebot import on_command, CommandSession,on_natural_language,NLPResult,NLPSession
import pyperclip,nonebot
from awesome.plugins.util.dao import selectNumByQQId,updateNum
from awesome.plugins.util.httpUtil import httpGet
from nonebot.log import logger
myQQs = [2109241,857697474]
__plugin_name__ = 'gettoken'
__plugin_usage__ = r"""
用来获取密令,发送 1\token\获取token\密令 四者中的任意一个即可获取体育在线考试的密令
""".strip()
#@on_natural_language({'密令'}, only_to_me=False)
async def _(session: NLPSession):
    return NLPResult(100.0, ('token',), None)
#@on_natural_language({'体育'}, only_to_me=False)
async def _(session: NLPSession):
    return NLPResult(100.0, ('token',), None)

# on_command 装饰器将函数声明为一个命令处理器
@on_command('token', aliases=('1', 'token', '获取token','密令','0'))
async def token(session: CommandSession):
   
    qqNum = session.ctx["user_id"]
    msg = session.ctx['message'].extract_plain_text()
    senStr,useNum = await getToken(qqNum,msg)
    await session.send(senStr)
    if useNum is not None:
        bot = nonebot.get_bot()
        await bot.send_private_msg(user_id=2109241, message=("<%s>刚刚获取了一次体育在线测试的Token,他还可以获取：%d 次" %(qqNum,useNum)))
# 获取token  
async def getToken(qqNum,st) -> (str,int):
    
    useNum = selectNumByQQId(qqNum)
   
    if (useNum is not None and useNum > 0 ) or qqNum in myQQs:
       
        auth = "9h6BGD624a273gm2FOJeeDeY5jKB7b5NR6b1LR75adQleqg8gfE8vyBq3abXY1eV090u5n6fR5RefEFyZ3jZH820NtuDc4HZ9Isz63IeDv6dPA0FeHU3P0TJ15O9mzf4d00ffMeaX8qvS2i8U3CX7Df9r5x00Fn2UJT3Q1btEa4X0kiy1c0L2P0ao4LB0J1RB17cJf6O17e84rc8M9pbcvuu01d2N1R6aW1FBMVS20c6A6cs5C586Tlc2dJFGxsB"
        resp = httpGet("http://raven520.top/getToken?auth="+auth)
        if resp.status_code == 200:
            appendStr =''
            tipStr = ''
            lastStr = ''
            if st.find('0')>=0:
                appendStr = '&type=0'
                tipStr = "点击该链接，输入您的账号(手机号)和密码登录即可。"
                lastStr = '请您先再易班试对了账号密码再在我的网站登录，不然后台登不进去！！谢谢配合~'
            elif st.find('1')>=0:
                appendStr = '&type=1'
                tipStr = "点击该链接，输入您的学号和身份证后六位登录即可。"
                lastStr = '直接登录该网站即可满分，无需校园网。'
            res =  tipStr+"请用浏览器打开该链接。http://raven520.top/sport?token="+resp.text+appendStr+" \n温馨提示：直接点击该私密链接登录即可获取分数。如果提示服务链接失败，请您刷新页面！\nps："+lastStr
            # 如果获取的QQ不是我的QQ
            if qqNum not in myQQs:
                #那么设置他的可用次数 -1
                useNum = useNum -1 
                updateNum(qqNum,useNum)
                logger.info("<%s>获取了体育在线测试的Token,他目前还可以获取：%d 次" %(qqNum,useNum))
        else:
            res = "当前访问过于频繁，请稍后再试！"
        pyperclip.copy(res)
       
        return res,useNum
    else:

        return "您还没有权限获取密令呢~,如果您需要体育在线答题密令,请联系管理员<衣服架子>,成功转账之后再与我联系,向我 发送 密令 即可。",None


 
