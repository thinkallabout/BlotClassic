""" Basic configuration settings for blot """

import os

from blot.path import path
from blot.conf import conf
from blot.env import create
from blot.template import get

default_path = os.path.join(os.getcwd(), 'website')

class Blot():
	""" Configuration container """
	def compile(self):
		pass

	def __init__(self, base=default_path):
		# Path to working folder
		self.path = path(base)

		# Blot configuration
		self.conf = conf(False, self.path) # Container
		self.conf.output = os.path.join(self.path.path, 'bin') # Output path
		self.conf.env = env.create(self.conf, self.path)

		# Global site vars for Jinja2
		self.glob = {}

		# Dictionary with templates
		self.templates = template.get(
					self.path.templates)
