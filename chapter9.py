dictionaryName = {'item1': 1, 'item2':2, 'item3':3}

print dictionaryName['item1']


epicProgrammerDict = {'Tim Berners-Lee': 'tbl@gmail.com', 'Guido van Rossum': 'gvr@gmail.com', 'Linus Torvalds': 'lt@gmail.com',}
print epicProgrammerDict

print epicProgrammerDict['Tim Berners-Lee']


epicProgrammerDict['Tim Berners-Lee'] = 'tim@gmail.com'
print 'New email for tim: ' + epicProgrammerDict['Tim Berners-Lee']

epicProgrammerDict['Larry Page'] = 'lp@gmail.com'

print epicProgrammerDict

epicProgrammerDict['Sergey Brin'] = 'sb@gmail.com'

epicProgrammerDict['Me'] = 'me@gmail.com'

print epicProgrammerDict

del epicProgrammerDict['Sergey Brin']

print epicProgrammerDict

del epicProgrammerDict['Me']

print epicProgrammerDict


