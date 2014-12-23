# Made by Tavor Baharav 12/21/2014
# tavor@baharav.org

# Unjumble words:
# Usage

# >>> unjumble('ylniag')
# ['gainly', 'laying']

f = open('dictionary.txt', 'r')
totaldict= f.readlines()
totaldict = [elem[:-1] for elem in totaldict]


def permutations(myword):
	def helper(wordportion, words):
		if not wordportion:
			return words
		newwords=[]
		for elem in words:
			for i in range(len(elem)+1):
				newwords.append(elem[:i] + wordportion[0] + elem[i:])
		return helper(wordportion[1:], newwords)
	return helper(myword[1:], [myword[0]])

def badunjumble(inputword):
	possibilities= permutations(inputword)
	for elem in possibilities:
		if elem in totaldict:
			return elem
	return 'Error'

def startswith(strang, prefix):
	if not prefix:
		return True
	if not strang:
		return False
	return strang[0]== prefix[0] and startswith(strang[1:], prefix[1:])


def unjumble(myword):
	def helper(currentword, otherletters, mydict):
		if not mydict:
			return False
		updateddict = [elem for elem in mydict if startswith(elem, currentword)]
		if not otherletters:
			if currentword in mydict:
				return updateddict
			return False

		for i in range(len(otherletters)):
			trial = helper(currentword + otherletters[i], otherletters[:i] + otherletters[i+1:], updateddict)
			if trial:
				for elem in trial:
					solvedwords.append(elem)
					
	solvedwords=[]
	newdict = [elem for elem in totaldict if len(elem) == len(myword)]
	helper('', myword, newdict)
	originals=[]
	for elem in solvedwords:
		if elem not in originals:
			originals.append(elem)
	return originals

	

