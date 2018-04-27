# from distutils.core import setup
from setuptools import setup

setup(
  name = 'cebstemmer',
  packages = ['cebstemmer'],
  version = '1.3',
  description = "A Cebuano Stemmer based on Krovetz Algorithm",
  author = 'Arjemariel Requina',
  author_email = 'rjrequina@gmail.com',
  url = 'https://github.com/ajrequina/Cebuano-Stemmer',
  download_url = 'https://github.com/ajrequina/Cebuano-Stemmer/archive/1.0.tar.gz',
  keywords = ['stemmer', 'cebuano-stemmer'],
  classifiers = [],
  data_files=[
  	('data', [
  		'cebstemmer/data/PREF.txt', 
  		'cebstemmer/data/SUFF.txt',
  	])
  ],
  install_requires=['cebdict']
)