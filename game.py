# Characters 
class Player():

	def __init__(self, name):
		self.name = name

		self.health = 100
		self.death = False
		self.progress = []

	def hurt(self, damage):
		self.health -= damage

		if self.heath <= 0: 
			self.death = True
			return death

	def save_progress(self, current):
		self.progress.append(current)

def main():
	print("UT Oregon Trail!")
	print("1:) New Game")
	print("2:) Continue Game")
	option = input("-->")
	if option == "1":
		start()
	else:
		#Currently does nothing. Need to store the player with a login in the db. 
		main()

def start():
	print("What is your name?")
	name = input("-->")
	player = Player(name)
	player.save_progress(start)
	print("In %s's dormroom." % (player.name))
	print("1:) Get Up")
	print("2:) Sleep")
	option = ''
	while option not in ["1", "2"]:
		option = input("-->")
	if option == "1":
		player.save_progress(get_ready)
		get_ready(player)
	else:
		game_over(player)

def get_ready(player):
	print("You are getting ready for the day. You should really go to class but you don't feel like going today.")
	print("1:) Go to class.")
	print("2:) Skip class")
	option = ''
	while option not in ["1", "2"]:
		option = input("-->")
	if option == "1":
		print("Off to class!")
		#Call in_class functinon
	else:
		print("Looks like %s's day off" % (player.name))
		#Calls lunch function


def game_over(player):

	print("Game Over")
	print("1:) Continue")
	print("2:) Start Over")
	option = '' 
	while option not in ["1", "2"]:
		option = input("-->")
	if option == "1":
		player.progress[-1]()
	else: 
		start()

main()

