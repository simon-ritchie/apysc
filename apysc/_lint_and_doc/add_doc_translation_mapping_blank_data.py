"""This module is for the adding of document translations
mapping dictionary's blank data.
"""

from enum import Enum
from types import ModuleType
from typing import Dict, List, Union
import os
import importlib

from apysc._lint_and_doc import document_text_split_util
from apysc._lint_and_doc.document_text_split_util import Heading, BodyText, CodeBlock

_SplittedVals = List[Union[Heading, BodyText, CodeBlock]]


class Lang(Enum):
    """Translation target languages definitions.
    """
    JP = 'jp'


_MAPPING_CONST_NAME: str = 'MAPPING'


def add_mapping_blank_data(*, lang: Lang) -> None:
    """
    Add mapping blank data of document translations.

    Parameters
    ----------
    lang : Lang
        A target translation language.
    """
    from apysc._file import file_util
    src_docs_file_paths: List[str] = _get_src_docs_file_paths()
    for src_doc_file_path in src_docs_file_paths:
        markdown_txt: str = file_util.read_txt(file_path=src_doc_file_path)
        splitted_values: _SplittedVals= document_text_split_util.\
            split_markdown_document(markdown_txt=markdown_txt)
        keys: List[str] = _convert_splitted_values_to_keys(
            splitted_values=splitted_values)
        mappings: List[Dict[str, str]] = _make_mappings_from_keys(
            keys=keys, src_doc_file_path=src_doc_file_path,
            lang=lang)
        _save_mapping_data(
            mappings=mappings, src_doc_file_path=src_doc_file_path,
            lang=lang)
    pass


def _save_mapping_data(
        *, mappings: List[Dict[str, str]],
        src_doc_file_path: str,
        lang: Lang) -> None:
    """
    Save mapping data module with specified mappings data.

    Parameters
    ----------
    mappings : list of dict
        Target mappings data to save.
    src_doc_file_path : str
        A target source document file path.
    lang : Lang
        A target translation language.
    """
    from apysc._file import file_util
    basename: str = os.path.basename(src_doc_file_path)
    module_str: str = (
        f'"""This module is for the translation mapping data '
        'of the \nfollowing document:'
        f'\n\nDocument file: {basename}'
        f'\nLanguage: {lang.value}'
        '\n"""'
        '\n\nfrom typing import Dict'
        f'\n\n{_MAPPING_CONST_NAME}: Dict[str, str] = {{'
    )
    for mapping in mappings:
        key: str = list(mapping.keys())[0]
        value: str = list(mapping.values())[0]
        module_str += (
            f"\n\n    '{key}':"
            f"\n    '{value}',"
        )
        if len(value) >= 74:
            module_str += '  # noqa'
    module_str += '\n\n}'
    module_path: str = _get_mapping_module_path(
        src_doc_file_path=src_doc_file_path, lang=lang)
    file_util.save_plain_txt(txt=module_str, file_path=module_path)


def _make_mappings_from_keys(
        *, keys: List[str],
        src_doc_file_path: str,
        lang: Lang) -> List[Dict[str, str]]:
    """
    Make mapping dictionary values from specified key values.

    Parameters
    ----------
    keys : list of str
        Target dictionary key values.
    src_doc_file_path : str
        A target source document file path.
    lang : Lang
        A target translation language.

    Returns
    -------
    mappings : list of dict
        Created mapping dictionary values. A dictionary
        value becomes a blank string if it is a new mapping value.
    """
    already_saved_mapping: Dict[str, str] = _read_already_saved_mapping(
        src_doc_file_path=src_doc_file_path, lang=lang)
    mappings: List[Dict[str, str]] = []
    for key in keys:
        value: str = already_saved_mapping.get(key, '')
        mappings.append({key: value})
    return mappings


def _read_already_saved_mapping(
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
    mapping_module_path: str = _get_mapping_module_path(
        src_doc_file_path=src_doc_file_path, lang=lang)
    if not os.path.isfile(mapping_module_path):
        return {}
    module: ModuleType = module_util.read_target_path_module(
        module_path=mapping_module_path)
    importlib.reload(module)
    if not hasattr(module, _MAPPING_CONST_NAME):
        return {}
    already_saved_mapping: Dict[str, str] = getattr(
        module, _MAPPING_CONST_NAME)
    return already_saved_mapping


def _get_mapping_module_path(
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


def _convert_splitted_values_to_keys(
        *, splitted_values: _SplittedVals) -> List[str]:
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
        A converted key strings.
    """
    keys: List[str] = []
    for splitted_value in splitted_values:
        key: str = ''
        if isinstance(splitted_value, Heading):
            key = splitted_value.overall_text
        if isinstance(splitted_value, BodyText):
            key = splitted_value.text
        if isinstance(splitted_value, CodeBlock):
            key = splitted_value.overall_code_block
        key = key.replace("'", "\\'")
        keys.append(key)
    return keys


def _get_src_docs_file_paths() -> List[str]:
    """
    Get source documents file paths.

    Returns
    -------
    src_docs_file_paths : list of str
        Source documents file paths.
    """
    dir_path: str = './docs_src/source/'
    file_or_dir_names: List[str] = os.listdir(dir_path)
    src_docs_file_paths: List[str] = []
    for file_or_dir_name in file_or_dir_names:
        file_or_dir_path: str = os.path.join(dir_path, file_or_dir_name)
        if not os.path.isfile(file_or_dir_path):
            continue
        if not file_or_dir_path.endswith('.md'):
            continue
        if _is_translated_document(path=file_or_dir_path):
            continue
        src_docs_file_paths.append(file_or_dir_path)
    return src_docs_file_paths


def _is_translated_document(*, path: str) -> bool:
    """
    Get a boolean indicating whether a specified document path
    is a translated document or not.

    Parameters
    ----------
    path : str
        A target document path.

    Returns
    -------
    result : bool
        If a specified document path is a translated document,
        this interface returns True.
    """
    basename: str = os.path.basename(path)
    for lang in Lang:
        if basename.startswith(lang.value):
            return True
    return False
