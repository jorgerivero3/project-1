class Level:
	def __init__(self, level):
		self.day = DAYS[level[0][0]]
		self.story = level[1][0]
		self.prompts = level[1][1:]
		self.effects = level[2]
		self.nextLevel = level[3]
		self.image = level[4]

	def get_next_level(self, choice):
		return self.nextLevel[choice]

	def num_choices(self):
		return len(self.prompts)



master = {}


DAYS = {"a": "Thursday", "b": "Thursday", "c": "Thursday", "d":"Friday", "z":"Friday", "e": "Saturday", "f": "Saturday", "g": "Saturday"}
#monday a-c, tuesday d-e
'''
mondays = [a1,a2,a3,a4,a5,b5,a6,b6,c6,a7,a8,b8,a9]
tuesdays = [d1,d2,d3,d4,d5,e5,d6,e6,d7,d8,e8,d9]
'''
#Scripts format: [0] == title, [1] == Story + choices, [2] == character effects, [3] == next levels

# DAY 1
a1 = ["a1", ["A sharp, loud sound awakens you from your peaceful slumber. 'Another day', you think to yourself. Laying in bed, it feels so comfy and nice. The bed might as well be cloud from heaven itself.\
You think about just drifting off...about the sweet release of sleep.", "1. No, it's time for class", "2. Hit that snooze button"], [['-5s'], ['-5g']], ['a2','a3'], 'sleepy.gif']

a2 = ["a2", ["After some self-motivational pep talks, you groggly stumble out of bed, shower, and get dressed for another day at the greatest university in the world. \
After praying, you get hit by a car crossing Guad (and once again making it across unscathed), you arrive to hel- I mean, class.", "1. Continue"], [['-2s','-10e']], ['a3'], 'guad.png']

a3 = ["a3", ["After enduring the most fun-filled, totally-not-boring class ever, you manage to make it and are free. Now comes one of the most important decisions of your life so far - lunch. \
Where and what will you eat on this fine day?", "1. Ramen", "2. Don's", "3. Jester Sushi", "4. Chic-Fil-A"], [['+2e'],['+5e'],['+5e'],['+7e']], ['a4','a4','a4', 'a4'], 'ques.png']

a4 = ["a4", ["Following lunch, since you're such a good student, you go to your other class today. However, as you sit down, the teacher says those dreaded \
words: 'Ok, class, put everything away and get out a pen or pencil.' Oh no, a quiz. You didn't study, you had no idea this was coming, and you're probably screwed. \
As the paper arrives in front of you, you see the first question: 'What is the volume of the sun when it was 1.2 million years old but only had 67.87 percent of its oxygen?", "1. What", '2. At least 3', '3. 765,543','4. Big'], [['-2e'],['-2e'],['-2e'],['-2e']], ['a5','a5', 'a5', 'a5'], 'in_class.png']

a5 = ["a5", ["Yeah, that sounds right. Next question: 'What happened on the Isle of Ceylon on June 15th, 1954?", 
"1. I'm so confused.", "2. George R. R. Martin started Game of Thrones", "3. OU continued to suck", "4. The sun went out"], [['-2e'],['-2e'],['-2e'],['-2e']], ['a6','a6', 'a6', 'a6'], 'in_class.png']

a6 = ["a6", ["'What are these questions', you think to yourself, as you move on to question #3: \
'What is considered the 3rd minor chord of the A flat minor-harmonic scale in bass clef?", "1. What's a clef", "2. Just let this end", "3. G sharp", "4. A natural"], [['-2e'],['-2e'],['-2e'],['-2e']], ['a7','a7', 'a7', 'a7'], 'in_class.png'] 

a7 = ["a7", ["2 more. Just answer 2 more questions and you're done. Next one: 'E'", "1. This isn't even a question", "2. What class am I even in", "3. Why am I doing this to myself", "4. E"], [['-2e'],['-2e'],['-2e'],['+4e']], ['a8','a8', 'a8', 'a8'], 'in_class.png']

a8 = ["a8", ["Finally, the last question. What could it possibly be? 'Hewwo, what is thee sum of 2 + 2 OwO?'", 
"1. I hate myself so much", "2. 4", "3. Rawr xD", "4. Thank you, quiz, for bringing back my depression"], [['-2e'],['-2e'],['+5e'],['-20e']], ['a9','a9', 'a9', 'a9'], 'in_class.png']

a9 = ["a9", ["You instantly regret going to class since you would have made a 0 anyway. After the quiz is done and all taken up, the teacher shows a small \
bit of mercy and releases class early. You think about how much more fun you could have had hanging out with friends. Whatever, you are a good student \
unlike them.", "1. Continue"], [['+10e']], ['b1'], 'in_class.png'] 

b1 = ['b1', ["While hanging out after class, one of your friends comes up to you and offers a most interesting proposal: there is a party tonight at a fraternity house, and you are invited. \
However, you aren't really sure if you want to go: sleep and quiet sounds nice. What should you do?", "1. I'm good, quiet is the place to be", "2. Hell yeah, let's party"], [['+5e'], ['+15e']], ['a10', 'b2'], 'guy.png']

a10 = ["a10", ["While a party sounds fun, you just want to be able to sleep soundly and relax peacefully that night. After some hours of studying, watching netflix, and eating dinner, you fall asleep peacefully \
(not) ready for the day tomorrow", "1. Continue to next day"], ['+40e'], ['d1'], 'sleepy.gif']


# Originally no character effects here, code not yet written to handle situations without effects. Temp added one. -Jorge
b2 = ['b2', ["After grueling through the whole day, you figure you deserve some time to have fun. After getting the address and start time, you head home and get ready. Now, what time should \
you arrive at the party?", "1. 10:00, right on start time", "2. 10:45, late enough but still early"], [], ["b3", "b4"], 'ques.png']

b3 = ["b3", ["You show up right at 10:00, in fact you are even a little early because you wish to show respect to your hosts. As you approach the gate, one of the confused members informs you \
that no one has arrived yet and it would probably be best to wait a little while.", "1. Should have just waited smh"], ["+1e"], ["b4"], 'ques.png']

b4 = ["b4", ["You show up at 10:45 to a modest queue outside the fence. After some waiting, you get to the front table. '$40 please'. 'What,' you think to youself, 'That's bullsh*t.' \
What will you do in this scenario?", "1. Whatever, I'm here, I'll just pay the $40.", "2. This is crap. I'm getting in no matter what!", "3. Price is WAAAYYY to high. I'm going home."], [["+5e"], ["-15e"], ["+5e"]], ["b5", "b6", "b7"], 'frat.png']

b5 = ["b5", ["After some grumbling, you cough up $40 cash, get a wristband, and walk in. Now that you're here, it is time for a night of (possible) debauchery", "1. Continue"], ["+5e"], ["b8"], 'frat.png']

b6 = ["b6", ["You're not gonna pay that fee, so you just start walking in. Unfortunately, after taking 2 steps, a bunch of frat bros surround you and start beating the crap out of you \
When they think you've had enough, they (literally) throw you out. Battered and bruised physically and mentally, you walk home and cry yourself to sleep", "1. Life sucks"], ["+1e"], ["d1"], 'fratgang.png']

b7 = ["b7", ["This party probably isn't even worth $20, let alone $40. You decide to head home and get a good night's sleep \
while reminiscing about how lonely you are", "1. Parties are for losers anyway"], ["+10e"], ["d1"], 'frat.png']

b8 = ["b8", ["As you walk in, you see some different poisons for you to sample. Do you start out light or go all the way?", 
"1. Let's just get a beer", "2. Punch sounds pretty good", "3. Give me a shot, let's go"], [['-2e'], ['-4e'], ['-6e']], ["b9", "b10", "c1"], 'cup.png']

b9 = ["b9", ["You start off slow with a beer (more like 3), and you enjoy the night. You talk to some friends you spot, dance a little, \
and have fun. It's time for another drink. What now?", "1. More beer!", "2. Let's get punch-y", "3. SHOTS!"], [["-2e"], ["-4e"], ["-6e"]], ["b10", "c1", "c2"], 'cup.png']

b10 = ["b10", ["You really start to feel the effects. The night becomes a little blurry, and your friends look fuzzy, \
but that's not slowing you down. You want more", "1. SHOTS", "2. SHOTS", "3. SHOTS"], [["-6e"], ["-6e"], ["-6e"]], ["c3", "c3", "c3"], 'cup.png']

c1 = ["c1", ["Oh man, you're really feeling it now. You start sseemingly teleporting around as you have no remebrance of moving. \
What was in that punch? Did I even drink punch? Oh well, might as well have shots", "1. No choices, take some shots"], ["-6e"], ["c2"], 'blurrycup.png']

c2 = ["c2", ["You are now gone. The night passes with lots of blackness. You remember throwing up in a corner, \
your friends ordering you an Uber, you riding (and throwing up again) in the uber before being kicked out, \
somehow making back to your apartment and your bed, before passing out into the night", "1. Worth it"], ["+20e"], ["d1"], 'blurrycup.png']


#DAY 2
d1 = ["d1", ["You wake up the next day feeling (perhaps surprisingly) well. Unfortunately you overslept your first class. Now that you're up, might as well get up, right?",
"1. Let's get this bread", "2. Not really feeling it"], [["+10e"], ["+15e"]], ["d2", "d3"], 'sleepy.gif']

d2 = ["d2", ["You get up, brush your teeth, get dressed, and head out for the day. What should you do at campus?", "1. Study", "2. Watch Netflix", "3. Homework"], 
[["+3e"], ["+4e"], ["+3e"]], ["d4", "d5", "d6"], 'ques.png']

d3 = ["d3", ["You decide to do nothing today, and pretty much laze around, binging The Office on Netflix and eating some snacks. Eventually you go to sleep later that night (yeah that's the end)", 
"1. Continue"], ["+10e"], ["g1"], 'netflix.png']

d4 = ["d4", ["You study for a little while, then get bored and watch Netflix instead. Why can't you ever focus?", "1. Continue"], ["+5e"], ["d5"], 'netflix.png']

d5 = ["d5", ["You start watching Netflix as watching it on campus just feels better. Maybe you like the feeling that \
because you're on campus, you're actually doing something productive, no matter what it is.", "1. Whatever, it's Friday"], ["+1e"], ["d7"], 'netflix.png']

d6 = ["d6", ["You start on your homework and after an hour, you finish it. You decide to celebrate and relax by watching Netflix", "1. Do all roads just lead to Netflix?"], 
["+6e"], ["d5"], 'netflix.png']

d7 = ["d7", ["After really doing nothing for a little bit, you remember that tomorrow is that day. Yes, that day", "1. Gameday", "2. Soup day", "3. Saturday"], [], [["z1"], ["d8"], ["d9"]], 'netflix.png']

d8 = ["d8", ["Wait, what? I don't even think that's a real day", "1. Saturday", "2. Gameday"], [], [["d9"], ["z1"]], 'netflix.png']

d9 = ["d9", ["Yes, it is a Saturday, but there's more too it than that", "1. Gameday", "2. Soup day"], [], [["z1"], ["d8"]], 'netflix.png']

z1 = ["z1", ["That's right, Gameday. That great tribal ritual that all Longhorn fans participate in. This one is special as UT will be playing A&M for the \
first time since 2011, when we won on that last second field goal (suck it, Aggies). You must prepare for this great event", "1. Need some new burnt orange apparel!", "2. Contact friends for tailgating"], 
[["+10e"], ["+15e"]], [["z2"], ["z3"]], 'ques.png']

z2 = ["z2", ["You head to the COOP to get some new burnt orange gear for gameday. After some perusing, you decide on the classic: polo shirt and shorts with some burnt orange dock shoes.", "1. It's time"], 
["+5e"], ["z3"], 'cow.png']

z3 = ["z3", ["You text the gm and start coming up with ideas. You're assigned the important task of getting the beer. What brand do you decide to buy?", "1. ShinerBock", "2. Corona", "3. Land Shark", "4. The one and only LoneStar"], 
[], [["z4"], ["z4"], ["z4"], ["z4"]], 'cow.png']

z4 = ["z4", ["Good choice, you think to yourself. You buy plenty of cases of it, and now you're ready for tomorrow. you head home locked in and ready to go. Those Aggies won't know what hit them.", "1. Hook 'em"], 
["+40e"], ["e4"], 'cow.png']

#DAY 3
e4 = ["e4", ["You head to the game ready to cheer your heart out and drink lots of yeasty beer. Your seats are for the student section but you see a few empty seats at the 50, do you sneak over?", "1. Yes, I am devious" , "2. No, I follow rules"], 
[], [["e5"],["f5"]], 'cow.png']

e5 = ["e5", ["Nice, got the best seats in the HOUSE. One problem though ... the seat owners just came back with nachos ...", "1. Greet them warmly" , "2. Act invisible"], 
[], [["e7"],["e8"]], 'cow.png']

e6 = ["e6", ["You remain in your seat knowing full well you will be standing the whole time ready to destroy your voice box", "1. Continue"], 
[], ["e9"], 'cow.png']

e8 = ["e8", ["The seat owners easily see you. Considering you don't have the power to actually turn invisible ... you ooze an embarrassed aura as you walk back to the student section", "1. Continue"], 
[], ["e9"], 'cow.png']

e7 = ["e7", ["The seat owners are slightly swhasty and welcome you kindly! They even share some nachos.", "1. Continue"], 
[], ["e9"], 'cow.png']

e9 = ["e9", ["The score of the game is raging back and forth until eventually the end of the game nears", "1. Continue"], 
[], ["f1"], 'cow.png']

f5 = ["f5", ["You stay in your seat and the ball is kicked off! The rivalry begins again!", "1. Continue"], 
[], ["e9"], 'cow.png']

f1 = ["f1", ["Texas is deep in the redzone and has one play to win the game. If you were the coach, what would you call?", "1. Blue 42?" , "2. Omaha?" , "3. Goal line fade to Johnson" , "4. QB Sneak"], 
[], [["f2"],["f2"],["f3"],["f4"]], 'cow.png']

f2 = ["f2", ["No worries, Coach Hermann has it under control. They perform a triple reverse qb throw with fries", "1. Continue"], 
[], ["f9"], 'cow.png']

f3 = ["f3", ["You and Coach Herman must be on the same wave length! The ball is snapped and Ehlinger launches the ball to the corner ... JOHNSON CATCHES IT!", "1. JFIOPEWHFIOPEWHIPFEJ!!!"], 
[], ["f9"], 'cow.png']

f4 = ["f4", ["Coach Herman must have you on the payroll because he called the exact same play! Ehlinger takes the snap and immediately lunges forward ... the ball breaks the plane!", "1. WHOOOOfdshjhfiuef!!!"], 
[], ["f9"], 'cow.png']

f9 = ["f9", ["TEXAS WINS THE FOOTBALL GAME! TEXAS WINS THE FOOTBALL GAME!", "1. Continue"], 
[], ["g1"], 'cow.png']

g1 = ["g1", ["The crowd erupts in cheer, you chest bump the ten closest people. You can finally say it:", "1. Texas Football is BACK!"], 
[], ["g2"], 'cow.png']

g2 = ["g2", ["The End. Thanks for playing", "1. No, thank you!"], 
[], ["gg"], 'cow.png']


levels = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, c1, c2,
d1, d2, d3, d4, d5, d6, d7, d8, d9, z1, z2, z3, z4, e4, e5, e6, e7, e8, e9, f1, f2, f3, f4, f9, g1, g2]


#Builds the Level objects with the scripts above
for script in levels:
	level = Level(script)
	master[script[0]] = level
