from copy import deepcopy
import string
import time

from cebdict import dictionary

import sys

'''
Returns contents of a file
Can specify start and end of contents in reading a file
'''
def read_file(name=None, start=None, end=None, strip=False, dict_format=False, decode=False):
    if name:
        
        name = sys.prefix + '/' + name
        # sys.path.insert(0, name)

        f = open(name, "r")
        contents = []
        dictionary = {}
        for line in f:
            if strip:
                line = line.strip()
            splitted = line.split(" ")
            dictionary[splitted[0]] = splitted[1:]
            if decode:
                line = line.decode('utf-8')
            contents.append(line)

        f.close()
        if start is not None:
            contents = contents[start:]

        if dict_format:
            return dictionary

        return contents
    return None


'''
Fetch prefixes
'''
def prefixes():
    return read_file('data/PREF.txt', strip=True)

'''
Fetch suffixes
'''
def suffixes():
    return read_file('data/SUFF.txt', strip=True)

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



prefs = prefixes()
suffs = suffixes()

'''
Given a word, stems the word and returns the root and affixes of the word
'''
def stem_word(word=None, as_object=False):
    if word:
        processes = [
            [],
            ['inf'],
            ['pref'],
            ['inf', 'pref'],
            ['redup'],
            ['inf', 'redup'],
            ['pref', 'redup'],
            ['inf', 'pref', 'redup'],
            ['suff'],
            ['inf', 'suff'],
            ['pref', 'suff'],
            ['inf', 'pref', 'suff'],
            ['redup', 'suff'],
            ['inf', 'redup', 'suff'],
            ['pref', 'redup', 'suff'],
            ['inf', 'pref', 'suff', 'redup']

        ]

        stem = Word(text=word)
        temp_stem = deepcopy(stem)
        for process in processes:
            temp_stem = remove_affixes(process=process, stem=temp_stem)
            temp_stem = remove_inflections(process=process, stem=temp_stem)
            temp_stem = lookup(stem=temp_stem)
            temp_stem = affix_lookup(stem=temp_stem)

            if temp_stem.is_entry or len(process) == 4:
                stem = temp_stem
                break

            temp_stem = deepcopy(stem)
        
        if as_object:
            return stem

        return [stem.root, stem.prefix, stem.infix, stem.suffix]
    return None

'''
Remove affixes
'''
def remove_affixes(process=[], stem=None):
    if not stem:
        return stem

    if 'pref' in process:
        stem = strip_prefix(stem=stem)

    if 'suff' in process:
        stem = strip_suffix(stem=stem)

    if 'inf' in process:
        stem = strip_infix(stem=stem)

    return stem

'''
Remove inflections
'''
def remove_inflections(process=[], stem=None):
    if 'redup' in process:
        stem = remove_duplication(stem=stem)

    return stem

'''
Helper function that will strip prefixes from the word
'''
def strip_prefix(stem=None):
    if not stem:
        return stem

    longest_prefix = None
    word = stem.root
    word = ''.join([i for i in word if i.isalpha()])

    for prefix in prefs:
        if word.startswith(prefix):
            if not longest_prefix:
                longest_prefix = prefix
            else:
                temp_stem = deepcopy(stem)
                temp_stem.root = string.replace(word, prefix, '')
                temp_stem = lookup(stem=temp_stem)
                if temp_stem.is_entry:
                    longest_prefix = prefix
                    break

    if longest_prefix:
        stem.root = string.replace(word, longest_prefix, '')
        stem.prefix = longest_prefix
    return stem

'''
Helper function that will strip suffixes from the word
'''
def strip_suffix(stem=None):
    if not stem:
        return stem

    word = stem.root
    word = ''.join([i for i in word if i.isalpha()])
    longest_suffix = None

    for suffix in suffixes():
        if word.endswith(suffix):
            if not longest_suffix:
                longest_suffix = suffix
            else:

                temp_stem = deepcopy(stem)
                temp_stem.root = word[0:word.rfind(suffix)]
                temp_stem = lookup(stem=temp_stem)
                if temp_stem.is_entry:
                    longest_suffix = suffix
                    break

    if longest_suffix:
        stem.root = word[0:word.rfind(longest_suffix)]
        stem.suffix = longest_suffix
    return stem

'''
Strip infixes -um- and -in-
'''
def strip_infix(stem=None):
    if not stem:
        return stem

    word = stem.root
    if word.find('um') > 0 or word.find('in') > 0:
        if word.find('in'):
            stem.root = word.replace('in', '')
            stem.infix = 'in'
        elif word.find('um'):
            stem.root = word.replace('um', '')
            stem.infix = 'um'

    return stem

'''
Removes duplication of a word
'''
def remove_duplication(stem=None):
    if not stem:
        return stem

    longest_string = None
    size = 1
    stem.root = ''.join([i for i in stem.root if i.isalpha()])
    for i in range(1, len(stem.root)):
        str_a = stem.root[0:i]
        str_b = stem.root[i: i + size]

        if str_a == str_b:
            longest_string = str_a
        size += 1

    if longest_string:
        if len(longest_string) > 2:
            stem.root = longest_string

    return stem

'''
Checks if the root exists in dictionary
If does not exists, sets root, prefix and suffix to None
as an indicator
'''
def lookup(stem=None):
    entry = stem.root.lower().replace('o', 'u')
    entry = entry.replace('e', 'i')

    stem.is_entry = dictionary.is_entry(entry) or dictionary.is_entry(stem.root)
    return stem

'''
Checks if the root is an affix
'''
def affix_lookup(stem=None):
    if stem.root in prefs or stem.root in suffs:
        stem.is_entry = True
        return stem

    return stem


if __name__ == "__main__":
    pass
