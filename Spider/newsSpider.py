import requests
from bs4 import BeautifulSoup


class newsSpider(object):
    """docstring for newsSpider"""

    def __init__(self):

        super(newsSpider, self).__init__()

    def getNews(self):
        url = "http://geek.csdn.net/"
        res = requests.get(url)
        content = BeautifulSoup(res.text, "html.parser")
        newslist = content.select("#geek_list > .geek_list > dd > span a")
        print(type(newslist))
        datas=[]
        for news in newslist :
            datas.append(spiderData(news.get('href'),news.text))
            
        return datas
class spiderData(object):
    """docstring for spiderData"""
    def __init__(self, href,text):
        super(spiderData, self).__init__()
        self.href = href
        self.text = text
        
newslist = newsSpider().getNews()
for news in newslist :
    print(news.href)
    print(news.text)
