"""The test project for the debug mode setting.

Command examples:
$ python test_projects/debug_mode/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

import apysc as ap
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
    stage: ap.Stage = ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500)
    ap.set_debug_mode(stage=stage)
    _: ap.Sprite = ap.Sprite(stage=stage)
    int_1: ap.Int = ap.Int(10)
    int_1 += 5
    ap.unset_debug_mode()

    int_2: ap.Int = ap.Int(30)
    int_2 += 15

    ap.save_overall_html(
        dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == '__main__':
    main()
