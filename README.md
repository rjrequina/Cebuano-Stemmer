# Cebuano-Stemmer
Cebuano Stemmer based on Krovetz Algorithm

`Note: Only prefixes, suffixes, infixes, and reduplication is covered`

## Installation
* `pip install cebstemmer` or
* inside the folder run `python setup.py install`

## Requirements
* `cebdict>=2.1`

## Functions
* stem_word(word='', as_object=False)
   - Accepts a Cebuano word and returns the morphemes of the word
   - Default Output: List of morphemes
      ```
        [root, prefix, infix, suffix]
      ```
   - OPTION:
        as_object
          - When true, Word object is returned.
          
          ```
          class Word:
            def __init__(self, text=None):
                self.orig_text = text
                self.text = text.lower() if text is not None else text
                self.prefix = None
                self.infix = None
                self.suffix = None
                self.root = text.lower() if text is not None else text
                self.is_entry = False
          ```
   
## How to Use
```
from cebstemmer import stemmer

stemmer.stem_word('buangon')

Output: 
   ['buangon', None, None, on]

word = stemmer.stem_word('buangon', as_object=True)
print(word.root)
print(word.suffix)

Output:
  buang
  on
```

## Evaluation
![png-2](https://user-images.githubusercontent.com/24803247/39425959-649b0ba4-4cb0-11e8-94b5-b1aacd3174d6.PNG)

## References

* Krovetz, R. (1993). Viewing morphology as an inference process (pp. 191–202). ACM Press. https://doi.org/10.1145/160688.160718

