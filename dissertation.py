# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 16:44:55 2017

@author: Alireza.Farhidzadeh
Thanks to developers of wordcloud and nltk libraries.
"""


from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'mydissertation.txt')).read()
wordcount = Counter(text.split())

# read the mask / color image taken from the image
grad_coloring = np.array(Image.open(path.join(d, "Graduation-cap-blue.jpg")))
stopwords = set(STOPWORDS)
stopwords.update(('Figure', 'based', 'et', 'al','Therefore','used', 'using', 'show', 'shown' 'and','I','A','And','So','arnt','This','When','It','many','Many','so','cant','Yes','yes','No','no','These','these'))

filtered_words = [word for word in text.split() if word not in stopwords]
filterwordcount = Counter(filtered_words)
filterwordcount.most_common(1)

wc = WordCloud(background_color="white", max_words=1000, mask=grad_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)
# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(grad_coloring)

# show
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
wc.to_file("dissertation.png")
plt.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
wc.to_file("dissertation2.png")
plt.figure()
plt.imshow(grad_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()
