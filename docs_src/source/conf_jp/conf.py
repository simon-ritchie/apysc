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

import sys
from datetime import datetime
from typing import Dict
from typing import List

from sphinx.application import Sphinx
from typing_extensions import Final

sys.path.append('../../../')
from apysc._lint_and_doc import conf_common
from apysc._lint_and_doc import document_util
from apysc._lint_and_doc.docs_lang import Lang

# -- Project information -----------------------------------------------------

_now: datetime = datetime.now()
_lang: Lang = Lang.JP
project: Final[str] = conf_common.PROJECT
copyright: Final[str] = f'{_now.year}, {project} プロジェクト'
author: Final[str] = conf_common.AUTHOR


# -- General configuration ---------------------------------------------------

root_doc: str = 'jp_index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions: Final[List[str]] = conf_common.EXTENSIONS

# Add any paths that contain templates here, relative to this directory.
templates_path: Final[List[str]] = conf_common.TEMPLATES_PATH

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: Final[List[str]] = document_util.get_exclude_patterns(
    lang=_lang)

source_suffix: Final[Dict[str, str]] = conf_common.SOURCE_SUFFIX

source_parsers: Final[Dict[str, type]] = conf_common.SOURCE_PARSERS


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme: Final[str] = conf_common.HTML_THEME

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path: Final[List[str]] = conf_common.HTML_STATIC_PATH

html_css_files: Final[List[str]] = conf_common.HTML_CSS_FILES

html_logo: Final[str] = conf_common.HTML_LOGO

# Disable the `_sources` copying.
html_copy_source: bool = conf_common.HTML_COPY_SOURCE


def setup(sphinx: Sphinx) -> None:
    """
    The Sphinx calls when it starts building.

    Parameters
    ----------
    sphinx : Sphinx
        The Sphinx instance.
    """
    conf_common.setup(sphinx=sphinx)
