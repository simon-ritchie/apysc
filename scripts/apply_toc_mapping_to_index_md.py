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
    module_paths: List[str] = _get_target_module_paths()
    pass


def _get_target_module_paths() -> List[str]:
    """
    Get target index.md's module paths.

    Returns
    -------
    module_paths : list of str
        Target module paths.
    """
    module_paths: List[str] = []
    DIR_PATH: str = './docs_src/source/'
    file_names: List[str] = os.listdir(DIR_PATH)
    for file_name in file_names:
        if not file_name.endswith('index.md'):
            continue
        module_path: str = os.path.join(
            DIR_PATH,
            file_name,
        )
        module_paths.append(module_path)
    return module_paths


if __name__ == '__main__':
    _main()
