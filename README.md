# nlpre
Preprocessing for NLP applicaitons. It could also definitely be used for non-nlp applications. Totally your call.Supports pandas dataframs, arrays and lists, as well as strings.

## Objects
`Corpus`: an object that holds the original text, as well as any cleaned or tokenized versions

## Methods
`nlpre.Corpus.clean()`: cleans the text, removing html, brackets, etc

`nlpre.Corpus.de_gutenburg()`: strips the header and footer from Project Gutenburg txt files

`nlpre.Corpus.ngrams(n=1, length=10)`: generates a list of ngrams
- **n**: ngram number (1 for unigrams, 2 for bigrams, and so on)
- **length:** length of the list of ngrams returned

`nlpre.Corpus.plot_ngrams(n=1, length=10, color=Blue)`: plots the ngram count using Seaborn
- **n**: ngram number (1 for unigrams, 2 for bigrams, and so on)
- **length:** length of the list of ngrams returned
- **color:** color range for the count plot
