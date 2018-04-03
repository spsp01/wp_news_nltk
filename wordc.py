from wordcloud import WordCloud
import matplotlib.pyplot as plt
text= open('logger.txt','r',encoding='UTF-8').read().replace('\n',' ').replace(',','')


wordcloud = WordCloud(width=800, height=400).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
