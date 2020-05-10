import re
import string

def cleaner(text, options):
    options['gutenburg'].append(de_gutenburg)
    options['uncased'].append(uncase)
    options['brackets'].append(rm_brackets)
    options['hyperlinks'].append(rm_links)
    options['punctuation'].append(rm_punct)
    options['line_breaks'].append(rm_breaks)
    options['tabs'].append(rm_tabs)
    options['nums'].append(rm_wrdnums)

    for key in options:
        if options[key][0]:
            text = options[key][1](text)
    return text

def uncase(text):
    return str(text).lower()

def rm_brackets(text):
    text =  re.sub('\[.*?\]', '', text)
    return re.sub('<.*?>+', '', text)

def rm_links(text):
    return re.sub('https?://\S+|www\.\S+', '', text)

def rm_punct(text):
    return re.sub('[%s]' % re.escape(string.punctuation), '', text)

def rm_breaks(text):
    return re.sub('\n', ' ', text)

def rm_tabs(text):
    return re.sub('\t', ' ', text)

def rm_wrdnums(text):
    return re.sub('\w*\d\w*', '', text)

def de_gutenburg(text):
    text = text.split()
    idx = []
    for i, w in enumerate(text):
        if w =='***' and len(idx) < 3:
            idx.append(i)
    start_idx = idx[1] + 1
    end_idx = idx[2]
    text = text[start_idx:end_idx]
    return ' '.join(text)
