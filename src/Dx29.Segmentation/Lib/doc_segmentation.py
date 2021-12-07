from nltk.data import load

class DocSegmentation():
    def __init__(self, lang):
        self.lang = lang.lower()
        self.language = 'english'
        if lang == 'es':
            self.language = 'spanish'
        self.tokenizer = load("tokenizers/punkt/{0}.pickle".format(self.language))

    def process(self, txt):
        segs = []
        n = 0
        sents = self.tokenizer.tokenize(txt)
        for sent in sents:
            n += 1
            item = { 'id': F'S{n:04}', 'source': sent }
            segs.append(item)
        return { 'language_source': self.lang, 'segments': segs }
