"""This module is for the adding of document translations
mapping dictionary's blank data.
"""

from enum import Enum
from typing import List
import os


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
    src_docs_file_paths: List[str] = _get_src_docs_file_paths()
    pass


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
        src_docs_file_paths.append(file_or_dir_path)
    return src_docs_file_paths
