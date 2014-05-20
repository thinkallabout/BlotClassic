class path():
	def __init__(self, path):
		""" Set Blot working directory """
		self.path = path

		# Default dirs
		self.images = path + '/images'
		self.posts = path + '/posts'
		self.templates = path + '/templates'
