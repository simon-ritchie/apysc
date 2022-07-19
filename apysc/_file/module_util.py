"""Module related common utilities.

Mainly following interfaces are defined:

- get_module_paths_recursively
    - Get all module paths under the specified directory.
- save_tmp_module
    - Save a temporary Python module.
- save_tmp_module_and_run_script
    - Save a temporary Python module and run that script.
- read_target_path_module
    - Read a module of the specified module path.
- read_module_or_class_from_package_path
    - Read a specified package path module or class.
"""

import importlib
import os
import subprocess as sp
from datetime import datetime
from random import randint
from types import ModuleType
from typing import Any
from typing import List
from typing import Optional


def get_module_paths_recursively(
    dir_path: str = "./", *, module_paths: Optional[List[str]] = None
) -> List[str]:
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
        Python module paths. This interface does not
        include the `__init__.py` modules.
    """
    if module_paths is None:
        module_paths = []
    file_or_dir_names: List[str] = os.listdir(dir_path)
    for file_or_dir_name in file_or_dir_names:
        file_or_dir_path: str = os.path.join(dir_path, file_or_dir_name)
        if os.path.isdir(file_or_dir_path):
            module_paths = get_module_paths_recursively(
                dir_path=file_or_dir_path, module_paths=module_paths
            )
            continue
        if not file_or_dir_path.endswith(".py"):
            continue
        if file_or_dir_name == "__init__.py":
            continue
        module_paths.append(file_or_dir_path)
    return module_paths


def save_tmp_module(*, script: str) -> str:
    """
    Save a temporary Python module.

    Parameters
    ----------
    script : str
        Python script string.

    Returns
    -------
    saved_module_path : str
        Saved temporary module path.
    """
    random_int: int = randint(1_000_000_000, 10_000_000_000)
    saved_module_path: str = f"./tmp_{datetime.now().timestamp()}_{random_int}.py"
    with open(saved_module_path, "w") as f:
        f.write(script)
    return saved_module_path


def save_tmp_module_and_run_script(*, script: str) -> str:
    """
    Save a temporary Python module and run that script.

    Parameters
    ----------
    script : str
        Python script string.

    Returns
    -------
    stdout : str
        Result stdout string.
    """
    tmp_mod_path: str = save_tmp_module(script=script)
    process: sp.CompletedProcess = sp.run(
        f"python {tmp_mod_path}", shell=True, stdout=sp.PIPE, stderr=sp.STDOUT
    )
    stdout: str = process.stdout.decode("utf-8")
    os.remove(tmp_mod_path)
    return stdout


def read_target_path_module(module_path: str) -> ModuleType:
    """
    Read a module of the specified module path.

    Parameters
    ----------
    module_path : str
        Target module path.

    Returns
    -------
    module : ModuleType
        Read module.
    """
    if module_path.startswith("./"):
        module_path = module_path.replace("./", "", 1)
    module_path = module_path.rsplit(".py", maxsplit=1)[0]
    module_path = module_path.replace("/", ".")
    module: ModuleType = importlib.import_module(name=module_path)
    return module


def read_module_or_class_from_package_path(module_or_class_package_path: str) -> Any:
    """
    Read a specified package path module or class.

    Parameters
    ----------
    module_or_class_package_path : str
        Target package module or class path.

    Returns
    -------
    module_or_class : ModuleType or Type
        Read module or class.
    """
    try:
        module: ModuleType = importlib.import_module(module_or_class_package_path)
    except Exception:
        splitted: List[str] = module_or_class_package_path.rsplit(".", maxsplit=1)
        module_or_class_package_path = splitted[0]
        class_name: str = splitted[1]
        module = importlib.import_module(module_or_class_package_path)
        return getattr(module, class_name)
    return module
