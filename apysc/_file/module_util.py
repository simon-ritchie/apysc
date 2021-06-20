"""Module related common utilities.

Mainly following interfaces are defined:

- get_module_paths_recursively
    Get all module paths under the specified directory.
- save_tmp_module_and_run_script
    Save temporary Python module and run that script.
"""

import os
import subprocess as sp
from datetime import datetime
from typing import List
from typing import Optional


def get_module_paths_recursively(
        dir_path: str = './',
        module_paths: Optional[List[str]] = None) -> List[str]:
    """
    Get all module paths under the specified directory.

    Parameters
    ----------
    dir_path : str
        Directory path to search modules.
    module_paths : list of str or None
        Current Python module paths (only used by recursive
        function calls).

    Returns
    -------
    module_paths : list of str
        Python module paths.
        `__init__.py` modules will not be included.
    """
    if module_paths is None:
        module_paths = []
    file_or_dir_names: List[str] = os.listdir(dir_path)
    for file_or_dir_name in file_or_dir_names:
        file_or_dir_path: str = os.path.join(dir_path, file_or_dir_name)
        if os.path.isdir(file_or_dir_path):
            module_paths = get_module_paths_recursively(
                dir_path=file_or_dir_path, module_paths=module_paths)
            continue
        if not file_or_dir_path.endswith('.py'):
            continue
        if file_or_dir_name == '__init__.py':
            continue
        module_paths.append(file_or_dir_path)
    return module_paths


def save_tmp_module_and_run_script(script: str) -> str:
    """
    Save temporary Python module and run that script.

    Parameters
    ----------
    script : str
        Python script string.

    Returns
    -------
    stdout : str
        Result stdout string.
    """
    tmp_mod_path: str = f'./tmp_{datetime.now().timestamp()}.py'
    with open(tmp_mod_path, 'w') as f:
        f.write(script)
    process: sp.CompletedProcess = sp.run(
        f'python {tmp_mod_path}', shell=True,
        stdout=sp.PIPE, stderr=sp.STDOUT)
    stdout: str = process.stdout.decode('utf-8')
    os.remove(tmp_mod_path)
    return stdout
