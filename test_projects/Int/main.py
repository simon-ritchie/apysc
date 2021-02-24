"""Test project for `Int` class.

Command example:
$ python test_projects/Int/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage
from apyscript.file import file_util
from apyscript.html import exporter
from apyscript.logging.trace import trace
from apyscript.type.int import Int

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    stage: Stage = Stage(background_color='#333')

    int_1: Int = Int(10)
    trace('int_1 expected: 10, actual:', int_1)

    int_2: Int = int_1 + 20
    trace('int_2 expected: 30, actual:', int_2)

    int_3: Int = int_1 + int_2
    trace('int_3 expected: 40, actual:', int_3)

    exporter.save_expressions_overall_html(dest_dir_path=_DEST_DIR_PATH)



if __name__ == '__main__':
    main()
