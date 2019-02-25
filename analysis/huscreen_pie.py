#coding:utf-8
from pyecharts import Pie
import sys
from config import mongoutil

#HU交互（大屏）用户体验统计

reload(sys)
sys.setdefaultencoding('utf-8')

comments=mongoutil.getCollection1()
print('数据记录条数count:', comments.estimated_document_count())
cursor = comments.find()
text = ''.join(map(lambda doc: doc.get('comment'), cursor))

attr = ["难用","反应慢","易死机","更新快","设计高大上","难看","交互差","交互好","上手快","上手慢","易用"]
v1 = [0,0,0,0,0,0,0,0,0,0,0]
for index,i in enumerate(attr):
    attri=attr[index]
    print attri
    count=text.count(attri)
    v1[index]=count
    
print v1
#HU交互（大屏）用户体验统计
pie = Pie("")
pie.add("",
        attr,
        v1,
        is_label_show=True,
        legend_orient="vertical",
        legend_pos="left",
    )
pie.render(r'../templates/huscreen.html')

