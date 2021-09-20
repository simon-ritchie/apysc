"""Test project for `Boolean` class.

Command examples:
$ python test_projects/Boolean/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from typing_extensions import TypedDict

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


class _Bool14Options(TypedDict):
    boolean_14: ap.Boolean


def main() -> None:
    """Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(background_color='#333')

    boolean_1: ap.Boolean = ap.Boolean(True)
    ap.assert_true(boolean_1)

    boolean_2: ap.Boolean = ap.Boolean(False)
    ap.assert_false(boolean_2)

    boolean_3: ap.Boolean = ap.Boolean(1)
    ap.assert_true(boolean_3)

    boolean_4: ap.Boolean = ap.Boolean(0)
    ap.assert_false(boolean_4)

    boolean_5: ap.Boolean = ap.Boolean(boolean_1)
    ap.assert_true(boolean_5)

    boolean_6: ap.Boolean = ap.Boolean(boolean_2)
    ap.assert_false(boolean_6)

    boolean_1.value = False
    ap.assert_false(boolean_1)

    boolean_2.value = True
    ap.assert_true(boolean_2)

    boolean_7: ap.Boolean = ap.Boolean(True)
    boolean_8: ap.Boolean = boolean_7.not_
    ap.assert_false(boolean_8)
    boolean_9: ap.Boolean = boolean_8.not_
    ap.assert_true(boolean_9)

    boolean_10: ap.Boolean = ap.Boolean(True)
    boolean_11: ap.Boolean = ap.Boolean(True)
    boolean_12: ap.Boolean = boolean_10 == boolean_11
    ap.assert_true(boolean_12)
    boolean_13: ap.Boolean = boolean_10 != boolean_11
    ap.assert_false(boolean_13)

    boolean_14: ap.Boolean = ap.Boolean(False)
    options: _Bool14Options = {'boolean_14': boolean_14}
    stage.click(on_stage_clicked, options=options)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_stage_clicked(e: ap.MouseEvent, options: _Bool14Options) -> None:
    """
    Test handler that called when stage is clicked.

    Parameters
    ----------
    e : MouseEvent
        Created event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('stage clicked!')
    boolean_14: ap.Boolean = options['boolean_14']
    boolean_14.value = True
    ap.assert_true(boolean_14 == True)  # noqa


if __name__ == '__main__':
    main()
