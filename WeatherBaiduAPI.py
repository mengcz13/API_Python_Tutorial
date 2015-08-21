# -*- coding: utf-8 -*-
# 使用百度api
import sys, urllib, urllib2, json

print u'输入目标城市名称'
city = raw_input().decode('gb2312').encode('utf-8')#Windows Powershell下输入中文为gb2312编码，api接受utf-8编码
url = 'http://apis.baidu.com/apistore/weatherservice/cityname?cityname='+urllib.quote(city)

req = urllib2.Request(url)

req.add_header("apikey", "f6b8377dddfbcf73886365c8345aaa75")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    res = json.loads(content)

from pprint import pprint

if res['errNum']==-1:
	print u'查询失败',res['errMsg']
else:
	#print res['retData']['city'],':',res['retData']['weather']
	pprint(res)
	weainfo = res['retData']
	print u'城市'+':'+weainfo['city']
	print u'位置'+':'+u'经度'+str(weainfo['longitude'])+','+u'纬度'+str(weainfo['latitude'])
	print u'海拔高度'+':'+weainfo['altitude']+u'米'
	print u'城市代码'+':'+weainfo['citycode']
	print u'更新时间'+':'+weainfo['date']+' '+weainfo['time']
	print u'当前天气'+':'+weainfo['weather']
	print u'当前温度'+':'+weainfo['temp']+u'℃'
	