import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

with open('za.txt', "r", encoding='utf8') as f:
    za_txt = f.read()

seg_list = jieba.cut(za_txt, cut_all=False)

rm_list = ['我覺']
text = ' '.join(filter(lambda s: None if s in rm_list else s, seg_list))


wc = WordCloud(font_path='NotoSerifCJKtc-Regular.otf',
               relative_scaling=.75, width=1280, height=720).generate(text)
wc.to_file('za_cloud.png')

plt.imshow(wc)
plt.axis("off")
plt.show()
