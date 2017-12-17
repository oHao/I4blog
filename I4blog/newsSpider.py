import requests
from bs4 import BeautifulSoup

class newsSpider(object):
    """docstring for newsSpider"""
    def __init__(self, arg):
        super(newsSpider, self).__init__()
        self.arg = arg
        
    def getNews():
        url = "http://geek.csdn.net/"
        res = requests.get(url)
        content = BeautifulSoup(res.text, "html.parser")
        newslist = content.select("#geek_list > .geek_list > dd > span a")
        newslistmsg = content.select("#geek_list > .geek_list > dd > .list-inline li ")
        ''' 这个暂时不可用'''
        for msg in newslistmsg:
            print(msg.select('a').text)
        for link in newslist:
            print(link.text,link.get('href'))


newsSpider.getNews()
