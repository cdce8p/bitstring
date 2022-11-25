# Configuration file for the Sphinx documentation builder.
#
import datetime

year = datetime.datetime.now().year

project = 'bitstring'
copyright = f'2006 - {year}, Scott Griffiths'
author = 'Scott Griffiths'
release = '4.0'

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

root_doc = 'index'

add_function_parentheses = False
add_module_names = False

html_show_sphinx = False
html_static_path = ['_static']
html_css_files = ["custom.css"]

html_theme = 'piccolo_theme'

html_theme_options = {
    "banner_text": "New major version released. Requires Python 3.7 or later - see release notes for full details.",
    "banner_hiding": "permanent",
    "show_theme_credit": False,
    "globaltoc_maxdepth": 2,
    "source_url": 'https://github.com/scott-griffiths/bitstring/',
}
