"""This module is for the common settings of each
Sphinx's conf.py module.
"""

from typing import List


PROJECT: str = 'apysc'
AUTHOR: str = 'simonritchie'
EXTENSIONS: List[str] = [
    'recommonmark',
    'sphinx_markdown_tables',
]
