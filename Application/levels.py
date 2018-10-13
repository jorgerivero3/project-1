class Level:
	def __init__(self, level):
		self.day = DAYS[level[0][0]]
		self.story = level[1][0]
		self.prompts = level[1][1:]
		self.effects = level[2]
		self.nextLevel = level[3]

	def get_next_level(self, choice):
		return self.nextLevel[choice - 1]

	def num_choices(self):
		return len(self.prompts)

master = {}


DAYS = {"a": "Monday", "b": "Monday", "c": "Monday", "d":"Tuesday", "e": "Tuesday", "f": "Tuesday"}
#monday a-c, tuesday d-e
'''
mondays = [a1,a2,a3,a4,a5,b5,a6,b6,c6,a7,a8,b8,a9]
tuesdays = [d1,d2,d3,d4,d5,e5,d6,e6,d7,d8,e8,d9]
'''
#Scripts format: [0] == title, [1] == Story + choices, [2] == character effects, [3] == next levels

a1 = ["a1", ["A sharp, loud sound awakens you from your peaceful slumber. 'Another day', you think to yourself. Laying in bed, it feels so comfy and nice. The bed might as well be cloud from heaven itself.\
You think about just drifting off...about the sweet release of sleep.", "1. No, it's time for class", "2. Hit that snooze button"], [['-5s'], ['']], ['a2','a3']]

a2 = ["a2", ["After some self-motivational pep talks, you groggly stumble out of bed, shower, and get dressed for another day at the greatest university in the world. \
After praying, you get hit by a car crossing Guad (and once again making it across unscathed), you arrive to hel- I mean, class.", "1. Continue"], [['-2s-10e']], ['a3']]

a3 = ["a3", ["After enduring the most fun-filled, totally-not-boring class ever, you manage to make it and are free. Now comes one of the most important decisions of your life so far - lunch. \
Where and what will you eat on this fine day?", "1. Ramen", "2. Don's", "3. CFA", "4. Chic-Fil-A"], [['+2e'],['+5e'],['+5e'],['+7e']], ['a4','a4','a4', 'a4']]

a4 = ["a4", ["Following lunch, since you're such a good student, you go to your other class today. However, as you sit down, the teacher says those dreaded \
words: 'Ok, class, put everything away and get out a pen or pencil.' Oh no, a quiz. You didn't study, you had no idea this was coming, and you're probably screwed. \
As the paper arrives in front of you, you see the first question: 'What is the volume of the sun when it was 1.2 million years old but only had 67.87 percent of its oxygen?", "1. What", '2. At least 3', '3. 765,543','4. Big'], [['-2e'],['-2e'],['-2e'],['-2e']], ['a5','a5', 'a5', 'a5']]

a5 = ["a5", ["Yeah, that sounds right. Next question: 'What happened on the Isle of Ceylon on June 15th, 1954?", 
"1. I'm so confused.", "2. George R. R. Martin started Game of Thrones", "3. OU continued to suck" "4. The sun went out"], [['-2e'],['-2e'],['-2e'],['-2e']], ['a6','a6', 'a6', 'a6']]

a6 = ["a6", ["'What are these questions', you think to yourself, as you move on to question #3: \
'What is considered the 3rd minor chord of the A flat minor-harmonic scale in bass clef?", "1. What's a clef", "2. Just let this end", "3. G sharp", "4. A natural"], [['-2e'],['-2e'],['-2e'],['-2e']], ['a7','a7', 'a7', 'a7']] 

a7 = ["a7", ["2 more. Just answer 2 more questions and you're done. Next one: 'E'", "1. This isn't even a question", "2. What class am I even in", "3. Why am I doing this to myself", "4. E"], [['-2e'],['-2e'],['-2e'],['+4e']], ['a8','a8', 'a8', 'a8']]

a8 = ["a8", ["Finally, the last question. What could it possibly be? 'Hewwo, what is thee sum of 2 + 2 OwO?'", 
"1. I hate myself so much", "2. 4", "3. Rawr xD", "4. I am now suicidal. Thank you, quiz, for bringing back my depression"], [['-2e'],['-2e'],['+5e'],['-20e']], ['a9','a9', 'a9', 'a9']]

a9 = ["a9", ["You instantly regret going to class since you would have made a 0 anyway. After the quiz is done and all taken up, the teacher shows a small \
bit of mercy and releases class early. You think about how much more fun you could have had hanging out with friends. Whatever, you are a good student \
unlike them.", "1. Continue"], [['+10e']], ['a5']] 

levelNames = [a1, a2, a3, a4, a5, a6, a7, a8, a9]

#Builds the Level objects with the scripts above
def compileLevels(levelNames):
	temp = {}
	for script in levelNames:
		level = Level(script)
		temp[script[0]] = level
	return temp

master = compileLevels(levelNames)
