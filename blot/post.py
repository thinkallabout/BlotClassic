import os

class Post():
	""" Blog post, page or something else """

	def __init__(self, blot):
		pass

def find_types(blot):
	folder = os.listdir(blot.path.path)
	dirs = ['images', 'templates', 'config.json']
	types = []

	# All paths except special
	for i in folder:
		if i in dirs:
			# Remove when found
			folder.remove(i)
		else:
			types.append(i)
	return types
