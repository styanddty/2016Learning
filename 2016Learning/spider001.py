# python3.4 爬虫教程
# 一个简单的示例爬虫
# 林炳文Evankaka(博客：http://blog.csdn.net/evankaka/)
import urllib.request
url = "http://www.nwsuaf.edu.cn/"
hds = [{'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
       {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
       {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]
req = urllib.request.Request(url, headers=hds[0])
webPage = urllib.request.urlopen(req)
data = webPage.read()
data = data.decode('UTF-8')
print(data)
# print(type(webPage))
# print(webPage.geturl())
# print(webPage.info())
# print(webPage.getcode())
