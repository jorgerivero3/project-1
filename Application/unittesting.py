import unittest
from Application.models import User
from Application import levels
from Application.routes import get_level, doEffect,


class functiontesting(unittest.TestCase):
 
 	current_user = User() #create object
 	#initialize stats
 	current_user.health = 100
 	current_user.sanity = 100
 	current_user.grades = 100

 	def test_levels():
		self.assertTrue(len(levels.master != 0)) #non empty dictionary

	#used for next 2 tests
	current_user.progress = 'a1'
	pageDetails = get_level(current_user.progress)

	def test_effects(pageDetails): #testing function from routes
		index = 0 #if user picked 1
		eff = pageDetails.effects[index]
		doEffect(eff)
		self.asserEqual(current_user.sanity, 95) #effect specific to choice

	def test_update(pageDetails):
		index = 0 #same index as before
		current_user.progress = pageDetails.get_next_level(index)
		self.asserEqual(current_user.progress, 'a2') #specific to choice

if __name__ == '__main__':
    unittest.main()
