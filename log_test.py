from collections import Counter

f = open('logger.txt','r',encoding="UTF-8").read().replace('\n','')
lista = f.split(',')
counts = Counter(lista)
open('counter.txt','w', encoding='UTF-8').write(str(counts.most_common()))