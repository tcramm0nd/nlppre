# nlppre
Preprocessing for NLP applicaitons. It could also definitely be used for non-nlp applications. Totally your call.Supports Pandas DataFrames, arrays and lists, as well as strings.

## Class: Corpus
`nlppre.Corpus(text, columns=None, url=False)`: an object that holds the original text, as well as any cleaned or tokenized versions
- **text:** the text you wish to process
- **columns:** if inputting a Pandas DataFrame, columns is a list or string of the columns to import from that DataFrame.
- **url:** if True, the `text` field will be instead treated as a URL leading to a .txt file for import.

### Class Methods
`nlppre.Corpus.clean(self, gutenburg=False, uncased=True, brackets=True, hyperlinks=True, punctuation=True, line_breaks=True,                     tabs=True, nums=True)` cleans the text, removing html, brackets, etc

`nlppre.Corpus.tokenize(self, preview=True)`: splits a  body of text into a list of words

## Class: NGram
`nlppre.NGram(corpus, n=2, length=10)`: takes in a corpus of text and creates a list of N-grams. N-grams are a count of how many times a word or sequence of words appears in a text. For instance, a unigram is how many times a single word appears, bigrams are a count of how many times a sequence of two words appears, and so on.
- **corpus:** a `nlppre.Corpus()` object
- **n:** the `n` in N-grams
- **length:** the length of the N-gram list to plot

### Class Methods

`nlppre.NGram.create(n=1, length=10)`: generates a list of ngrams
- **n**: ngram number (1 for unigrams, 2 for bigrams, and so on)
- **length:** length of the list of ngrams returned

`nlppre.NGram.plot(n=1, length=10, color=Blue)`: plots the ngram count using Seaborn
- **n**: ngram number (1 for unigrams, 2 for bigrams, and so on)
- **length:** length of the list of ngrams returned
- **color:** color range for the count plot
