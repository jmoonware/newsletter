#
# newsletter.py
# 	Holiday newsletter generator
# 	Copyright (c) 2015 by John A. Moon
#	This code is provided "as is", without warranty of any kind
# 	Hint: Holiday drinks may improve interpretation of the output (optimal is about 3)
#	Usage: type 'python newsletter.py" at a command prompt (you know, that black window 
#	thingy in Windows under Start->Run->cmd) Presuming you already installed Python 
#	(you have, haven't you?)
#	

import random
import time
import PithyPhrases
import GrammarElements
import TransitionPhrases

# gets a random item in a list
# if unique is True, then it deletes the element from the list
def getRandom(items,unique):
	if len(items)>0:
		listIndex=random.randint(0,len(items)-1)
		returnItem = items[listIndex]
		if unique==True:
			del items[listIndex]
	else:
		returnItem="something"
	return(returnItem)

def addArticle(noun):
		if noun[0] in ['a','e','i','o','u','A','E','I','O','U']:
			return('an '+noun)
		else:
			return('a '+noun)
		
months=['January','March','June','August','October']

line=[]
line.append(getRandom(TransitionPhrases.greetings,True))
line.append('\n\n')
line.append('This year, we')  
line.append(getRandom(GrammarElements.verbs,True))
line.append(getRandom(GrammarElements.adverbs,True))
line.append(getRandom(GrammarElements.prepositions,True))
line.append(getRandom(GrammarElements.propernouns,True))
line.append(getRandom(GrammarElements.timeprepositions,True))
line.append(getRandom(months,True)+'.')
line.append('That really made us pause.')
line.append(getRandom(PithyPhrases.data,True))
line.append('\n\n')

line.append(getRandom(GrammarElements.timeprepositions,True).capitalize())
line.append(getRandom(months,True)+',')
line.append('we')
line.append(getRandom(GrammarElements.verbs,True))
line.append(getRandom(GrammarElements.adverbs,True))
line.append(getRandom(GrammarElements.placeprepositions,False))
line.append(getRandom(GrammarElements.places,True)+'.')
line.append(getRandom(PithyPhrases.data,True))
line.append('\n\n')

line.append('We also have some great news!')
line.append(getRandom(GrammarElements.names,True))
line.append(getRandom(GrammarElements.verbs,True))
line.append(addArticle(getRandom(GrammarElements.nouns,True)))
line.append(getRandom(GrammarElements.prepositions,False))
line.append(getRandom(GrammarElements.propernouns,True))
line.append(getRandom(GrammarElements.placeprepositions,False))
line.append(getRandom(GrammarElements.places,True))
line.append(getRandom(GrammarElements.timeprepositions,False))
line.append(getRandom(months,False)+'!')
line.append(getRandom(PithyPhrases.data,True))
line.append(getRandom(GrammarElements.names,True))
line.append('was so jealous!')
line.append('\n\n')

line.append('This year we were also fortunate that the')
line.append(getRandom(GrammarElements.adjectives,True))
line.append(getRandom(GrammarElements.nouns,True))
line.append(getRandom(GrammarElements.verbs,True))
line.append(getRandom(GrammarElements.adverbs,True))
line.append(getRandom(GrammarElements.prepositions,False))
line.append(getRandom(GrammarElements.propernouns,True)+'.')
line.append(getRandom(PithyPhrases.data,True))
line.append('\n\n')

line.append(getRandom(TransitionPhrases.wrapups,True))
line.append(getRandom(PithyPhrases.data,True))
line.append(getRandom(TransitionPhrases.wrapups,True))
line.append('\n\n')

line.append(getRandom(TransitionPhrases.goodbyes,True))
line.append('\n\n')

with open('newsletter'+str(time.time())+'.txt','w+') as newsFile:
	newsFile.write(' '.join(line))

print(' '.join(line))
