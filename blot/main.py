# Copyright (C) 2016 Cameron Brown
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys, os
import shutil
import yaml
from jinja2 import Environment, FileSystemLoader
import markdown2

ENVIRONMENT_PRODUCTION = "production"
ENVIRONMENT_DEVELOPMENT = "development"
ENVIRONMENT = ENVIRONMENT_DEVELOPMENT
VERBOSE = False

"""
Class which encapsulates site, post and asset configuration.
"""
class Config():
    def get_config(self):
        return self.config
        
    def get_path(self):
        return self.path

    def validate(self, config, path):
        raise NotImplementedError

    def __init__(self, path):
        if VERBOSE:
            print("info: Loading config.yaml from: " + path)
        with open(os.path.join(path, "config.yaml"), "r") as file:
            config = yaml.load(file)
            if config == None or (self.validate(config, path) == False):
                print("error: Failed to validate " + path)
                sys.exit(0)
            elif VERBOSE:
                print("info: Validated config.yaml in " + path + " sucessfully")
        self.config = config
        self.path = path
        
"""
Represents a single jinja2 template that can be injected with 
variables and the compiled into a final output.
"""
class Template():
    environment = None
    templates = {}
    
    @staticmethod
    def get_environment():
        return Template.environment
        
    @staticmethod
    def get_template(name):
        try:
            template = Template.templates[name]
        except KeyError:
            env = Template.get_environment()
            template = env.get_template(name)
            Template.templates[name] = template
        return template
        
    @staticmethod
    def set_template_path(template_path):
        if Template.environment == None:
            Template.environment = Environment(
                loader=FileSystemLoader(template_path),
                trim_blocks=True)
        return Template.environment
        
    def render(self, config):
        return self.template.render(config)

    def __init__(self, template_name):
        env = Template.get_environment()
        self.template = self.get_template(template_name)
        
"""
Base type of content in blot. Extend to create new types
of pages with different features. 
"""
class Content(Config):
    # Stores a dictionary with all pieces of content.
    content_items = {}
    
    # Absolute directory reference to content folder.
    content_path = None
    
    @staticmethod
    def get_content():
        return Content.content_items
        
    @staticmethod
    def add_content(content_path):
        content = Content(content_path)
        name = content.get_name()
        if name in Content.content_items:
            print("error: Content name is not unique in " + config_path)
            sys.exit(0)
        else:
            Content.content_items[name] = content
            print("info: found content: " + name)
            
    @staticmethod
    def set_content_path(content_path):
        Content.content_path = content_path
        
    @staticmethod
    def search(content_path):
        Content.set_content_path(content_path)
        for subdir, dirs, files in os.walk(content_path):
            for file in files:
                # If this is a config file, then add the directory
                # to the list of content, otherwise, continue.
                if file == "config.yaml":
                    name = os.path.basename(subdir)
                    Content.add_content(name)
            
    def validate(self, config, path):
        if "name" not in config:
            print("error: Name undefined in " + path)
            return False
        if "template" not in config:
            print("error: Template undefined in " + path)
            return False
        return True
        
    def render(self, site, output_path, environment):
        # Compile Markdown content into HTML.
        config = self.get_config()
        try:
            content = config["content"]
            content_path = os.path.abspath(os.path.join(self.get_path(), 
                config["content"]))
        except KeyError:
            content_path = None
        
        # Calculate assets relative path.
        content_output_path = os.path.abspath(os.path.join(output_path, config["name"]))
        assets_output_path = os.path.abspath(os.path.join(output_path, "assets"))
        assets_relative_path = os.path.relpath(assets_output_path, content_output_path)
        
        # Template variables.
        template_variables = {
            "environment": environment,
            "assets": assets_relative_path,
            "site": site,
            "content": config,
        }
            
        if content_path == None:
            print("info: Skipping Markdown compliation for " + self.name)
        else:
            # Render Markdown seperately from the main template to parse 
            # variables inside it.
            with open(content_path) as file:
                data = file.read()
                markdown = markdown2.markdown(data)
                markdown = Template.get_environment().from_string(markdown)
                config["body"] = markdown.render(template_variables)
            
        # Compile jinja2 template into a string and return.
        template = Template(config["template"])
        return template.render(template_variables)
        
    def get_name(self):
        return self.name
        
    def get_template(self):
        return self.template
        
    def __init__(self, content_path):
        abspath = os.path.abspath(os.path.join(Content.content_path, content_path))
        super(Content, self).__init__(abspath)
        self.name = self.get_config()["name"]
        self.template = self.get_config()["template"]
        try:
            self.content = self.get_config()["content"]
        except KeyError:
            print("info: No Markdown content for " + self.name)
        
"""
Simple wrapper around assets of various types.
"""
class Asset(Config):
    def get_name(self):
        return self.name

    def __init__(self, name, asset_path):
        super(Asset, self).__init__(asset_path)
        self.name = name
        
"""
Encapsulates site variables and configuration.
"""
class Site(Config):
    def build(self):
        # Get directories
        dirs = ["assets"]
        for name, content in Content.get_content().items():
            if name == "index":
                continue
            dirs.append(name)
             # Add content to site.content for template use
            self.config["content"].append(content.get_config())
        
        # Create directories if the don"t exist
        output_dir = self.sources["output"]
        for directory in dirs:
            dirname = os.path.join(output_dir, directory)
            if not os.path.exists(dirname):
                print("creating folder: " + dirname)
                os.makedirs(dirname)
                
        # Copy static files
        print("info: Copying asset files")
        copytree(self.sources["assets"], os.path.join(output_dir, "assets"))

        # Compile content
        rendered_content = {}
        for name, content in Content.get_content().items():
            print("compile: " + name)
            if name == "index":
                path = os.path.join(os.getcwd(), self.sources["output"], "index.html")
            else:
                path = os.path.join(os.getcwd(), self.sources["output"], name, "index.html")
            render = content.render(self.get_config(), self.sources["output"], self.environment)
            
            # Add rendered content to the list of HTML strings
            rendered_content[path] = render
            
        for path, content in rendered_content.items():
            print("writing file: " + path)
            file = open(path, "w+")
            file.write(content)
            file.close()

    def validate_filepath(self, path, config_path):
        fullpath = os.path.abspath(os.path.join(config_path, path))
        if os.path.exists(fullpath) == False:
            print("error: " + fullpath + " doesn\"t exist")
        return True

    def validate(self, config, config_path):
        if "sources" not in config:
            print("error: Sources not defined")
            return False
        try:
            if self.validate_filepath(config["sources"]["assets"], config_path) == False:
                print("error: Invalid assets folder")
                return False
            if self.validate_filepath(config["sources"]["content"], config_path) == False:
                print("error: Invalid content folder")
                return False
            if self.validate_filepath(config["sources"]["output"], config_path) == False:
                print("error: Invalid output folder")
                return False
            if self.validate_filepath(config["sources"]["templates"], config_path) == False:
                print("error: Invalid templates folder")
                return False
        except KeyError as err:
            print("error: Missing required property " + str(err))
            return False
        return True
        
    def get_output_path(self):
        return os.path.abspath(os.path.join(self.get_path(), self.get_config()["sources"]["output"]))

    def __init__(self, config_path):
        super(Site, self).__init__(config_path)
        self.environment = ENVIRONMENT
        self.sources = {
            "assets": os.path.join(config_path, self.get_config()["sources"]["assets"]),
            "content": os.path.join(config_path, self.get_config()["sources"]["content"]),
            "output": os.path.join(config_path, self.get_config()["sources"]["output"]),
            "templates": os.path.join(config_path, self.get_config()["sources"]["templates"]),
        }
        
        # Container for all content
        self.config["content"] = []
        
        # Search for content and set template folder
        Content.search(self.sources["content"])
        Template.set_template_path(self.sources["templates"])

# blueprint new [name] -p [path]
# blueprint build -p [path] -o [output]
# blueprint serve -p [path]

# http://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def main():
    print("blot v2.0")
    print("=========")

    path = os.path.abspath(os.path.join(os.getcwd(), "example"))
    output = "output/"
    build(path, output)
    # serve(path, "127.0.0.1", 8000)
    
def new(name, config_path):
    pass
    
def build(config_path, output):
    site = Site(config_path)
    site.build()
    
def serve(config_path, address, port):
    site = Site(config_path)
    os.chdir(site.get_output_path()) # Change cwd
    import http.server, socketserver
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((address, port), Handler)
    print("serve: Serving at ", address + ":" + str(port))
    httpd.serve_forever()
    
if __name__ == "__main__":
    main()