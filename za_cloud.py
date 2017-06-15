# coding=utf-8
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

with open('za.txt', "r", encoding='utf8') as f:
    za_txt = f.read()
za_txt = za_txt.replace('comic LO', 'ComicLO')

jieba.set_dictionary('dict.txt.big')
words = ['覺得', '醒來', '貧乳', '小二', '三次元', '然後', '四糸乃', '的話', '約會',
         '夾心酥', '9歲', '14歲', '性慾 ', '短褲', '人妻', '韻味', '若隱若現', '幼稚園', '小學生', '房間']
for word in words:
    jieba.add_word(word)

seg_list = list(jieba.cut(za_txt, cut_all=False))
text = ' '.join(seg_list)

wc = WordCloud(font_path='NotoSerifCJKtc-Regular.otf',
               relative_scaling=.75, width=1280, height=720).generate(text)
wc.to_file('za_cloud.png')

plt.imshow(wc)
plt.axis("off")
plt.show()
