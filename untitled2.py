# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:16:30 2018

@author: lenovo
"""





import urllib.request as r
tianqisrc='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
info=r.urlopen(tianqisrc.format(city)).read().decode('utf-8','ignore')
print(info)

import json
shuju=json.loads(info)


xuhao1=shuju['list'][3]
xuhao2=shuju['list'][11]
xuhao3=shuju['list'][19]
xuhao4=shuju['list'][27]
xuhao5=shuju['list'][35]
xuhao=[xuhao1,xuhao2,xuhao3,xuhao4,xuhao5]



print("您现在已进入全球天气系统，欢迎查看未来7天城市天气！")
print("\n")
j=1
for i in [3,11,19,27,35]:
    xuhao=shuju['list'][i]
    
    temp=xuhao['main']['temp']
    print("当前城市第"+str(j)+"天的气温是："+str(temp))
    
    maxtemp=xuhao['main']['temp_max']   
    print("当前城市第"+str(j)+"天的最高气温是："+str(maxtemp))
    
    pressure=xuhao['main']['pressure']
    print("当前城市第"+str(j)+"天的气压是："+str(pressure))
    
    weather=xuhao['weather'][0]['description']
    print("当前城市第"+str(j)+"天的天气情况是："+str(weather))
    print("\n")
    j=j+1
    
   





















