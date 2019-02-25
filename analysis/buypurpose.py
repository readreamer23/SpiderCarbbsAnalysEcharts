#coding:utf-8
import sys
from config import mongoutil

#购车目的柱形图

reload(sys)
sys.setdefaultencoding('utf-8')

def getBuyPurPoseData():
    collection_koubei=mongoutil.getCollectionKoubei()
    #print('数据记录条数count:', collection_koubei.estimated_document_count())
    cursor = collection_koubei.find({"type":'1'})
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
    #client.close()
    return result


if __name__=='__main__':
    result=getBuyPurPoseData()
    print result[0]
    print '-------------------'
    print result[1]


