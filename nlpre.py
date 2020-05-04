import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class Corpus:
    def __init__(self, text, columns=None, url=False):
        self.text = text
        self.df = False
        
        if columns:
            self.text = text[columns]
            self.df = True

        if url == True:
            txt = []
            import urllib.request
            with urllib.request.urlopen(text) as f:
                for line in f:
                    txt.append(line.decode('utf-8'))
            self.text = ' '.join(txt)

    def __len__(self):
        return len(self.text)

    def __getitem__(self, item):
        if self.df == True:
            return self.text[item]
        return self.text.split()[item]

    def clean(self, gutenburg=False):
        self.gutenburg = gutenburg

        if self.df == True:
            self.clean_text = self.text.apply(lambda x: self._clean(x))
        else:
            self.clean_text = self._clean(self.text)

    def _clean(self, text):
        """null_vals=True, cased=True, brackets=True, hyperlinks=True,
                punctuation=True, line_breaks=True, nums=True"""

        text = str(text).lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', ' ', text)
        text = re.sub('\t', ' ', text)
        text = re.sub('\w*\d\w*', '', text)
        return text

    def de_gutenburg(self):
        text = self.text.split()
        idx = []
        for i, w in enumerate(text):
            if w =='***' and len(idx) < 3:
                idx.append(i)
        start_idx = idx[1] + 1
        end_idx = idx[2]
        text = text[start_idx:end_idx]
        self.text = ' '.join(text)

    def ngrams(self, n=1, length=10):

        if 'self.clean_text' not in locals():
            self.clean()

        if self.df == False:
            self.clean_text = [self.clean_text]


        vec = CountVectorizer(stop_words='english',
                                ngram_range=(n,n)).fit(self.clean_text)
        words = vec.transform(self.clean_text)
        sum_words = words.sum(axis=0)
        word_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
        word_freq =sorted(word_freq, key = lambda x: x[1], reverse=True)

        return word_freq[:length]

    def plot_ngram(self, n=1, length=10, color='Blue'):
        color = color + 's_d'
        if n == 1:
            n_gram = 'Unigrams'
        elif n == 2:
            n_gram = 'Bigrams'
        elif n == 3:
            n_gram = 'Trigrams'
        else:
            n_gram = str(n) + '-grams'

        df = pd.DataFrame()
        df = pd.DataFrame(self.ngrams(n, length), columns=[n_gram, 'Count'])
        plot = sns.barplot(x='Count', y = n_gram, data=df, palette= color)

        del df

        return plot
