#coding=utf-8
"""
  工程服务运行入口.
"""
from __future__ import unicode_literals

import random
import datetime

from flask import Flask, render_template
from flask.templating import Environment
from pyecharts import Bar
from pyecharts import HeatMap, Map
from pyecharts.engine import ECHAERTS_TEMPLATE_FUNCTIONS
from pyecharts.conf import PyEchartsConfig
from analysis.cararea import  getCarAreaValues
from analysis.cararea import  getCarAreaAttrs
from analysis.buypurpose import getBuyPurPoseData
from analysis.buypurpose_all import getBuyPurPoseDataByType

# ----- Adapter ---------
class FlaskEchartsEnvironment(Environment):
    def __init__(self, *args, **kwargs):
        super(FlaskEchartsEnvironment, self).__init__(*args, **kwargs)
        self.pyecharts_config = PyEchartsConfig(jshost='/static/js')
        self.globals.update(ECHAERTS_TEMPLATE_FUNCTIONS)


# ---User Code ----

class MyFlask(Flask):
    jinja_environment = FlaskEchartsEnvironment


app = MyFlask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/heatmap/")
def heatmap():
    hm = create_heatmap()
    return render_template('heatmap.html', hm=hm)


def create_heatmap():
    begin = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 12, 31)
    data = [[str(begin + datetime.timedelta(days=i)),
             random.randint(1000, 25000)] for i in
            range((end - begin).days + 1)]
    heatmap = HeatMap("日历热力图示例", "某人 2017 年微信步数情况", width=1100)
    heatmap.add("", data, is_calendar_heatmap=True,
                visual_text_color='#000', visual_range_text=['', ''],
                visual_range=[1000, 25000], calendar_cell_size=['auto', 30],
                is_visualmap=True, calendar_date_range="2017",
                visual_orient="horizontal", visual_pos="center",
                visual_top="80%", is_piecewise=True)
    return heatmap


@app.route('/fujian/')
def fujian():
    value = [20, 190, 253, 77, 65]
    attr = ['福州市', '厦门市', '南平市', '泉州市', '三明市']
    map = Map("福建地图示例", width='100%', height=600)
    map.add("", attr, value, maptype='福建', is_visualmap=True,
            visual_text_color='#000')
    return render_template('fujian_map.html', m=map)


@app.route('/mytest1/')
def mytest1():
    value = [120, 120, 120, 120, 120]
    attr = ['福州市', '厦门市', '南平市', '泉州市', '三明市']
    map = Map("福建地图示例", width='100%', height=900)
    map.add("", attr, value, maptype='福建', is_visualmap=True,
            visual_text_color='#000')
    return render_template('mytest1.html', m=map)



@app.route('/buypurpose/')
def buypurpose():
    result=getBuyPurPoseData() 
    attr =  result[0]
    value = result[1]
    bar = Bar("荣威RX5购车目的统计示例图")
    bar.add("荣威RX5购车目的统计", attr, value, is_stack=True)
    return render_template('buypurpose.html',m=bar)

#领克02
@app.route('/buypurpose/3')
def buypurpose3():
    result=getBuyPurPoseDataByType('3') 
    attr =  result[0]
    value = result[1]
    bar = Bar("领克02车型购车目的统计图")
    bar.add("领克02车型购车目的统计", attr, value, is_stack=True)
    return render_template('buypurpose_type.html',m=bar)

#广汽GE3
@app.route('/buypurpose/4')
def buypurpose4():
    result=getBuyPurPoseDataByType('4') 
    attr =  result[0]
    value = result[1]
    bar = Bar("广汽GE3车购车目的统计图")
    bar.add("广汽GE3车购车目的统计", attr, value, is_stack=True)
    return render_template('buypurpose_type.html',m=bar)

#宝马3系
@app.route('/buypurpose/5')
def buypurpose5():
    result=getBuyPurPoseDataByType('5') 
    attr =  result[0]
    value = result[1]
    bar = Bar("宝马3系车购车目的统计图")
    bar.add("宝马3系车购车目的统计", attr, value, is_stack=True)
    return render_template('buypurpose_type.html',m=bar)

#蔚来ES8
@app.route('/buypurpose/6')
def buypurpose6():
    result=getBuyPurPoseDataByType('6') 
    attr =  result[0]
    value = result[1]
    bar = Bar("蔚来ES8车购车目的统计图")
    bar.add("蔚来ES8车购车目的统计", attr, value, is_stack=True)
    return render_template('buypurpose_type.html',m=bar)

#奔驰C级
@app.route('/buypurpose/7')
def buypurpose7():
    result=getBuyPurPoseDataByType('7') 
    attr =  result[0]
    value = result[1]
    bar = Bar("奔驰C级车购车目的统计图")
    bar.add("奔驰C级车购车目的统计", attr, value, is_stack=True)
    return render_template('buypurpose_type.html',m=bar)

#长安CS35 PLUS车型
@app.route('/buypurpose/8')
def buypurpose8():
    result=getBuyPurPoseDataByType('8') 
    attr =  result[0]
    value = result[1]
    bar = Bar("长安CS35 PLUS车购车目的统计图")
    bar.add("长安CS35 PLUS车购车目的统计", attr, value, is_stack=True)
    return render_template('buypurpose_type.html',m=bar)


#车辆区域分布统计--上下滑动效果
@app.route('/cararea/')
def cararea():
    value = getCarAreaValues()
    attr = getCarAreaAttrs()
    map = Map("车辆区域分布统计", width='100%', height=600)
    map.add("", attr, value, maptype='china', is_visualmap=True, is_label_show=True,
            visual_text_color='#000',
            visual_range=[0, 10000]
            )
    return render_template('cararea.html', m=map)
    

#车辆区域分布统计---定义值区间效果
@app.route('/cararea/2')
def cararea2():
    value = getCarAreaValues()
    attr = getCarAreaAttrs()
    map = Map("车辆区域分布统计", width='100%', height=600)
    map.add("", attr, value, maptype='china', is_visualmap=True, is_label_show=True,
            visual_text_color='#000',
            is_piecewise=True,
            pieces=[
                {"max": 1000000, "min": 20001, "label": "2万-100万值"},
                {"max": 20000, "min": 10001, "label": "10001-20000值"},
                {"max": 10000, "min": 8001, "label": "8001-10000值"},
                {"max": 8000, "min": 7001, "label": "7001-8000值"},
                {"max": 7000, "min": 6001, "label": "6001-7000值"},
                {"max": 6000, "min": 5001, "label": "5001-6000值"},
                {"max": 5000, "min": 4001, "label": "4001-5000值"},
                {"max": 4000, "min": 3001, "label": "3001-4000值"},
                {"max": 3000, "min": 2001, "label": "2001-3000值"},
                {"max": 2000, "min": 1001, "label": "1001-2000值"},
                {"max": 1000, "min": 501, "label": "501-1000值"},
                {"max": 500, "min": 101, "label": "101-500值"},
                {"max": 100, "min": 11, "label": "11-100值"},
                {"max": 10, "min": 0, "label": "0-10值"},
            ]
            )
    return render_template('cararea.html', m=map)
       


#导航用户体验图
@app.route('/carnavigation/')
def carnavigation():
    return render_template('carnavigation.html')

@app.route('/huscreen/')
def huscreen():
    return render_template('huscreen.html')


#论坛词频统计
@app.route('/ciyun/')
def ciyun():
    return render_template('ciyun.html')

#长安CS35 PLUS论坛词频统计
@app.route('/ciyun/changanCS35PLUS')
def ciyun_changan_cs35plus():
    return render_template('ciyun/ciyun_changan_cs35plus.html')


#荣威RX5-口碑--满意的地方
@app.route('/ciyun/1/manyi')
def ciyun_rongwei_manyi():
    return render_template('ciyun/ciyun_1_manyi.html')

#荣威RX5-口碑--不满意的地方
@app.route('/ciyun/1/bumanyi')
def ciyun_rongwei_bumanyi():
    return render_template('ciyun/ciyun_1_bumanyi.html')

#荣威RX5-口碑---空间
@app.route('/ciyun/1/kongjian')
def ciyun_rongwei_kongjian():
    return render_template('ciyun/ciyun_1_kongjian.html')

#领克02---满意的地方
@app.route('/ciyun/3/manyi')
def ciyun_lingke_manyi():
    return render_template('ciyun/ciyun_3_manyi.html')

#领克02---不满意的地方
@app.route('/ciyun/3/bumanyi')
def ciyun_lingke_bumanyi():
    return render_template('ciyun/ciyun_3_bumanyi.html')

#领克02---空间
@app.route('/ciyun/3/kongjian')
def ciyun_lingke_kongjian():
    return render_template('ciyun/ciyun_3_kongjian.html')



#广汽GE3---满意的地方
@app.route('/ciyun/4/manyi')
def ciyun_gqGE3_manyi():
    return render_template('ciyun/ciyun_4_manyi.html')

#广汽GE3---不满意的地方
@app.route('/ciyun/4/bumanyi')
def ciyun_gqGE3_bumanyi():
    return render_template('ciyun/ciyun_4_bumanyi.html')

#广汽GE3---空间
@app.route('/ciyun/4/kongjian')
def ciyun_gqGE3_kongjian():
    return render_template('ciyun/ciyun_4_kongjian.html')

#宝马3系---满意的地方
@app.route('/ciyun/5/manyi')
def ciyun_BMW3_manyi():
    return render_template('ciyun/ciyun_5_manyi.html')

#宝马3系---不满意的地方
@app.route('/ciyun/5/bumanyi')
def ciyun_BMW3_bumanyi():
    return render_template('ciyun/ciyun_5_bumanyi.html')

#宝马3系---空间
@app.route('/ciyun/5/kongjian')
def ciyun_BMW3_kongjian():
    return render_template('ciyun/ciyun_5_kongjian.html')

#蔚来ES8---满意的地方
@app.route('/ciyun/6/manyi')
def ciyun_WLes8_manyi():
    return render_template('ciyun/ciyun_6_manyi.html')

#蔚来ES8---不满意的地方
@app.route('/ciyun/6/bumanyi')
def ciyun_WLes8_bumanyi():
    return render_template('ciyun/ciyun_6_bumanyi.html')

#蔚来ES8---空间
@app.route('/ciyun/6/kongjian')
def ciyun_WLes8_kongjian():
    return render_template('ciyun/ciyun_6_kongjian.html')

#奔驰C级---满意的地方
@app.route('/ciyun/7/manyi')
def ciyun_BENZC_manyi():
    return render_template('ciyun/ciyun_7_manyi.html')

#奔驰C级---不满意的地方
@app.route('/ciyun/7/bumanyi')
def ciyun_BENZC_bumanyi():
    return render_template('ciyun/ciyun_7_bumanyi.html')

#奔驰C级---空间
@app.route('/ciyun/7/kongjian')
def ciyun_BENZC_kongjian():
    return render_template('ciyun/ciyun_7_kongjian.html')

#长安CS35 PLUS-口碑--满意的地方
@app.route('/ciyun/8/manyi')
def ciyun_changan_cs35plus_manyi():
    return render_template('ciyun/ciyun_8_manyi.html')

#长安CS35 PLUS-口碑--不满意的地方
@app.route('/ciyun/8/bumanyi')
def ciyun_changan_cs35plus_bumanyi():
    return render_template('ciyun/ciyun_8_bumanyi.html')

#长安CS35 PLUS-口碑--空间
@app.route('/ciyun/8/kongjian')
def ciyun_changan_cs35plus_kongjian():
    return render_template('ciyun/ciyun_8_kongjian.html')




#按词云生成的分词字符计算的每个字符的总数量
@app.route('/ciyuncountwords/')
def ciyuncountwords():
    return render_template('ciyuncountwords.html')

#仪表数据饼图
@app.route('/motormetercount/')
def motormetercount():
    return render_template('motormetercount.html')



#app.run(port=10200)

app.run(host='0.0.0.0',port=10200)
