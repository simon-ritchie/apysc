"""This module is for translation-mapping
utility implementations.
"""

import importlib
import os
from types import ModuleType
from typing import Dict, List, Union

from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc.document_text_split_util import BodyText
from apysc._lint_and_doc.document_text_split_util import CodeBlock
from apysc._lint_and_doc.document_text_split_util import Heading

MAPPING_CONST_NAME: str = 'MAPPING'
_SplittedVals = List[Union[Heading, BodyText, CodeBlock]]


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


def convert_splitted_values_to_keys(
        *,
        splitted_values: _SplittedVals) -> List[str]:
    """
    Convert specified splitted values to dictionary's key
    strings.

    Parameters
    ----------
    splitted_values : List of Heading, BodyText and CodeBlock
        Target splitted values.

    Returns
    -------
    keys : list of str
        Converted strings.
    """
    keys: List[str] = []
    for splitted_value in splitted_values:
        is_body_text: bool = False
        key: str = ''
        if isinstance(splitted_value, Heading):
            key = splitted_value.overall_text
        if isinstance(splitted_value, BodyText):
            is_body_text = True
            key = splitted_value.text
        if isinstance(splitted_value, CodeBlock):
            key = splitted_value.overall_code_block
        key = escape_key_or_value(key_or_val=key)
        if not is_body_text:
            keys.append(key)
        else:
            _append_body_text_keys_to_list(key=key, keys=keys)
    return keys


def _append_body_text_keys_to_list(
        *, key: str, keys: List[str]) -> None:
    """
    Append document's body text keys to a specified key's list.

    Parameters
    ----------
    key : str
        A target key string. This interface splits its string
        if there are two consecutive line breaks.
    keys : list of str
        A key's list to append.
    """
    splitted_keys: List[str] = key.split('\\n\\n')
    for key_ in splitted_keys:
        keys.append(key_)


def escape_key_or_value(*, key_or_val: str) -> str:
    """
    Escape a mapping key or value to save.

    Parameters
    ----------
    key_or_val : str
        A target key or value.

    Returns
    -------
    key_or_val : str
        An escaped key or value string.
    """
    key_or_val = key_or_val.replace('\\', '\\\\')
    key_or_val = key_or_val.replace("'", "\\'")
    key_or_val = key_or_val.replace('\n', '\\n')
    key_or_val = key_or_val.replace('\\\\n', '\\n')
    return key_or_val
