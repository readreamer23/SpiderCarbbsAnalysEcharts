#coding:utf-8
import jieba
from jieba import analyse
import collections
from matplotlib import pyplot
from wordcloud import WordCloud
from config import mongoutil
from config import cartypeUtil

#生成词云
#cartype=自定义车型id, msgtype=统计关键词（满意，不满意等）
def ciYunType(cartype,msgtype):
    print 'cartype='+cartype+',msgtype='+msgtype
    comments=mongoutil.getCollectionKoubei()
    cursor = comments.find({"type":cartype})
    typestr=cartype+'_'+msgtype
    print '车型消息类型typestr='+typestr
    picname='wc_'+typestr+'.png'
    print '图片名称='+picname
    text = ''.join(map(lambda doc: doc.get(msgtype+'_msg'), cursor))
    print text
    jieba.load_userdict(r'../config/userdict.txt')
    analyse.set_stop_words(r'../config/stopwords_'+msgtype+'.txt')
    
    m=collections.Counter(text)
    tags = analyse.extract_tags(text, topK=40, withWeight=False)
    #词云所有词列表
    new_text = ' '.join(tags)
    validtext=new_text.replace(' ','')
    if validtext is None or validtext=='':
        return
    #圆形图设置开始
    #x,y = np.ogrid[:300,:300]
    #mask = (x-150) ** 2 + (y-150) ** 2 > 130 ** 2
    #mask = 355 * mask.astype(int)
    #圆形图设置结束
    
    wc = WordCloud(
        max_words=200,
        background_color='white', 
        scale=1,  # 默认之为1。可以理解为生成的图片像素密度值，值越大，图片密度越高，越清楚。  
        width=1099, 
        height=724,
        font_path=r'../example/fonts/FZXingKai-S04S.TTF').generate(new_text)
    
    # 绘图(标准长方形图)
    pyplot.imshow(wc, interpolation='bilinear')
    pyplot.figure()
    pyplot.axis('off')
    wc.to_file(r'../static/images/'+picname)


    
#重新生成所有数据词云    
def handleAllCarCiYun():
    cartypelist=cartypeUtil.getCarTypeList()
    for index,i in enumerate(cartypelist):
        typelist=i.split(',')
        print typelist
        ciYunType(typelist[0],typelist[3])
         
    

if __name__=='__main__':
    carType='8'
    msgType='kongjian'
    ciYunType(carType,msgType)
    #handleAllCarCiYun()
    
    