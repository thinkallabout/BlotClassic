import os, sys

def get(folder):
	print folder
	try:
		templates = os.listdir(folder)
	except OSError:
		os.mkdir(folder)
		print ' * Creating folder "' + folder + '"'
		templates = os.listdir(folder)

	if len(templates) == 0:
		print ' * No templates in folder'
		sys.exit(0)

	for template in templates:
		print template
