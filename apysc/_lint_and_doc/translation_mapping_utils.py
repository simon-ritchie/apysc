"""This module is for the translation-mapping
utility implementations.
"""

import importlib
import os
from types import ModuleType
from typing import Dict
from apysc._lint_and_doc.docs_lang import Lang

MAPPING_CONST_NAME: str = 'MAPPING'


def read_mapping_data(
        *, src_doc_file_path: str,
        lang: Lang) -> Dict[str, str]:
    """
    Read an already saved mapping data.

    Parameters
    ----------
    src_doc_file_path : str
        A target source document file path.
    lang : Lang
        A target translation language.

    Returns
    -------
    already_saved_mapping : dict
        An already saved mapping data dictionary.
    """
    from apysc._file import module_util
    mapping_module_path: str = get_mapping_module_path(
        src_doc_file_path=src_doc_file_path, lang=lang)
    if not os.path.isfile(mapping_module_path):
        return {}
    module: ModuleType = module_util.read_target_path_module(
        module_path=mapping_module_path)
    importlib.reload(module)
    if not hasattr(module, MAPPING_CONST_NAME):
        return {}
    already_saved_mapping: Dict[str, str] = getattr(
        module, MAPPING_CONST_NAME)
    return already_saved_mapping


def get_mapping_module_path(
        *, src_doc_file_path: str, lang: Lang) -> str:
    """
    Get a mapping data module path.

    Parameters
    ----------
    src_doc_file_path : str
        A target source document file path.
    lang : Lang
        A target translation language.

    Returns
    -------
    mapping_module_path : str
        A mapping data module path.
    """
    basename: str = os.path.basename(src_doc_file_path)
    basename = basename.replace('.md', '.py', 1)
    mapping_module_path: str = os.path.join(
        f'./apysc/_translation/{lang.value}/',
        basename,
    )
    return mapping_module_path
