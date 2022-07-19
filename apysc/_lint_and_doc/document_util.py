"""
This module is for the common utilities and definitions
for the documents.
"""

import os
from typing import List

from apysc._lint_and_doc.docs_lang import Lang


def _get_src_dir_path() -> str:
    """
    Get a source directory path.

    Returns
    -------
    src_dir_path : str
        A source directory path.
    """
    src_dir_path: str = "/mnt/apysc/docs_src/source/"
    if os.path.isdir("./docs_src/"):
        src_dir_path = "./docs_src/source/"
    return src_dir_path


def get_docs_md_file_paths() -> List[str]:
    """
    Get documents' markdown file paths.

    Returns
    -------
    file_paths : List[str]
        Documenet's markdown file paths.
    """
    src_dir_path: str = _get_src_dir_path()
    file_names: List[str] = os.listdir(src_dir_path)
    file_paths: List[str] = []
    for file_name in file_names:
        file_path: str = os.path.join(src_dir_path, file_name)
        if not file_path.endswith(".md"):
            continue
        file_paths.append(file_path)
    return file_paths


def get_exclude_patterns(*, lang: Lang) -> List[str]:
    """
    Get excluding patterns' list.

    Parameters
    ----------
    lang : Lang
        A target language of documents.

    Returns
    -------
    patterns : List[str]
        Excluding patterns' list.
    """
    patterns: List[str] = []
    if lang == Lang.EN:
        for lang in Lang:
            patterns.append(f"{lang.value}_*.md")
        return patterns

    docs_file_paths: List[str] = get_docs_md_file_paths()
    for doc_file_path in docs_file_paths:
        basename: str = os.path.basename(doc_file_path)
        if not basename.startswith(f"{lang.value}_"):
            patterns.append(f"{basename}")
    return patterns
