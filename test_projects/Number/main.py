"""Test project for `Number` class.

Command example:
$ python test_projects/Number/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apyscript.display.stage import Stage
from apyscript.file import file_util
from apyscript.html import exporter
from apyscript.logging.trace import trace
from apyscript.type.number import Number

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """Entry point of this test project.
    """
    _: Stage = Stage(background_color='#333')

    number_1: Number = Number(value=10.5)
    trace('number_1 expected: 10.5, actual:', number_1)

    number_2: Number = number_1 + 20.6
    trace('number_2 expected: 31.1, actual:', number_2)

    number_3: Number = number_1 + number_2
    trace('number_3 expected: 41.6, actual:', number_3)

    exporter.save_expressions_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
