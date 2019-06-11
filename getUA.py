# import requests as re, json, time, random, os
# from bs4 import BeautifulSoup as bs
# from UserAgentGetter.UserAgentGetter import UserAgentGetter
# by A.Stoev
# Modified by V.Varbanovski

name = "UserAgentGetter"
import requests as re, json, time, random, os
from bs4 import BeautifulSoup as bs
from pprint import pprint

"""UserAgentGetter is a simple package which provides"""
def newUA():

    data = {}
    resp = re.get("https://bannerblue.dev.publix.bgnews.info/visuallog/UAinfo.html", params={
        'Host':'techblog.willshouse.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language':'en-US,en;q=0.5',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests':'1',
    })
    soup = bs(resp.text, "lxml")
    div = soup.select('.useragent')
    i = 0
    for row in div[1:21]:
        data[i]=row.text
        i+=1
    data['time'] = time.time()
    file = open(os.path.join(os.path.dirname(__file__), 'ua.json'), "w+")
    file.write(json.dumps(data))
    print(data)
    file.close()
def UA():
       
       a = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11"
       #a = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
       return a

