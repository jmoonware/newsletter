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

def getRandom(items):
	return(items[random.randint(0,len(items)-1)])

def addArticle(noun):
		if noun[0] in ['a','e','i','o','u','A','E','I','O','U']:
			return('an '+noun)
		else:
			return('a '+noun)
		
months=['January','March','June','August','October']

line=[]
line.append(getRandom(TransitionPhrases.greetings))
line.append('\n\n')
line.append('This year, we')  
line.append(getRandom(GrammarElements.verbs))
line.append(getRandom(GrammarElements.adverbs))
line.append(getRandom(GrammarElements.prepositions))
line.append(getRandom(GrammarElements.propernouns))
line.append(getRandom(GrammarElements.timeprepositions))
line.append(getRandom(months)+'.')
line.append('That really made us pause.')
line.append(getRandom(PithyPhrases.data))
line.append('\n\n')

line.append(getRandom(GrammarElements.timeprepositions).capitalize())
line.append(getRandom(months)+',')
line.append('we')
line.append(getRandom(GrammarElements.verbs))
line.append(getRandom(GrammarElements.adverbs))
line.append(getRandom(GrammarElements.placeprepositions))
line.append(getRandom(GrammarElements.places)+'.')
line.append(getRandom(PithyPhrases.data))
line.append('\n\n')

line.append('We also have some great news!')
line.append(getRandom(GrammarElements.names))
line.append(getRandom(GrammarElements.verbs))
line.append(addArticle(getRandom(GrammarElements.nouns)))
line.append(getRandom(GrammarElements.prepositions))
line.append(getRandom(GrammarElements.propernouns))
line.append(getRandom(GrammarElements.placeprepositions))
line.append(getRandom(GrammarElements.places))
line.append(getRandom(GrammarElements.timeprepositions))
line.append(getRandom(months)+'!')
line.append(getRandom(PithyPhrases.data))
line.append(getRandom(GrammarElements.names))
line.append('was so jealous!')
line.append('\n\n')

line.append('This year we were also fortunate that the')
line.append(getRandom(GrammarElements.adjectives))
line.append(getRandom(GrammarElements.nouns))
line.append(getRandom(GrammarElements.verbs))
line.append(getRandom(GrammarElements.adverbs))
line.append(getRandom(GrammarElements.prepositions))
line.append(getRandom(GrammarElements.propernouns)+'.')
line.append(getRandom(PithyPhrases.data))
line.append('\n\n')

line.append(getRandom(TransitionPhrases.wrapups))
line.append(getRandom(PithyPhrases.data))
line.append(getRandom(TransitionPhrases.wrapups))
line.append('\n\n')

line.append(getRandom(TransitionPhrases.goodbyes))
line.append('\n\n')

with open('newsletter'+str(time.time())+'.txt','w+') as newsFile:
	newsFile.write(' '.join(line))

print(' '.join(line))
