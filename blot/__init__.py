# Copyright 2014 Cameron Brown

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Basic configuration settings for blot """

import os

from blot.path import path
from blot.conf import conf
from blot.env import create
from blot.template import get
from blot.post import Post, find_types
from blot.compiler import compiler

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
		# Posts & post types
		self.posts = post.Post(self)
		self.posts.types = post.find_types(self)
