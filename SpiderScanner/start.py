#!/usr/bin/python
import sys
from spider import StaticSpider
from spider import DynamicSpider
from scanner import DomxssScanner
from tools import Deldump
from tools import FileOperation
from spider import SpiderOperation
from test.test_decimal import file
from scanner import ScanOperation


def spiderURL(url,deep,spdomain):
    spider = SpiderOperation.SpiderOperation()
    spider.init(deep, url,spdomain)
    spider.startSpider()
    rurls = spider.getUrls()
    fileop = FileOperation.FileOperaton()
    fileop.fileWrite(rurls)
    
    print("===================================")
    print("共爬取到URL如下：")
    fr = fileop.fileRead()
    for u in fr.keys():
        print("%s %s" % (u,fr[u]))
    print(("==================================="))
    
def scannerDomxss():
    scanner = ScanOperation.ScanOperation();
    scanner.startScan()
    scanner.getScanresults()
    
def scanner(url,deep,spdomain):
    spiderURL(url, deep,spdomain)
    scannerDomxss()
'''
环境配置：
    1. python3.0   
    2. pip isntall selenium   模拟浏览器  
    3. pip install beautifulsoup4   安装HTML解析包
    4. pip install lxml
    5. 安装phantomjs:  需要修改DomxssScanner.py和DynamicSpider.py脚本中的配置，替换为当前环境的phantomjs路径
        webdriver.PhantomJS("/Users/snow/programs/phantomjs-2.1.1-macosx/bin/phantomjs",service_args=self.service_args)  
    6. pip install requests   安装HTTP包
    
'''
'''
说明：
    参数1:    url 待爬取的目标URL
    参数2:    deep 爬取的深度
    参数3:    爬取的域名
    运行示例:    python start.py http:www.baidu.com 2 baidu.com
'''       
if __name__ == "__main__":
    url = "http://47.104.218.243/info.html"
    deep = 2
    spdomain = 'www.baidu.com'
    if len(sys.argv) == 2:
        url = sys.argv[1]
    elif len(sys.argv) == 3:
        url = sys.argv[1]
        deep = int(sys.argv[2])
    elif len(sys.argv) == 4:
        url = sys.argv[1]
        deep = int(sys.argv[2])
        spdomain = sys.argv[3]
    else:
        print('test program.......')
        
    scanner(url,deep,spdomain)
