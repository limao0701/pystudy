import urllib
import  urllib2
request=urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()

values={}
values['username'] = "1016903103@qq.com"
values['password']="XXXX"
data = urllib.urlencode(values)
print data
