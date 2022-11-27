import csv
import pymorphy2
from string import punctuation
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


morph = pymorphy2.MorphAnalyzer()
with open('train.csv', encoding='u8') as f:
    header, *data = csv.reader(f, delimiter='\t', quotechar='"')


def clean_text(text):
    text = [t.strip(punctuation) for t in text.split()]
    text = [morph.parse(t)[0].normal_form for t in text]
    text = [t for t in text if t not in stopwords.words('russian')]
    return text


all_star_list = [x[0] for x in douban_data]
for item in data[:1]:
    idx, mark, text = item
    print(clean_text(text))


# print(data[1])
