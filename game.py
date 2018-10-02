# Characters 
class Player():

	def __init__(self, pronoun):
		self.name = name

		self.health = 100
		self.death = False

	def hurt(self, damage):
		self.health -= damage

		if self.heath <= 0: 
			self.death = True
			return death

def main():
	print("UT Oregon Trail!")
	print("1:) Start")
	print("2:) Exit")
	option = input("-->")
	if option == 1:
		start()
	else:
		main()

