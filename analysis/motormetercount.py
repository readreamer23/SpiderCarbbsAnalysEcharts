#coding:utf-8

from pyecharts import Pie
import sys
from config import mongoutil

#仪表数据统计---饼图

reload(sys)
sys.setdefaultencoding('utf-8')

#client=pymongo.MongoClient(host='127.0.0.1', port=27017)
#client=mongoutil.getClient()
#comments = client.qichezhijia.qichezhijia1
comments=mongoutil.getCollection1()
print('数据记录条数count:', comments.estimated_document_count())
cursor = comments.find()
text = ''.join(map(lambda doc: doc.get('comment'), cursor))
    
attr = ["数字仪表盘", "高大上", "炫酷", "体验好", "看不懂", "鸡肋"]
v1=[0,0,0,0,0,0]
for index,i in enumerate(attr):
    attri=attr[index]
    print attri
    count=text.count(attri)
    v1[index]=count
    
print v1
pie = Pie("仪表盘数据统计")
pie.add("", attr, v1, is_label_show=True)
pie.render(r'../templates/motormetercount.html')

