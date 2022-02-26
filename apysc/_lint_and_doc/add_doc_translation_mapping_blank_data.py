"""This module is for the adding of document translations
mapping dictionary's blank data.
"""

from enum import Enum
from typing import List, Union
import os

from apysc._lint_and_doc import document_text_split_util
from apysc._lint_and_doc.document_text_split_util import Heading, BodyText, CodeBlock

_SplittedVals = List[Union[Heading, BodyText, CodeBlock]]


class Lang(Enum):
    """Translation target languages definitions.
    """
    JP = 'jp'


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
    pass


def _convert_splitted_values_to_keys(
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
