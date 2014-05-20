from blot import Blot
import os

root_dir = os.getcwd() + '/src'
scripts = root_dir + '/scripts'
site = Blot(root_dir)

site.path.images = root_dir + '/img'
site.path.posts = root_dir + '/posts'
site.path.templates = root_dir + '/templates'

site.conf.output = root_dir + '/bin'

if __name__ == '__main__':
	site.compile()
