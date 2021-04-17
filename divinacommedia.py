import operator
from functools import reduce

def myMapLine(line):
	words = line.split(' ')
	words = map( lambda w: w.strip(), words )
	words = filter( lambda w: len(w) > 3, words )
	return list(words)

def myExtend(x, y):
	x.extend(y)
	return x

def addWordToOccurences(occurrences, word):
	occurrences[word] = occurrences.get(word, 0) + 1
	return occurrences

with open('dante.txt') as file:
	words = map( myMapLine , file )
	words = reduce( myExtend, words, [] )
	occurrences = reduce( addWordToOccurences, words, {} )
	occurrences = sorted( occurrences.items(), key=operator.itemgetter(1), reverse=True )

	print(occurrences[:20])
