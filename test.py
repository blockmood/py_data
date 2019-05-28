from urllib import request
from pyquery import PyQuery as pb
import pymysql

url = 'https://www.yw11.com'

result = []
result_url = []

f = request.urlopen(url + '/namelist.php')

content = f.read().decode('utf-8')

doc = pb(content)

a = doc('.listbox .e3 li').items()

db = pymysql.connect('localhost','root','','py_test')
cursor = db.cursor()

for i in a:
    url = i.children('a').attr('href')
    data = i.children('a').text()
    result.append(data)
    result_url.append(url)

sql = 'insert into py_surname(name,parent_id)VALUES(%s,%s)'

for i,val in enumerate(result):
   try:
       cursor.execute(sql,(val,i))
       db.commit()
       print('数据插入成功')
   except:
       db.rollback()
       print('插入失败')

sql1 = 'insert into py_name(name,parent_id)VALUES(%s,%s)'

for g,val in enumerate(result_url):
    print('打开了 https://www.yw11.com'+ val + '第' + str(g) + '个')
    c = request.urlopen('https://www.yw11.com' + val)
    v = c.read().decode('utf-8')
    doc1 = pb(v)
    array = doc1('.listbox1_text ul li').items()
    for k in array:
        try:
            cursor.execute(sql1, (k.text(), g))
            db.commit()
        except:
            db.rollback()
            print('插入失败')

