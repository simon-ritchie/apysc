"""Test project for `Boolean` class.

Command examples:
$ python test_projects/Boolean/main.py
$ python Boolean/main.py
"""

import sys
from typing import Any, Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import Boolean, MouseEvent
from apysc import Stage
from apysc import assert_false, trace
from apysc import assert_true
from apysc.file import file_util
from apysc.html import exporter

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """Entry point of this test project.
    """
    stage: Stage = Stage(background_color='#333')

    boolean_1: Boolean = Boolean(True)
    assert_true(boolean_1)

    boolean_2: Boolean = Boolean(False)
    assert_false(boolean_2)

    boolean_3: Boolean = Boolean(1)
    assert_true(boolean_3)

    boolean_4: Boolean = Boolean(0)
    assert_false(boolean_4)

    boolean_5: Boolean = Boolean(boolean_1)
    assert_true(boolean_5)

    boolean_6: Boolean = Boolean(boolean_2)
    assert_false(boolean_6)

    boolean_1.value = False
    assert_false(boolean_1)

    boolean_2.value = True
    assert_true(boolean_2)

    boolean_7: Boolean = Boolean(True)
    boolean_8: Boolean = boolean_7.not_
    assert_false(boolean_8)
    boolean_9: Boolean = boolean_8.not_
    assert_true(boolean_9)

    boolean_10: Boolean = Boolean(True)
    boolean_11: Boolean = Boolean(True)
    boolean_12: Boolean = boolean_10 == boolean_11
    assert_true(boolean_12)
    boolean_13: Boolean = boolean_10 != boolean_11
    assert_false(boolean_13)

    boolean_14: Boolean = Boolean(False)
    stage.click(on_stage_clicked, kwargs={'boolean_14': boolean_14})

    exporter.save_expressions_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_stage_clicked(e: MouseEvent, kwargs: Dict[str, Any]) -> None:
    """
    Test handler that called when stage is clicked.

    Parameters
    ----------
    e : MouseEvent
        Created event instance.
    kwargs : dict
        Keyword arguments.
    """
    trace('stage clicked!')
    boolean_14: Boolean = kwargs['boolean_14']
    boolean_14.value = True
    assert_true(boolean_14 == True)


if __name__ == '__main__':
    main()
