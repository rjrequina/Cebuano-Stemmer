# Cebuano-Stemmer
Cebuano Stemmer based on Krovetz Algorithm


Number of entries |
--- |
16587 |


## Installation
* `pip install cebstemmer` or
* inside the folder run `python setup.py install`

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
Output: ['buangon', None, None, on]

word = stemmer.stem_word('buangon', as_object=True)
print(word.root)
print(word.suffix)

Output:
  buang
  on
```

## References

* Wolff, J. (1972). A dictionary of Cebuano Visayan (Vol. 1). Cornell University, 
       Southeast Asia Program and Linguistic Society of the Philippines.

* Wolff, J. (1972). A dictionary of Cebuano Visayan (Vol. 2). Cornell University,  
                  Southeast Asia Program and Linguistic Society of the Philippines.

