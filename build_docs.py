"""Documentations build script.

Command example:
$ python build_docs.py
"""

import os
import shutil
import subprocess as sp
from logging import Logger

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

    logger.info(msg='Build completed!')


if __name__ == '__main__':
    _main()
