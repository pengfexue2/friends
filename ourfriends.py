import itchat

def get_list():
    #在命令行生成登录二维码
    #itchat.auto_login(enableCmdQR=True)

    #获取登录二维码图片，扫码登录微信网页版
    itchat.auto_login()
    #获取好友信息列表
    friendList = itchat.get_friends(update=True)

    contactlist = []
    for i in friendList:
        person = {}
        person["City"] = i["City"]
        person["PYQuanPin"] = i["PYQuanPin"]
        person["Province"] = i["Province"]
        person["PYInitial"] = i[ "PYInitial"]
        person["Sex"] = i["Sex"]
        person['Signature'] = i["Signature"]
        person['NickName'] = i["NickName"]
        contactlist.append(person)
    itchat.logout()
    return contactlist


contactlist = get_list()
contactlist2 = get_list()
count = 0
common_list = []
empty = {"City":"","PYQuanPin":"","Province":"","PYInitial":"","Sex":0,'Signature':"",'Signature':"",'NickName':""}
emptyM = {"City":"","PYQuanPin":"","Province":"","PYInitial":"","Sex":1,'Signature':"",'Signature':"",'NickName':""}
emptyF = {"City":"","PYQuanPin":"","Province":"","PYInitial":"","Sex":2,'Signature':"",'Signature':"",'NickName':""}
for i in contactlist:
    if i in contactlist2:
        if i not in[contactlist[0],contactlist2[0],empty,emptyM,emptyF]:
            common_list.append(i)
            count += 1
display=[]
for item in common_list:
    profile = ""
    if item["NickName"]:
        profile+=f"好友昵称：{item['NickName']}"
    elif item["PYQuanPin"]:
        profile+=f"用户名全拼：{item['PYQuanPin']}"
    elif item["PYInitial"]:
        profile+=f"用户名缩写：{item['PYIntial']}"

    if item['Province'] or item['City']:
        profile+=f",{item['Province']}{item['City']}"
    if item['Sex']==1:
        profile+=",男"
    elif item['Sex']==2:
        profile+=",女"

    display.append(profile)

with open("record.txt","w") as f:
    print(f"你们共有{count}位共同好友(若除性别外其它信息为空，不在此记录)，他们分别是：")
    f.write(f"你们共有{count}位共同好友，他们分别是:\n")
    for i in display:
        print(i)
        try:
            f.write(i+"\n")
        except:
            f.write("该好友信息中含有字符无法识别,请在窗口中查看\n")



