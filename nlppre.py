import re
from _text_cleaning._clean_fns import cleaner
from _ngrams.ngrams import create, plot

class Corpus:
    def __init__(self, text, columns=None, url=False):
        self.text = text
        self.df = False

        if columns:
            self.text = text[columns].values.tolist()
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

    def clean(self, gutenburg=False, uncased=True, brackets=True,
              hyperlinks=True, punctuation=True, line_breaks=True, tabs=True,
              nums=True
              ):

        self.options = {'gutenburg': [gutenburg],
                   'uncased': [uncased],
                   'brackets': [brackets],
                   'hyperlinks': [hyperlinks],
                   'punctuation': [punctuation],
                   'line_breaks': [line_breaks],
                   'tabs': [tabs],
                   'nums': [nums]
                  }
        if self.df == True:
            # self.clean_text = self.text.apply(lambda x: self._clean(x))
            self.clean_text = []
            for item in self.text:
                self.clean_text.append(cleaner(item, self.options))
        else:
            self.clean_text = cleaner(self.text, self.options)
    def tokenize(self, preview=True):
        pattern = re.compile(r'\W+')

        self.tokenized = pattern.split(self.text)

        if preview:
            if preview > 0:
                print(self.tokenized[:preview])
            else:
                print(self.tokenized[:10])

class NGram:
    def __init__(self, corpus, n=2, length=10):
        self.n = n
        self.length = length
        self.corpus = corpus
        self.ngram = create(corpus)
        # return self.ngram

    def __len__(self):
        return len(self.n_gram)

    def __getitem__(self, item):
        '''Returns either the count if given a string, or the word and count of
        a position if given an int'''
        if type(item) is str:
            for gram in self.ngram:
                if gram[0] == item:
                    return gram
        elif type(item) is int:
            return self.ngram[item]

    def __str__(self):
        return self.ngram[:10]




        # return self.ngram
