import os

class path():
	def __init__(self, path):
		""" Set Blot working directory """
		self.path = path
		if os.path.exists(self.path) != True:
			os.mkdir(self.path)

		# Default dirs
		self.images = path + os.path.join('images')
		self.posts = path + os.path.join('posts')
		self.templates = os.path.join('templates')
