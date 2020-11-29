from wordcloud import WordCloud
import jieba

txt = open(r"E:\wordcloud.txt", "rb").read()
txtout = "".join(jieba.cut(txt, cut_all=False))
font = "E:\仓耳爱民小楷.ttf"
wc = WordCloud(font_path=font,
               background_color="white",
               contour_width=5,
               contour_color="lightblue",
               )
wc.generate(txtout)

wc.to_file(r"D:\FileRecv\ok.png")
