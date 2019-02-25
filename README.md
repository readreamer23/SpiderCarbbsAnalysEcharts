# SpiderCarbbsSpiderAnalysis
python版本: 2.7

一、 概述
此工程是使用 flask 和 pyecharts (V0.3.0+)整合的一个项目，主要特点：
- 统计分析mongodb中数据，用图表的形式展示
- 整合 Flask 应用默认的模板引擎
- 完全使用本地的 js/css 等静态文件
- 模板文件可以使用模板文件

二、 使用
1 安装依赖库

```shell
pip install -r  requirements.txt
```

2 进入目录，运行脚本
```shell
python start_run.py
```

3 预览，访问浏览器 http://127.0.0.1:10200 即可。
	http://127.0.0.1:10200/buypurpose   购车目的柱状图
	http://127.0.0.1:10200/cararea      车辆区域分布全国地图	    

4.生产服务器部署启动服务脚本:   start.sh

