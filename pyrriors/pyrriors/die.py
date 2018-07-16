import random

class Die:
	"""docstring for Die"""
	def __init__(self, arg):
		super(Die, self).__init__()
		self.arg = arg


	def __init__(self, faces):
		self.faces = faces


	def roll(self):
		return random.randint(1,6)

	
	def __repr__():
		return 'A die'	
