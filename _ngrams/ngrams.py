from sklearn.feature_extraction.text import CountVectorizer
import seaborn as sns
import matplotlib.pyplot as plt

def create(corpus, n=1, length=10):

    corpus.clean()
    text = [corpus.clean_text]

    vec = CountVectorizer(stop_words='english',
                            ngram_range=(n,n)).fit(text)
    words = vec.transform(text)
    sum_words = words.sum(axis=0)
    word_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    word_freq =sorted(word_freq, key = lambda x: x[1], reverse=True)

    return word_freq[:length]

def plot(self, n=1, length=10, color='Blue'):
    color = color + 's_d'
    if n == 1:
        n_gram = 'Unigrams'
    elif n == 2:
        n_gram = 'Bigrams'
    elif n == 3:
        n_gram = 'Trigrams'
    else:
        n_gram = str(n) + '-grams'

    words = []
    count = []
    for item in self.ngrams(n, length):
        words.append(item[0])
        count.append(item[1])
    plot = sns.barplot(x=count, y=words, palette=color)



    return plot
