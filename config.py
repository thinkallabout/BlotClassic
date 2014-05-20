from blot import Blot
import os

root_dir = os.getcwd() + '/src/img'
site = Blot(root_dir)

site.path.images = os.getcwd() + '/src/img'
site.path.posts = os.getcwd() + '/src/posts'
site.path.templates = os.getcwd() + '/src/templates'
site.path.include = os.getcwd() + '/src/include'

site.conf.output = os.getcwd() + '/bin'

site.conf.title = 'Site Title'
site.conf.description = 'Site Description'

#site.compile()
