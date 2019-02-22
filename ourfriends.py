import itchat

def get_list():
    #在命令行生成登录二维码
    #itchat.auto_login(enableCmdQR=True)

    #获取登录二维码图片，扫码登录微信网页版
    itchat.auto_login()
    #获取好友信息列表
    friendList = itchat.get_friends(update=True)
    
    #每个登录的微信号生成一个好友信息列表
    contactlist = []
    for i in friendList:
        #好友信息列表中每个人，用一个字典来表示
        person = {}
        #为该好友的字典添加他的特征变量
        person["City"] = i["City"]
        person["PYQuanPin"] = i["PYQuanPin"]
        person["Province"] = i["Province"]
        person["PYInitial"] = i[ "PYInitial"]
        person["Sex"] = i["Sex"]
        person['Signature'] = i["Signature"]
        person['NickName'] = i["NickName"]
        #将该好友添加到列表中
        contactlist.append(person)
    #登出微信号
    itchat.logout()
    #返回该微信号好友信息列表
    return contactlist

#获取第一位扫码登录微信号的好友信息列表，注意，该列表的第一个元素是号主本人contactlist[0]，后面会用到
contactlist = get_list()
#获取第二位扫码登录微信号的好友信息列表，注意，该列表的第一个元素是号主本人contactlist2[0]，后面会用到
contactlist2 = get_list()

#共同好友计数
count = 0

#共同好友列表
common_list = []

#由于微信好友中可能存在除性别外信息全为空的好友，无法据此验证其身份，故先定义好无效身份方便后续排查
#无性别信息的空数据身份
empty = {"City":"","PYQuanPin":"","Province":"","PYInitial":"","Sex":0,'Signature':"",'NickName':""}
#性别为男的空数据
emptyM = {"City":"","PYQuanPin":"","Province":"","PYInitial":"","Sex":1,'Signature':"",'NickName':""}
#性别为女的空数据
emptyF = {"City":"","PYQuanPin":"","Province":"","PYInitial":"","Sex":2,'Signature':"",'NickName':""}

for i in contactlist:
    if i in contactlist2:
        #将两位微信号号主本人、无效身份信息好友在共同好友中排除
        if i not in[contactlist[0],contactlist2[0],empty,emptyM,emptyF]:
            #将符合条件的共同好友添加到列表中
            common_list.append(i)
            #共同好友数目计算
            count += 1
#用于展示共同好友信息的列表            
display=[]

for item in common_list:
    #用来描述每位共同好友信息的语句
    profile = ""
    #优先度是 昵称>用户名全拼>用户名缩写
    if item["NickName"]:
        profile+=f"好友昵称：{item['NickName']}"
    elif item["PYQuanPin"]:
        profile+=f"用户名全拼：{item['PYQuanPin']}"
    elif item["PYInitial"]:
        profile+=f"用户名缩写：{item['PYIntial']}"
    #若有地区信息，在其信息中添加“，省份城市”
    if item['Province'] or item['City']:
        profile+=f",{item['Province']}{item['City']}"
    #添加性别信息
    if item['Sex']==1:
        profile+=",男"
    elif item['Sex']==2:
        profile+=",女"
    #将个人描述语句添加到共同好友信息列表中
    display.append(profile)
    
#打开record.txt文档，若无则新建打开
with open("record.txt","w") as f:
    #将结果print出来
    print(f"你们共有{count}位共同好友(若除性别外其它信息为空，不在此记录)，他们分别是：")
    #将结果写入txt文档
    f.write(f"你们共有{count}位共同好友，他们分别是:\n")
    
    for i in display:
        #对共同好友列表中的信息，逐行打印和写入txt
        print(i)
        
        #这里采用try except的原因是有的好友信息中含有特殊字符，无法写入txt，若如此用提示语句代替该好友信息
        try:
            f.write(i+"\n")
        except:
            f.write("该好友信息中含有字符无法识别,请在窗口中查看\n")



