"""
This module is for the common utilities and definitions
for the documents.
"""

from typing import List
import os

SRC_DIR_PATH: str = './docs_src/source/'


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
