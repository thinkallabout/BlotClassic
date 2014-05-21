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
	def __init__(self, path):
		""" Set Blot working directory """
		self.path = path
		if os.path.exists(self.path) != True:
			os.mkdir(self.path)

		# Default dirs
		self.images = os.path.join(path, 'images')
		self.posts = os.path.join(path, 'posts')
		self.templates = os.path.join(path, 'templates')
