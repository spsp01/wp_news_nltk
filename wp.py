import requests
import lxml
from bs4 import BeautifulSoup
import nltk
from wordcloud import WordCloud
from many_stop_words import get_stop_words
from nltk.tokenize import RegexpTokenizer
from pyMorfologik import Morfologik
from pyMorfologik.parsing import ListParser
from collections import Counter
from cloud import tagging
import json

url2 = 'https://wiadomosci.wp.pl/holendrzy-zdobyli-kluczowe-informacje-o-rosyjskim-wywiadzie-hakerzy-zhakowali-hakerow-6213535075752065a'

#Pobiera like
def likes(url):
    likes = requests.get('https://graph.facebook.com/?id='+url)
    return likes.json()['share']['share_count']

def req(url):
    try:
        page = requests.get(url).text
    except requests.exceptions.HTTPError as err:
        page = ''
    soup = BeautifulSoup(page, 'lxml')
    return soup

def article_wp(url):
    soup = req(url)
    article = soup.find('article')
    return article

def article(url):
    article = article_wp(url)
    try:
        if article.find("div", {"class": "xU1sB_3"}) != None:
             article.find("div", {"class": "xU1sB_3"}).decompose()  # remove svg
        if article.find("div", {"class": "_1Qq9oHQ"}) != None:
             article.find("div", {"class": "_1Qq9oHQ"}).decompose()  # remove polub
        if article.find("div", {"data-st-area": "article-header"}) != None:
            article.find("div", {"data-st-area": "article-header"}).decompose()
    except:
          pass
    if article != None:
        return article.get_text()
#Pobiera tytuł
def title(url):
    soup = req(url)
    return soup.title.get_text()

#token = nltk.word_tokenize(article('https://wiadomosci.wp.pl/w-komisji-sprawiedliwosci-pe-burzliwa-debata-na-temat-praworzadnosci-w-polsce-6184976547022465a'))

slowa = []

def open_links():
    d = {}
    text = ''
    with open('linki.txt') as f:
     for line in f:
        b = line.strip('\n')
        #tokens.append(nltk.word_tokenize(article(b)))
        print(b)
        tagi = tagging(download_article(b))
        print(tagi)
        d[b] = tagi
    print(d)
    open('json.json','w',encoding='UTF-8').write(json.dumps(d, ensure_ascii=False))
    #return str(text)

def download_article(url):
    if article(url) != None:
         text = article(url).replace('\r', '').replace('\n', '')
    else:
        text = article(url)

    return text

#raw = download_article('https://wiadomosci.wp.pl/przebral-sie-w-stroj-pielegniarki-i-sprobowal-zgwalcic-pacjentke-6205685737444993a')



import matplotlib.pyplot as plt

open_links()
#open('output.txt','w', encoding='UTF-8').write(open_links())

#print(tokens)
#print(url2+'\n' +str(likes(url2))+'\n' + title(url2)+'\n'+ str(len(article(url2))))
