#
# newsletter.py
# 	Holiday newsletter generator
# 	Copyright (c) 2015 by John A. Moon
#	This code is provided "as is", without warrant of any kind
# 	Usage tip: Holiday drinks may make the output more sensible
# 
import random

def getRandom(items):
	return(items[random.randint(0,len(items)-1)])
	
names = ['Todd','Chelsea','Mustafa','Chad','Dweezil']
verbs = ['captured','flew','achieved','violated','awarded','retired','paid','slew']
nouns = ['chicken','paramecium','pine nuts','Christmas','holiday','exotic travel','expensive college','fancy car','prestigious award']
properNouns=['Zorro','Tooth Fairy','Haliburton','Cheese Whiz']
pithyPhrases = [
'It is what it is.',
'Don\'t spit into the wind.',
'It\'s our family tradition.',
'We are so blessed.',
'During the holidays, we always take time to reflect upon the year gone by.',
'Have you ever seen a gladiator movie?']
months=['January','March','June','August','October']
greetings=['Greetings','Hello Friends','Yo','It was a dark and stormy night','Call me Ishmael']
wrapUps = ['Oh well, that\'s about it.','That\'s all for this year.','Drop us a line sometime.','Be well and do good work.','Don\'t be strangers.','See you in the funny papers!']
goodByes=['Until next year!','Talk to you soon!','Happy sounding words!']
prepositions=['until','about','around']

line=[getRandom(greetings)+':']
line.append('\n\n')
line.append('This year, we')  
line.append(getRandom(verbs))
line.append('with')
line.append(getRandom(properNouns)+'.')
line.append('That really made us think:')
line.append(getRandom(pithyPhrases))
line.append('\n\n')

line.append('In')
line.append(getRandom(months))
line.append('we all')
line.append(getRandom(verbs))
line.append(getRandom(prepositions))
line.append(getRandom(properNouns)+'.')
line.append(getRandom(pithyPhrases))
line.append('\n\n')

line.append('We also have some great news!')
line.append(getRandom(names))
line.append(getRandom(verbs))
line.append(getRandom(prepositions))
line.append(getRandom(properNouns))
line.append('in')
line.append(getRandom(months)+'!')
line.append(getRandom(pithyPhrases))
line.append(getRandom(names))
line.append('was so jealous!')
line.append('\n\n')

line.append(getRandom(pithyPhrases))
line.append('We are so lucky that the')
line.append(getRandom(nouns))
line.append(getRandom(verbs))
line.append(getRandom(properNouns))
line.append('\n\n')

line.append(getRandom(wrapUps))
line.append(getRandom(pithyPhrases))
line.append(getRandom(pithyPhrases))
line.append(getRandom(wrapUps))
line.append('\n\n')

line.append(getRandom(goodByes))
line.append('\n\n')

print(' '.join(line))
