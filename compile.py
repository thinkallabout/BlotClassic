from blot import Blot
import os

print ' * Starting website'

root_dir = os.getcwd() + '/src/'
site = Blot(root_dir)

site.path.images = root_dir + '/img/'
site.path.posts = root_dir + '/posts/'
site.path.templates = root_dir + '/templates/'

site.conf.output = root_dir + '/bin/'

site.compile()
