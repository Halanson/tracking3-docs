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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Tracking3'
copyright = '2021, tracking3.io'
author = 'Martin Melzer'


# -- General configuration ---------------------------------------------------

root_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [

]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.rst']


# -- Options for HTML output -------------------------------------------------

html_logo = '_static/favicon.svg'
html_favicon = '_static/favicon.ico'
html_show_sourcelink = True
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

nav_bar_tabs = []

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'
html_theme_options = {
    'nav_title': 'App Documentation',
    'base_url': 'https://docs.tracking3.io/',
    'color_primary': 'orange',
    'color_accent': 'red',
    'html_minify': True,
    'css_minify': True,
    'repo_name': 'tracking3.io - Docs',
    'repo_url': 'https://github.com/Tracking3/tracking3-docs',
    'repo_type': 'github',
    'google_analytics_account': 'G-6XQPCXW501',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

