"""Test project for color_util module's interfaces.

Command examples:
$ python test_projects/color_util/main.py
$ python color_util/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

import apysc as ap
from apysc._color import color_util
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    _: ap.Stage = ap.Stage(
        background_color='#333')

    string_1: ap.String = color_util.complement_hex_color(
        hex_color_code=ap.String('333'))
    ap.assert_equal(expected='#333333', actual=string_1)

    string_2: ap.String = color_util.complement_hex_color(
        hex_color_code=ap.String('#5'))
    ap.assert_equal(expected='#000005', actual=string_2)

    string_3: ap.String = color_util.complement_hex_color(
        hex_color_code=ap.String('#333'))
    ap.assert_equal(expected='#333333', actual=string_3)

    string_4: ap.String = color_util.complement_hex_color(
        hex_color_code=ap.String('#555555'))
    ap.assert_equal(expected='#555555', actual=string_4)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
