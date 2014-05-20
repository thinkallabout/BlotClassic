import os

class path():
	def __init__(self, path):
		""" Set Blot working directory """
		self.path = path
		if os.path.exists(self.path) != True:
			os.mkdir(self.path)

		# Default dirs
		self.images = os.path.join(path, 'images')
		self.posts = os.path.join(path, 'posts')
		self.templates = os.path.join(path, 'templates')
