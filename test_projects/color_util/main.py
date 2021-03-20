"""Test project for color_util module's interfaces.

Command examples:
$ python test_projects/color_util/main.py
$ python color_util/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apyscript.color import color_util
from apyscript.console.assertion import assert_equal
from apyscript.display import Stage
from apyscript.file import file_util
from apyscript.html import exporter
from apyscript.type import String

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    _: Stage = Stage(
        background_color='#333')

    string_1: String = color_util.complement_hex_color(
        hex_color_code=String('333'))
    assert_equal(expected='#333333', actual=string_1)

    string_2: String = color_util.complement_hex_color(
        hex_color_code=String('#5'))
    assert_equal(expected='#000005', actual=string_2)

    string_3: String = color_util.complement_hex_color(
        hex_color_code=String('#333'))
    assert_equal(expected='#333333', actual=string_3)

    string_4: String = color_util.complement_hex_color(
        hex_color_code=String('#555555'))
    assert_equal(expected='#555555', actual=string_4)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
