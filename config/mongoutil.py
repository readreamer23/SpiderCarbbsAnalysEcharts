#coding:utf-8
import pymongo
import re

ip='127.0.0.1'
client=pymongo.MongoClient(ip,27017)
dbname='qichezhijia'

collectionname1='qichezhijia1'
collectionname2='qichezhijia2'
koubei='koubei'

def insertMongo1(content):
    db=client[dbname]
    collection=db[collectionname1]
    collection.insert(content)
    client.close()

def insertMongo2(content):
    db=client[dbname]
    collection=db[collectionname2]
    collection.insert(content)
    client.close()
    
def insertMongoKoubei(content):
    db=client[dbname]
    collection=db[koubei]
    collection.insert(content)
    client.close()    

def findByType(name,value):
    db=client[dbname]
    collection=db[collectionname1]
    query = { name: value }
    result = collection.find(query)
    return result


def getClient():
    mongoclient=pymongo.MongoClient(ip,27017)
    return mongoclient


def getCollection1():
    client1=getClient()
    db1=client1[dbname]
    collection1=db1[collectionname1]
    client1.close()
    return collection1


def getCollectionKoubei():
    client1=getClient()
    db1=client1[dbname]
    collection_koubei=db1[koubei]
    client1.close()
    return collection_koubei



def closeMongodb(client):
    client.close()

def groupbyType1(grouptype,grouptname):
    db=client[dbname]
    collection=db[collectionname1]
    pipe=[
                #{"$match":{"user":{"user":"user"}}},
                {"$group":{"_id":"$"+grouptype,grouptname:{"$sum":1}}}
                ]
    result = collection.aggregate(pipeline=pipe)
    client.close()
    return result

#指定条件分组计数
def groupbyType2(grouptype,grouptname,groupmatch):
    db=client[dbname]
    collection=db[collectionname1]
    pipe=[
                #{"$match":{"province":{"province":re.compile('回')}}},
                {"$match":{grouptype:re.compile(groupmatch)}},
                {"$group":{"_id":"$"+grouptype,grouptname:{"$sum":1}}}
                ]
    result = collection.aggregate(pipeline=pipe)
    client.close()
    return result



if __name__=='__main__':
    content={"test1":"test1"}
    print groupbyType2('province','provincecount','回')
    

