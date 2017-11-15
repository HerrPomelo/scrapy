# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:06:57 2017

@author: hp
"""
# 百度与360的关键词链接基本类似
import requests
keyword = "python"
try:
    kv= {'wd' : keyword}              
    # 如果是360的话则为kv=  {'q' : keyword}   http://www.so.com/s
    r = requests.get("http://www.baidu.com/s", params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')