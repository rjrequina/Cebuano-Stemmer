from utilities import read_file

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