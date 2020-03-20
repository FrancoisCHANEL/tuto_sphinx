# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))


# -- Project information -----------------------------------------------------

project = 'documm'
copyright = '2020, francois'
author = 'francois'

# The full version, including alpha/beta/rc tags
release = '1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.doctest',
    'hidden_code_block'
]

napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

doctest_global_setup = '''
try:
    import pandas as pd
except ImportError:
    pd = None
'''


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'nature'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


def setup(app):
    app.add_stylesheet('theme_overrides.css')


# pour parader le problème Sphinx error: master file c:\git\tuto_sphinx\docs\contents.rst not found
master_doc = 'index'


#* choix d'un thème pour les code snippets
# pygments_style = 'default'
pygments_style = 'sphinx'

#* force l'affichage de la docstring d'une classe + de celle de sa méthode __init__ ou __new__
autoclass_content = 'both'

#* précise quelles options sont appelées par les méthodes auto(module, class, function, etc.)
autodoc_default_options = {
    'members': True,
    'undoc-members' : True,
    'undoc-members': True,
    'exclude-members': [
        '__weakref__', 
        '__repr__', 
        '__str__', 
        '__init__', 
        '__dict__', 
        '__module__',
        'remove_proxy'
    ],
    'private-members' : True,
    'special-members' : True,
}

les_exclus = autodoc_default_options['exclude-members']
les_exclus = ', '.join(les_exclus)
autodoc_default_options.update({
    'exclude-members':les_exclus
})

#* gère la prise en compte des type hints dans auto-doc
autodoc_typehints = 'signature'

