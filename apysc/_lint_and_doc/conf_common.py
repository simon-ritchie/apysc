"""This module is for the common settings of each
Sphinx's conf.py module.
"""

from typing import Dict, List
from recommonmark.parser import CommonMarkParser


PROJECT: str = 'apysc'
AUTHOR: str = 'simonritchie'
EXTENSIONS: List[str] = [
    'recommonmark',
    'sphinx_markdown_tables',
]
TEMPLATES_PATH: List[str] = ['_templates']
SOURCE_SUFFIX: Dict[str, str] = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
SOURCE_PARSERS: Dict[str, type] = {
    '.md': CommonMarkParser,
}
HTML_THEME: str = 'groundwork'
HTML_STATIC_PATH: List[str] = ['_static']
HTML_CSS_FILES: List[str] = [
    'base.css',
    'codeblock.css',
    'iframe.css',
]
HTML_LOGO: str = '../_static/logo_for_document.png'
