# -*- coding: utf-8 -*-
# 使用百度api
import sys, urllib, urllib2, json

class Weather(object):
	def __init__(self, citystr):
		city = citystr.encode('utf-8')#Windows Powershell下输入中文为gb2312编码，api接受utf-8编码
		url = 'http://apis.baidu.com/apistore/weatherservice/cityname?cityname='+urllib.quote(city)
		req = urllib2.Request(url)
		req.add_header("apikey", "f6b8377dddfbcf73886365c8345aaa75")
		resp = urllib2.urlopen(req)
		content = resp.read()
		if(content):
			self.__res = json.loads(content)

	def weatherdata(self):
		if self.__res['errNum'] == -1:
			return -1
		else:
			return self.__res

def test():
	testwea = Weather(u'北京')
	from pprint import pprint
	pprint(testwea.weatherdata())
	wd=testwea.weatherdata()['retData']
	print u"查询城市：\n"+wd["city"]+u"\n"+u"城市坐标：\n"+u"东经："+str(wd["longitude"])+u"，北纬："+str(wd["latitude"])+u"\n"+u"海拔高度：\n"+wd["altitude"]+u"米\n"+u"天气状况：\n"+wd["weather"]+u"\n"+u"最高温度：\n"+wd["h_tmp"]+u"摄氏度"+u"\n"+u"最低温度：\n"+wd["l_tmp"]+u"摄氏度"+u"\n"+u"风向：\n"+wd["WD"]+u"\n"+u"风速：\n"+wd["WS"]+u"\n"+u"日出时间：\n"+wd["sunrise"]+u"\n"+u"日落时间：\n"+wd["sunset"]+u"\n"+u"更新时间：\n"+wd["date"]+u"  "+wd["time"]

if __name__ == '__main__':
	test()