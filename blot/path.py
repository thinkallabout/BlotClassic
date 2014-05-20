class path():
	def __init__(self, path):
		self.path = path

		self.images = path + '/images'
		self.posts = path + '/posts'
		self.templates = path + '/templates'
		self.includes = path + '/includes' # Additional files such as includes
