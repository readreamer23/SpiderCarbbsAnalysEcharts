#coding:utf-8
from pyecharts import Bar
import sys
from config import mongoutil

#车载导航用户体验统计

reload(sys)
sys.setdefaultencoding('utf-8')

#client=pymongo.MongoClient(host='127.0.0.1', port=27017)
#comments = client.qichezhijia.qichezhijia1
comments = mongoutil.getCollection1()

print('数据记录条数count:', comments.estimated_document_count())
cursor = comments.find()
text = ''.join(map(lambda doc: doc.get('comment'), cursor))

attr = ["高精度地图","地图好用","导航准","导航不准","寻错路","更新慢","反应快"]
v1 = [0,0,0,0,0,0,0]
for index,i in enumerate(attr):
    attri=attr[index]
    print attri
    count=text.count(attri)
    v1[index]=count
    
print v1

bar = Bar("车载导航用户体验统计")
bar.add("车载导航用户体验统计", attr, v1, is_stack=True)
bar.render(r'../templates/carnavigation.html')

