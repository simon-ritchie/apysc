"""This module is for the common settings of each
Sphinx's conf.py module.
"""

from typing import Dict, List


PROJECT: str = 'apysc'
AUTHOR: str = 'simonritchie'
EXTENSIONS: List[str] = [
    'recommonmark',
    'sphinx_markdown_tables',
]
SOURCE_SUFFIX: Dict[str, str] = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
