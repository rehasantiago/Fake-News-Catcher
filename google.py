#!C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36\\python.exe
import cgi
import sys
import requests
import string
import lxml.html
import random
from urllib.parse import urlencode
from urllib.parse import urlparse
import functionMatch as mat
import os

global input
with open('input.txt','r') as f:
    input=f.read()
global START_URL
START_URL="https://www.google.com/search?q="
global TRUSTED_WEBS
TRUSTED_WEBS=['https://timesofindia.indiatimes.com/','https://www.ndtv.com/','https://www.indiatoday.in/']
global l
l=[]
global article
article=[]
def request_site(url):
    
    user_agent_list = [
    #Chrome
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        #Firefox
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
    ]

    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    response = requests.get(url,headers=headers)
    return response
def formated_string(a):
    a=a.replace(" ","+")
    return a
def retrn_response(sentence):
    sentence=formated_string(sentence)
    url=START_URL+sentence
    
    scrape(url)
def scrape(url):
    response=request_site(url)
    tree=lxml.html.fromstring(response.text)
    news_url=tree.xpath("//h3[@class='LC20lb']/text()")
    links=tree.xpath("//div[@class='r']//a/@href")
    for i in links:
        parsed_uri = urlparse(i)
        result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        for j in TRUSTED_WEBS:
            if result!=j:
                pass
            else:
                l.append(i)
    


def toi(url):
    response=request_site(url)
    tree=lxml.html.fromstring(response.text)
    para=tree.xpath("//div[@class='Normal']/descendant::text()")
    para_news=''
    for i in para:
        para_news=para_news+i

    para_news = para_news.replace('"','')
    para_news = para_news.replace('\n',' ')
    para_news = para_news.replace('*','')
    para_news = para_news.replace('—','')
    para_news = para_news.replace("'",'')
    article.append(para_news)

def ndtv(url):
    response=request_site(url)
    tree=lxml.html.fromstring(response.text)
    para=tree.xpath("//div[@class='ins_storybody']//p/text()")
    para_news=''
    for i in para:
        para_news=para_news+i

    para_news = para_news.replace('"','')
    para_news = para_news.replace('\n',' ')
    para_news = para_news.replace('*','')
    para_news = para_news.replace('—','')
    para_news = para_news.replace("'",'')
    article.append(para_news)


def it(url):
    response=request_site(url)
    tree=lxml.html.fromstring(response.text)
    para=tree.xpath("//div[@class='description']//p/text()")
    para_news=''
    for i in para:
        para_news=para_news+i

    para_news = para_news.replace('"','')
    para_news = para_news.replace('\n',' ')
    para_news = para_news.replace('*','')
    para_news = para_news.replace('—','')
    para_news = para_news.replace("'",'')
    article.append(para_news)

userart = input
retrn_response(userart)
count=0
if l==[]:
    if count==0:
        count=count+1
        retrn_response(userart)

for i in l:
    
    parsed_uri = urlparse(i)
    result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    if result==TRUSTED_WEBS[0]:
        toi(i)
    elif result==TRUSTED_WEBS[1]:
        ndtv(i)
    elif result==TRUSTED_WEBS[2]:
        it(i)
    else:
        pass
    
final = mat.runApp(article,userart)
#final is comparison values 
#article has all articles 
#l has all links for articles
i=0
while i<len(final):
	check = int(final[i])
	if check>=9:
	    print('the given news is legit  and relevents articles are as follows',l)
	    sys.exit(1)
	i=i+1
print('The news is fake')