from distutils.core import setup


setup(
  name = 'cebstemmer',
  packages = ['cebstemmer'],
  version = '1.0',
  description = "A Cebuano Stemmer based on Krovetz Algorithm",
  author = 'Arjemariel Requina',
  author_email = 'rjrequina@gmail.com',
  url = 'https://github.com/ajrequina/Cebuano-Stemmer',
  download_url = 'https://github.com/ajrequina/Cebuano-Stemmer/archive/1.0.tar.gz',
  keywords = ['stemmer', 'cebuano-stemmer'],
  classifiers = [],
  data_files=[
  	('data', ['cebdict/data/cebposdict.txt']),
  	('data/function_words', [
  		'cebdict/data/function_words/CONJ.txt', 
  		'cebdict/data/function_words/DET.txt',
  		'cebdict/data/function_words/PART.txt',
  		'cebdict/data/function_words/PRON.txt'
  	])
  ]
)