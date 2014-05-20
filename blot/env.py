from jinja2 import Environment, FileSystemLoader

def create(conf, path):
	""" Create a new Jinja2 env """
	loader = FileSystemLoader(path.templates)
	env = Environment(loader=loader)

	# Set blot.conf.env to Jinja env
	conf.env = env
