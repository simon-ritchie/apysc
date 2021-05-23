"""Documentations build script.

Command example:
$ python build_docs.py
"""

import os
import shutil
import subprocess as sp
from logging import Logger
from typing import List

from apysc.console import loggers

logger: Logger = loggers.get_info_logger()


def _main() -> None:
    """Entry point of this command.
    """
    logger.info(msg='Sphix build command started...')
    os.chdir('./docs_src/')
    complete_process: sp.CompletedProcess = sp.run(
        'make html', shell=True,
        stdout=sp.PIPE, stderr=sp.STDOUT)
    stdout: str = complete_process.stdout.decode('utf-8')
    print(stdout)

    logger.info(msg='Moving documentation to docs directory...')
    os.chdir('../')
    shutil.rmtree('./docs/', ignore_errors=True)
    shutil.copytree(src='./docs_src/build/html/', dst='./docs/')

    logger.info(msg='Replacing `_static` paths by `static`...')
    _replace_static_path()

    logger.info(msg='Build completed!')


def _replace_static_path() -> None:
    """
    Replace document `_static` paths by `static`.
    """
    shutil.move(src='./docs/_static/', dst='./docs/static/')
    _replace_static_path_recursively(dir_path='./docs/')


def _replace_static_path_recursively(dir_path: str) -> None:
    """
    Replace each files' `_static` paths by `static`.

    Parameters
    ----------
    dir_path : str
        Target directory path.
    """
    file_or_dir_names: List[str] = os.listdir(dir_path)
    file_extensions: List[str] = ['.html', '.js']
    for file_or_dir_name in file_or_dir_names:
        file_or_dir_path: str = os.path.join(dir_path, file_or_dir_name)
        if os.path.isdir(file_or_dir_path):
            _replace_static_path_recursively(dir_path=file_or_dir_path)
            continue
        extension: str = os.path.splitext(file_or_dir_path)[1]
        if extension not in file_extensions:
            continue
        with open(file_or_dir_path) as f:
            file_txt: str = f.read()
        file_txt = file_txt.replace('_static', 'static')
        with open(file_or_dir_path, 'w') as f:
            f.write(file_txt)


if __name__ == '__main__':
    _main()
