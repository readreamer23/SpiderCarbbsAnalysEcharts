#coding:utf-8
from config import mongoutil
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def getCarAreaValues():
    return groupbyProvince()[1]



def getCarAreaAttrs():
    return groupbyProvince()[0]


#按省分组统计记录条数
def groupbyProvince():
    groupresult = mongoutil.groupbyType1("province","countprovince")
    grouplist = list(groupresult)
    attrlist=[]
    valuelist=[]
    result=[0,0]
    for i in grouplist:
        provincename=i['_id']    #省名称
        count=i['countprovince'] #省数量
        
        if not provincename is None and provincename.find('回')<0:
            attrlist.append(provincename)
            valuelist.append(count)
        else:
            provincename='无省份'   
        print provincename+str(count)
    
    result[0]=attrlist
    result[1]=valuelist
    return result


if __name__=='__main__':
    print groupbyProvince()


