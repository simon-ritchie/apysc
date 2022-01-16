"""The script to install the released (latest) apysc package from PyPI.
Also, removing checked out directories and additional minimum tests
will be run.

This is used by the deploying job mainly.
"""

import os
import shutil
import time
from typing import List
import sys

sys.path.append('./')

import apysc as ap
import scripts.command_util as command_util

_PIP_COMMAND: str = f'pip install apysc=={ap.__version__}'
_APYSC_TEST_CODE: str = (
    'import apysc as ap;'
    'stage: ap.Stage = ap.Stage();'
    "ap.save_overall_html(dest_dir_path='./');"
)


def _main() -> None:
    """
    Install the released (latest) apysc package from PyPI.
    Also, removing checked out directories and additional minimum tests
    will be run.
    """
    os.system('pip freeze | xargs pip uninstall -y')

    count: int = 0
    while True:
        stdout: str = command_util.run_command(command=_PIP_COMMAND)
        if 'ERROR: Could not find a version' not in stdout:
            break

        if count >= 10:
            raise Exception('apysc package installing is failed.')
        count += 1
        print(f'Sleeping 10 seconds... (retrying count: {count})')
        time.sleep(10)

    file_or_dir_names: List[str] = os.listdir('./')
    for file_or_dir_name in file_or_dir_names:
        if os.path.isfile(file_or_dir_name):
            os.remove(file_or_dir_name)
            continue
        if os.path.isdir(file_or_dir_name):
            shutil.rmtree(file_or_dir_name, ignore_errors=True)

    os.system(f'python -c "{_APYSC_TEST_CODE}"')
    assert os.path.exists('./index.html')
    print('HTML file is created by the apysc package correctly.')


if __name__ == '__main__':
    _main()
