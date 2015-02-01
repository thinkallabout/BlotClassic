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
import shutil
import errno
import operator

from blot.path import path
from blot.conf import conf
from blot.template import Template
from blot.post import Post
from blot.compiler import compile_post

default_path = os.path.join(os.getcwd(), 'website')

class Blot():
	""" Configuration container """
	def sort_posts(self):
		# Sort posts by timestamp
		self.posts.sort(
			key = operator.attrgetter('timestamp'))

		reversed_posts = []
		for post in reversed(self.posts):
			reversed_posts.append(post)
		self.posts = reversed_posts

	def compile(self):
		print ' * Compiling site'
		try:
			path.make_dirs(self.path)
		except OSError:
			pass

		self.sort_posts()

		# Create posts
		for post in self.posts:
			compile_post(self, post, post.var)

		# Copy static folder
		for item in os.listdir(self.path.static):
			src = os.path.join(self.path.static, item)
			dest = os.path.join(self.conf.output, item)
		if os.path.isdir(src):
			shutil.copytree(src, dest, False, None)
		else:
			shutil.copy2(src, dest)

	def __init__(self, base=default_path):
		# Path to working folder
		self.path = path(base)

		# Blot configuration
		self.conf = conf(self.path, self) # Container
		self.conf.output = os.path.join(self.path.path, 'bin') # Output path

		# Template container
		self.templates = []
		for template in os.listdir(self.path.templates):
			self.templates.append(Template(self, template))

		# Posts container
		self.posts = []
		for post in os.listdir(self.path.posts):
			self.posts.append(Post(self, post))

		# Global site vars for Jinja2
		self.glob = {"site": self}