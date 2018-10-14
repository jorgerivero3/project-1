import unittest
from Application.models import User
import Application.levels
from Application.routes import get_level, doEffect


class functiontesting(unittest.TestCase):
	
	def test_levels(self):
		self.assertTrue(len(Application.levels.master != 0)) #non empty dictionary
	
	def test_effects(self): #testing function from routes
		current_user = User() #create object
		#initialize stats
		current_user.health = 100
		current_user.sanity = 100
		current_user.grades = 100
		#progress/choice
		index = 0
		current_user.progress = 'a1'
		pageDetails = get_level(current_user.progress)
		#function within routes
		eff = pageDetails.effects[index]
		doEffect(current_user, eff)
		self.assertEqual(current_user.sanity, 95) #effect specific to choice

	def test_update(self):
		current_user = User() #create object
		#progress/choice
		index = 0
		current_user.progress = 'a1'
		pageDetails = get_level(current_user.progress)
		#function within routes
		current_user.progress = pageDetails.get_next_level(index)
		self.assertEqual(current_user.progress, 'a2') #specific to choice

	# NEEDS TO TEST THE WRONG STUFF

	#def test_wrong_input

if __name__ == '__main__':
	unittest.main()
