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

from typing import Dict
from typing import List

from recommonmark.parser import CommonMarkParser
from typing_extensions import Final

# -- Project information -----------------------------------------------------

project: Final[str] = 'apysc'
copyright: Final[str] = '2021, apysc project'
author: Final[str] = 'simonritchie'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions: Final[List[str]] = [
    'recommonmark',
    'sphinx_markdown_tables',
]

# Add any paths that contain templates here, relative to this directory.
templates_path: Final[List[str]] = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: Final[List[str]] = []

source_suffix: Final[Dict[str, str]] = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

source_parsers: Final[Dict[str, type]] = {
    '.md': CommonMarkParser,
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme: Final[str] = 'groundwork'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path: Final[List[str]] = ['_static', 'static']
