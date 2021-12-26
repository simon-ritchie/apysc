"""The script to check whether there are no top-level
`import apysc` or `import apysc as ap` in the apysc package
modules.

Command example:
$ python check_apysc_top_level_import.py
"""

from logging import Logger
import os
from types import ModuleType
from typing import Any, List, Tuple
from apysc._file import module_util
import inspect

from apysc._console import loggers

logger: Logger = loggers.get_info_logger()


def _main() -> None:
    """check whether there are no top-level
    `import apysc` or `import apysc as ap` in the apysc package
    modules.

    Raises
    ------
    Exception
        If there are any top-level import of the `import apysc` or
        `import apysc as ap` in the apysc package modules.
    """
    logger.info('Getting module paths recursively...')
    module_paths: List[str] = module_util.get_module_paths_recursively(
        dir_path='./apysc/')
    logger.info("Checking each module's member value...")
    for module_path in module_paths:
        if not os.path.isfile(module_path):
            continue
        module: ModuleType = module_util.read_target_path_module(
            module_path=module_path)
        members: List[Tuple[str, Any]] = inspect.getmembers(
            object=module)
        for member_name, _ in members:
            if member_name != 'ap' and member_name != 'apysc':
                continue
            raise Exception(
                'The modules in the apysc package can not import '
                'apysc (e.g., import apysc as ap) module at the '
                'top-level scope.'
                f'\nInvalid module: {module_path}')
    logger.info('Completed and there are no errors!')


if __name__ == '__main__':
    _main()
