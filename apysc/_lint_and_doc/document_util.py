"""
This module is for the common utilities and definitions
for the documents.
"""

from typing import List
import os
from pathlib import Path

from apysc._lint_and_doc.docs_lang import Lang

SRC_DIR_PATH: str = '/mnt/apysc/docs_src/source/'


def get_docs_md_file_paths() -> List[str]:
    """
    Get documents' markdown file paths.

    Returns
    -------
    file_paths : List[str]
        Documenet's markdown file paths.
    """
    file_names: List[str] = os.listdir(SRC_DIR_PATH)
    file_paths: List[str] = []
    for file_name in file_names:
        file_path: str = os.path.join(SRC_DIR_PATH, file_name)
        if not file_path.endswith('.md'):
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
            patterns.append(f'{lang.value}_*.md')
        return patterns

    docs_file_paths: List[str] = get_docs_md_file_paths()
    for doc_file_path in docs_file_paths:
        basename: str = os.path.basename(doc_file_path)
        if not basename.startswith(f'{lang.value}_'):
            patterns.append(f'{basename}')
    return patterns
