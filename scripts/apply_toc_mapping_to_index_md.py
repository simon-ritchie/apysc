"""Apply table-of-contents text mappings to each index's
markdown file.

Command examples:
$ python scripts/apply_toc_mapping_to_index_md.py
"""

import os
import subprocess as sp
import sys
from logging import Logger
from typing import List

sys.path.append('./')

from apysc._console import loggers
from apysc._file import module_util
from apysc._lint_and_doc import lint_and_doc_hash_util

logger: Logger = loggers.get_info_logger()


def _main() -> None:
    """Entry point of this command.
    """
    print('-' * 20)
    logger.info(
        msg='Applying index.md\'s table-of-contents text mappings...')
    html_paths: List[str] = _get_target_html_paths()
    pass


def _get_target_html_paths() -> List[str]:
    """
    Get target index.html's file paths.

    Returns
    -------
    html_paths : list of str
        Target HTML files paths.
    """
    html_paths: List[str] = []
    DIR_PATH: str = './docs/'
    file_names: List[str] = os.listdir(DIR_PATH)
    for file_name in file_names:
        if not file_name.endswith('index.html'):
            continue
        html_path: str = os.path.join(
            DIR_PATH,
            file_name,
        )
        html_paths.append(html_path)
    return html_paths


if __name__ == '__main__':
    _main()
