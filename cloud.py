from many_stop_words import get_stop_words
from nltk.tokenize import RegexpTokenizer
from pyMorfologik import Morfologik
from pyMorfologik.parsing import ListParser
from collections import Counter

def tagging(rawtekst):
    logger = open('logger.txt','a',encoding='UTF-8')
    stop_words = list(get_stop_words('pl'))
    tokenizer = RegexpTokenizer(r'\w+')
    if rawtext != None:
        d = tokenizer.tokenize(rawtekst.lower())
    else:
        d= []
    text =  [i for i in d if i not in stop_words]
    parser = ListParser()
    stemmer = Morfologik()
    y = stemmer.stem(text, parser)
    lista = []git init
    for index,i in enumerate(y):
        rtext = str(y[index][1]).replace('[','').replace(']','').replace('}','').replace('{','').replace("'",'').split(':')[0]
        if rtext != '' and len(rtext)>1:
            lista.append(rtext)
            logger.write(rtext+', ')
        else:
            pass
    counts = Counter(lista)
    top10 = []
    for index, i in enumerate(counts.most_common()):
        if index < 21:
           top10.append(i[0])
    logger.write('\n')
    logger.close()
    return top10