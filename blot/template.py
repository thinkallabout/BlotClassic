import os, sys

def get(folder):
	template_list = {}
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
		split_text = os.path.splitext(template)[0]
		template_list[split_text] = template

	return template_list
