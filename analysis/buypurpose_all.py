#coding:utf-8
import sys
from config import mongoutil

#购车目的柱形图

reload(sys)
sys.setdefaultencoding('utf-8')

def getBuyPurPoseDataByType(cartype):
    collection_koubei=mongoutil.getCollectionKoubei()
    #print('数据记录条数count:', comments.estimated_document_count())
    cursor = collection_koubei.find({"type":cartype})
    text = ','.join(map(lambda doc: doc.get('buypurpose'), cursor))
    print text
    attr = ["上下班","接送小孩","购物","自驾游","跑长途","拉货","泡妞","越野","商务接送"]
    values = [0,0,0,0,0,0,0,0,0]
    result=[0,0]
    for index,i in enumerate(attr):
        attri=attr[index]
        count=text.count(attri)
        values[index]=count
        
    result[0]=attr
    result[1]=values
    return result


if __name__=='__main__':
    result=getBuyPurPoseDataByType(8)
    print result[0]
    print result[1]


