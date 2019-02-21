# -*- coding: cp949 -*-

import requests
from bs4 import BeautifulSoup


class Crawling :
    def __init__(self,url):
        self.url = url

    def rq(self):
        r=requests.get(self.url)
        return r.content
    
    def bs(self, content):
        r=BeautifulSoup(content,"html.parser")
        return r



class Boan(Crawling):

   def pins(self,s,m):
        ts=s.find_all(class_=m)
        for t in ts :
            print t.get_text()

class Inews(Crawling):

    def pins(self,ss):
        tss=ss.select("body > main > article > ol > li > a")
        for tt in tss :
            print tt.get_text()



if __name__ == "__main__" :

    print "boannews\n"
    boan = Boan("https://www.boannews.com/media/list.asp")
    r =boan.rq()
    s= boan.bs(r)
    boan.pins(s,"news_txt")

    print "inews\n"
    inews=Inews('http://www.inews24.com/list/it')
    rr=inews.rq()
    ss=inews.bs(rr)
    inews.pins(ss)

    
