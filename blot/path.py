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

import os

class path():
	def make_dirs(self):
		# Create folder structure
		os.mkdir(self.path)
		os.mkdir(os.path.join(self.path, 'static'))
		os.mkdir(os.path.join(self.path, 'posts'))
		os.mkdir(os.path.join(self.path, 'templates'))
		os.mkdir(self.conf.output)

	def __init__(self, path):
		""" Set Blot working directory """
		self.path = path

		# Default dirs
		self.static = os.path.join(path, 'static')
		self.posts = os.path.join(path, 'posts')
		self.templates = os.path.join(path, 'templates')
