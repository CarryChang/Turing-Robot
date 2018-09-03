

from django.http import HttpResponse
from django.shortcuts import render
from snownlp import SnowNLP
from urllib import request as req
from bs4 import BeautifulSoup
from urllib import parse


i1 = parse.quote_plus('1')
url = 'https://baike.baidu.com/item/{}'.format(i1)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36",
           "HOST":"baike.baidu.com"
           }
html1 = req.urlopen(req.Request(url,headers=headers)).read().decode('utf-8')
soup = BeautifulSoup(html1,'lxml')
data = soup.find('div',class_='lemma-summary')
print(data.text)