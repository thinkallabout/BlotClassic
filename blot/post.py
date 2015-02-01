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
import markdown
import json

class Post():
	""" Blog post, page or something else """		
	def __init__(self, blot, path):
		self.path = path
		self.config = json.load(open(
			os.path.join(blot.path.path, blot.path.posts, self.path, 'post.json')))
		self.main = markdown.markdown(open(os.path.join(
			blot.path.posts, self.path, self.config['_compile']['main'])).read())

		# Template
		for i in blot.templates:
			if i.name == self.config['_compile']['template']:
				self.template = i.content
				break

		# Post URL (relative to "/")
		self.url = self.config['_compile']['url']
		self.timestamp = self.config['_compile']['timestamp']

                self.is_post = True

		# Template variables
		self.var = {}
		self.var['main'] = self.main
		for var in self.config['_post']:
			self.var[var] = self.config['_post'][var]
