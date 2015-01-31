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

def compile_post(blot, post, args):
	env = blot.conf.env
	try:
		os.mkdir(os.path.join(blot.conf.output, post.url))
	except OSError:
		pass
    
	html = open(os.path.join(blot.conf.output, post.url, 'index.html'), 'w')
	args['site'] = blot
	template = env.get_template(post.template)
	html.write(template.render(args))
	html.close()
