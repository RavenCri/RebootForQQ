import sqlite3
# 更新QQ 的token可用次数
def updateNum(qqNum,useNum):
    conn = sqlite3.connect('C:/Users/raven/Desktop/reboot/test.db')
    
    cursor = conn.cursor()
    
    c =  cursor.execute('update token set num='+str(useNum)+'   where QQNum = \''+str(qqNum)+'\'')
    if useNum == 0:
        c =  cursor.execute('delete from token   where QQNum = \''+str(qqNum)+'\'')
    cursor.close()
     #提交事务：
    conn.commit()
    #关闭connection：
    conn.close()

# 获取QQ的token可用次数
def selectNumByQQId(qqNum):
   
    conn = sqlite3.connect('C:/Users/raven/Desktop/reboot/test.db')
    #创建一个cursor：
    cursor = conn.cursor()
    #插入一条记录：
    c =  cursor.execute('select  num from token where QQNum = \''+str(qqNum)+'\'')
  
    for row in c:
        return row[0]


# 获取所有QQ的可用次数
def getQQList():
   qqList = {}
   conn = sqlite3.connect('C:/Users/raven/Desktop/reboot/test.db')
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



# 添加QQ
def addQQUsedNum(QQNum,num):
    conn = sqlite3.connect('C:/Users/raven/Desktop/reboot/test.db')
    #创建一个cursor：
    cursor = conn.cursor()
    #如果QQ 已经存在数据表中
    currQQList = getQQList()
    if QQNum in currQQList:
        # 次数 改变 为原有次数 + 要增加的次数
        updateNum(QQNum,currQQList.get(QQNum)+num)
        return
    cursor.execute('insert into token (QQNum, num) values (\''+QQNum+'\','+str(num)+')')
    cursor.close()
    conn.commit()
    conn.close()