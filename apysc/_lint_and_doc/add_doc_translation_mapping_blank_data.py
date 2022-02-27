"""This module is for the adding of document translations
mapping dictionary's blank data.
"""

from enum import Enum
from types import ModuleType
from typing import Dict, List, Union, Optional, Match
import os
import importlib
import re

from apysc._lint_and_doc import document_text_split_util
from apysc._lint_and_doc.document_text_split_util import Heading, BodyText, CodeBlock
from apysc._lint_and_doc import lint_and_doc_hash_util
from apysc._lint_and_doc.lint_and_doc_hash_util import HashType
from apysc._lint_and_doc.docstring_util import DOCSTRING_PATH_COMMENT_PATTERN

_SplittedVals = List[Union[Heading, BodyText, CodeBlock]]


class Lang(Enum):
    """Translation target languages definitions.
    """
    JP = 'jp'


_MAPPING_CONST_NAME: str = 'MAPPING'

_SKIPPING_PATTERNS: List[str] = [
    DOCSTRING_PATH_COMMENT_PATTERN,
]

_MAPPING_UNNECESSARY_STRS: List[str] = [
    '<hr>',
]


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
    hash_type: HashType = _get_hash_type_from_lang(lang=lang)
    src_docs_file_paths = lint_and_doc_hash_util.\
        remove_not_updated_file_paths(
            file_paths=src_docs_file_paths,
            hash_type=hash_type)
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
    lint_and_doc_hash_util.save_target_files_hash(
        file_paths=src_docs_file_paths, hash_type=hash_type)


def _get_hash_type_from_lang(*, lang: Lang) -> HashType:
    """
    Get a hash type from a specified language type.

    Parameters
    ----------
    lang : Lang
        A target translation language.

    Returns
    -------
    hash_type : HashType
        A target hash type.

    Raises
    ------
    ValueError
        If there is no implementation of a specified language
        type's branch condition.
    """
    if lang == Lang.JP:
        return HashType.TRANSLATION_MAPPING_JP
    raise ValueError(
        'There is no implementation of a specified language type\'s '
        'branch condition. Please add a necessary branch condition: '
        f'{lang}')


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
        'of the\nfollowing document:'
        f'\n\nDocument file: {basename}'
        f'\nLanguage: {lang.value}'
        '\n"""'
        '\n\nfrom typing import Dict'
        f'\n\n{_MAPPING_CONST_NAME}: Dict[str, str] = {{'
    )
    for mapping in mappings:
        key: str = list(mapping.keys())[0]
        value: str = list(mapping.values())[0]
        module_str += f"\n\n    '{key}':"
        if len(key) >= 70:
            module_str += '  # noqa'
        module_str += f"\n    '{value}',"
        if len(value) >= 70:
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
        key_: str = key.replace('\\\\', '\\')
        key_: str = key_.replace("\\'", "'")
        key_: str = key_.replace('\\n', '\n')
        value: str = already_saved_mapping.get(key_, '')
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
        is_body_text: bool = False
        key: str = ''
        if isinstance(splitted_value, Heading):
            key = splitted_value.overall_text
        if isinstance(splitted_value, BodyText):
            is_body_text = True
            key = splitted_value.text
        if isinstance(splitted_value, CodeBlock):
            key = splitted_value.overall_code_block
        key = key.replace('\\', '\\\\')
        key = key.replace("'", "\\'")
        key = key.replace('\n', '\\n')
        if not is_body_text:
            keys.append(key)
        else:
            _append_body_text_keys_to_list(key=key, keys=keys)
    keys = _remove_skipping_pattern_keys_from_list(keys=keys)
    keys = _remove_unnecessary_strs_from_key_list(keys=keys)
    return keys


def _remove_unnecessary_strs_from_key_list(
        *, keys: List[str]) -> List[str]:
    """
    Remove unnecessary strings from a specified key's list.

    Parameters
    ----------
    keys : list of str
        A target key's list.

    Returns
    -------
    result_keys : list of str
        An after removing key's list.
    """
    result_keys: List[str] = []
    for key in keys:
        if key in _MAPPING_UNNECESSARY_STRS:
            continue
        result_keys.append(key)
    return result_keys


def _remove_skipping_pattern_keys_from_list(
        *, keys: List[str]) -> List[str]:
    """
    Remove skipping pattern matching keys from a specified list.

    Parameters
    ----------
    keys : list of str
        A target key's list.

    Returns
    -------
    result_keys : list of str
        An after removing key's list.
    """
    result_keys: List[str] = []
    for key in keys:
        is_pattern_matching: bool = False
        for pattern in _SKIPPING_PATTERNS:
            match: Optional[Match] = re.search(
                pattern=pattern, string=key,
                flags=re.MULTILINE | re.DOTALL)
            if match is not None:
                is_pattern_matching = True
                break
        if is_pattern_matching:
            continue
        result_keys.append(key)
    return result_keys


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
