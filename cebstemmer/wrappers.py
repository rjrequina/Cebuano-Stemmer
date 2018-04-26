'''
Wrapper for each word with its properties

Properties:
    root_tags = tags of the word from the dictionary
    derived_tags = tags of the word from lexical rules
    is_close = boolean to check if the current word is a function word
    pos_tags = tag/s of the word
    text = the word itself (string)
    prefix = prefix of the word
    infix = infix of the word
    suffix = suffix of the word
    root = root of the word
    is_entry = boolean to check if the current is a dictionary entry
'''
class Word:
    def __init__(self, text=None):
        self.pos_tags = []
        self.root_tags = []
        self.derived_tags = []
        self.is_close = False
        self.orig_text = text
        self.text = text.lower() if text is not None else text
        self.prefix = None
        self.infix = None
        self.suffix = None
        self.root = text.lower() if text is not None else text
        self.is_entry = False


    def to_lower():
        if self.text:
            return self.text.lower()

        return self.text

    def __str__(self):
        return self.orig_text.encode('utf-8') + '/' + str(','.join(self.pos_tags))

    def print_stem_results(self):
        pref = self.prefix if self.prefix else '-'
        inf = self.infix if self.infix else '-'
        suff = self.suffix if self.suffix else '-'

        text = self.text + ':[(' + str(self.root) +  '), {' + pref + ',' + inf + ',' + suff + '}]'
        return text