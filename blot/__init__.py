""" Basic configuration settings for blot """

import os

from blot.path import path
from blot.conf import conf
from blot.env import create

default_path = os.getcwd() + '/blot'

class Blot():
	""" Configuration container """
	def compile():
		pass

	def __init__(self, base):
		# Path to working folder
		self.path = path(default_path)

		# Blot configuration
		self.conf = conf(False, self.path) # Container
		self.conf.output = self.path.path + '/bin' # Output path
		self.conf.env = env.create(self.conf, self.path)

		# Global site vars for Jinja2
		self.glob = {}
