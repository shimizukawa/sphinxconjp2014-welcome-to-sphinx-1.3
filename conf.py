# -*- coding: utf-8 -*-
import os, sys
sys.path.append(os.path.abspath('.'))

language = 'ja'

master_doc = 'index'
project = u'Welcome to Sphinx-1.3'
copyright = u'2014, Takayuki SHIMIZUKAWA'
version = release = '1.0'
exclude_patterns = ['_build', '.venv']
locale_dirs = ['locale']
pygments_style = 'sphinx'
extensions = [
    'sphinx.ext.todo',
    'sphinxjp.themes.s6',
]
todo_include_todos = True
html_logo = 'images/sphinx-logo.png'
html_static_path = ['_static']
html_use_index = False
html_theme = 's6'



# -- directive/role definition ------------------------------------------------>

from docutils.parsers.rst.directives.admonitions import Admonition
from sphinx.util.compat import make_admonition


class SpeechDirective(Admonition):
    css_class = 'speech'
    required_arguments = 0
    optional_arguments = 0

    def run(self):
        title = u'[speech]'
        if self.arguments:
            title += self.arguments[0]

        if 'class' in self.options:
            self.options['class'].append(self.css_class)
        else:
            self.options['class'] = [self.css_class]

        ret = make_admonition(
            self.node_class, self.name, [title], self.options,
            self.content, self.lineno, self.content_offset, self.block_text,
            self.state, self.state_machine)
        ret[0].attributes['name'] = self.name
        return ret


def setup(app):
    app.add_directive('speech', SpeechDirective)
    if app.config._raw_config.get('html_theme') == 's6':
        app.add_stylesheet('custom.css')
        app.add_javascript('custom.js')
