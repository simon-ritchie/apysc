"""Test project for `String` class.

Command examples:
$ python test_projects/String/main.py
$ python String/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc.console import assert_equal
from apysc.display import Stage
from apysc.file import file_util
from apysc.html import exporter
from apysc.type import String

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """Entry point of this test project.
    """
    _: Stage = Stage(background_color='#333')

    string_1: String = String(value='Hello')
    assert_equal(expected='Hello', actual=string_1)

    string_2: String = string_1 + ' World!'
    assert_equal(expected='Hello World!', actual=string_2)

    string_3: String = string_1 * 2
    assert_equal(expected='HelloHello', actual=string_3)

    string_1 += ' World!'
    assert_equal(expected='Hello World!', actual=string_1)

    string_1 *= 2
    assert_equal(expected='Hello World!Hello World!', actual=string_1)

    exporter.save_expressions_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
