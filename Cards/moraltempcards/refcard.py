import time
 
def refCard():
	x = {"time": time.asctime(), "context": raw_input("What is the context?: "),
	"temp": input("What is the moral temperature?: ")}
	return x
 
def makeCard():
	x = []
	x.append(refCard())
	return x
 
def updateCard():
	x.append(makeCard())
	return x
 
# x = makeCard()
# x = updateCard()
 
"""
x = makeCard()
What is the context?: At home.
What is the moral temperature?: 29
>>> x
[{'temp': 29, 'context': 'At home.', 'time': 'Tue Feb 11 00:49:11 2014'}]

x = [refCard()]
What is the context?: at home
What is the moral temperature?: 46

print x
[{'temp': 46, 'context': 'at home', 'time': 'Wed Mar 19 10:52:02 2014'}]
def updateCard():
x.append(refCard())
return x

x = updateCard()
What is the context?: nothing
What is the moral temperature?: 45
print x
[{'temp': 46, 'context': 'at home', 'time': 'Wed Mar 19 10:52:02 2014'},
{'temp': 45, 'context': 'nothing', 'time': 'Wed Mar 19 10:53:00 2014'}]
 
"""
