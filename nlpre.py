import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

class NLPRE:
    def __init__(self, text, columns=None):
        self.df = False
        if columns:
            self.text = text[columns]
            self.df = True
        else:
            self.text = text

    def __len__(self):
        return len(self.text)

    def __getitem__(self, item):
        return self.text[item]


    def clean(self):

        if self.df == True:
            self.clean_text = self.text.apply(lambda x: self._clean(x))
        else:
            self.clean_text = self._clean(self.text)

    def _clean(self, text):
        """null_vals=True, cased=True, brackets=True, hyperlinks=True,
                punctuation=True, line_breaks=True, nums=True"""
        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\t', '', text)
        text = re.sub('\w*\d\w*', '', text)
        return text
## this doesnt need to be a function! I can apply this to the text object expternally
    def tokenize(self, text, tokenizer=None):
        tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
        return tokenizer.tokenize(text)

    def create_ngrams(self, n, length):
        # realizing that ideally you'd want to implement your own versions
        # of these dependencies, to make your function more robust

        vec = CountVectorizer(stop_words=stop_words,
                                ngram_range=(n,n)).fit(self.text)
        words = vec.transform(corpus)
        sum_words = words.sum(axis=0)
        word_freq = sorted([(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()],
                            key = lamnda x: x[1], reverse=True)

        return word_freq[:length]
