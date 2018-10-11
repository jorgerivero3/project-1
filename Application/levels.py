class Level:
	def __init__(self, day, prompts, effects):
		self.day = day
		self.prompts = prompts
		self.effects = effects
		self.progress = progress

all = {}

#monday a-c, tuesday d-e
mondays = ['a1','a2','a3','a4','a5','b5','a6','b6','c6','a7','a8','b8','a9']
tuesdays = ['d1','d2','d3','d4','d5','e5','d6','e6','d7','d8','e8''d9']

#a1
["It's 8AM and your alarm rings, what do you do?", "1. Get out of bed", "2. Snooze the alarm"]
[['-5s'], ['']] #effects
['a2','a3'] #next level(s)
#a2
["You head to class and take notes"]
[['-2s-10e']]
['a3']
#a3
["It's noon. You start getting hungry. What's for lunch?", "1. Ramen", "2. Don's", "3. CFA"]
[['+2e'],['+5e'],['+5e']]
['a4','a4','a4']
#a4
["Following lunch you're a good student and go to class. When class ends, you're left with some difficult decisions.", "1. Go to office hours", '2. Hang out with friends']
[[],[]]
['a5','b5']
#a5
["You went to office hours and now the professor knows your name and now you know what a polymer is."]
['+5s']
#a6
["You hung out with your friends and played mario party to your heart's content"]
['+10s']
