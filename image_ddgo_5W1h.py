import requests
import re
import json
import time
import logging
from fake_useragent import UserAgent
import itertools
from googletrans import Translator

def proxy():
    response = requests.get("https://www.proxy-list.download/api/v1/get?type=http&a}non=elite&country=ru")
    proxy = (response.text)
    proxt_list = proxy.split('\r\n')
    proxy_dict = dict(itertools.zip_longest(
        *[iter(proxt_list)] * 2, fillvalue=""))
    return proxy_dict
proxy_dict = proxy()

def get_transalation(text1):
    final_text=[]
    try:
        text1= text1.replace('।','.')
        text1=text1.split('.')
        translator = Translator(service_urls=['translate.google.co.in', 'translate.google.com'], user_agent=ua, proxies=proxy_dict)
        for txt in text1:
            transalation1= translator.translate(txt, dest="en" )
            eng_text= transalation1.text
            final_text.append(eng_text)

        final_text=('. '.join(final_text))
        print(final_text)
        return final_text

    except Exception as e:
        print(e)
        pass
    
def urlfinder(keywords):
    keywords=keywords
    logging.basicConfig(level=logging.DEBUG);
    logger = logging.getLogger(__name__)
   
    def search(keywords, max_results=None):
        url = 'https://duckduckgo.com/';
        params = {
        'q': keywords
        };
        logger.debug("Hitting DuckDuckGo for Token");
        #   First make a request to above URL, and parse out the 'vqd'
        #   This is a special token, which should be used in the subsequent request
        res = requests.post(url, data=params)
        searchObj = re.search(r'vqd=([\d-]+)\&', res.text, re.M|re.I);
        if not searchObj:
            logger.error("Token Parsing Failed !");
            return -1;
        logger.debug("Obtained Token");    
        headers = {
            'dnt': '1',
            #'accept-encoding': 'gzip, deflate, sdch, br',
            'x-requested-with': 'XMLHttpRequest',
            'accept-language': '*',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'referer': 'https://duckduckgo.com/',
            'authority': 'duckduckgo.com',
        }
        params = (
        ('l', 'wt-wt'),
        ('o', 'json'),
        ('q', keywords),
        ('vqd', searchObj.group(1)),
        ('f', ',,,'),
        ('p', '2')
        )
        requestUrl = url + "i.js";
        logger.debug("Hitting Url : %s", requestUrl);
        i=0
        while i<10:
            j=0
            while j<10:
                try:
                    res = requests.get(requestUrl, headers=headers, params=params);
                    data = json.loads(res.text);
                    break;
                except ValueError as e:
                    logger.debug("Hitting Url Failure - Sleep and Retry: %s", requestUrl);
                    time.sleep(5);
                    continue;
                j=j+1  
            logger.debug("Hitting Url Success : %s", requestUrl);
            printJson(data["results"]);
           
            i=i+1
   
    imageurl=[]
    specs=[]
    title=[]
    
    def printJson(objs):
        for obj in objs:
            specs.append(("Width {0}, Height {1}".format(obj["width"], obj["height"])))
            title.append( ("Title {0}".format(obj["title"].encode('utf-8'))))
            imageurl.append((obj["image"]))     
            
    search(keywords)
    #print(imageurl)
    return imageurl[:10],specs[:10],title[:10]


    