# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:16:30 2018

@author: lenovo
"""


print("您现在已进入全球天气系统，欢迎查看全球城市天气！")
import urllib.request as r
city=input("请输入您想查询城市的拼音:")

tianqisrc='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
info=r.urlopen(tianqisrc.format(city)).read().decode('utf-8','ignore')
print(info)

import json
shuju=json.loads(info)


print("您查询的城市是:"+city)
print("1.当前城市未来五天天气，2.查看其它城市天气")
menno=input("请输入菜单：")

if menno=='1':
    print("您正在查看当前城市未来五天天气")
    j=1
    for i in [3,11,19,27,35]:
        xuhao=shuju['list'][i]
    
        date=xuhao['dt_txt']
        temp=xuhao['main']['temp']
        maxtemp=xuhao['main']['temp_max']   
        pressure=xuhao['main']['pressure']
        weather=xuhao['weather'][0]['description']
        print("当前城市的第"+str(j)+"天"+"\n"+"时间是："+str(date)+"\n"+"气温是："+str(temp)+"摄氏度"+"\n"+"最高气温是："+str(maxtemp)+"摄氏度"+"\n"+"气压是："+str(pressure)+"帕"+"\n"+"天气情况是："+str(weather))
     
        print("\n")
        j=j+1
        
if menno=='2':
    print("查看其它城市天气")
    
    
input('输入任意键退出...')




















