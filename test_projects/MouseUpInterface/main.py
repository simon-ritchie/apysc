"""Test project for MouseUpInterface class.

Command examples:
$ python test_projects/MouseUpInterface/main.py
$ python MouseUpInterface/main.py
"""

import sys
from typing import Any
from typing import Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import MouseEvent
from apysc import Stage
from apysc import assert_equal
from apysc import trace
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
    stage: Stage = Stage(
        background_color='#111',
        stage_width=1000, stage_height=500)
    stage.mouseup(handler=on_stage_mouse_up, options={'msg': 'Hello!'})

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


def on_stage_mouse_up(e: MouseEvent, options: Dict[str, Any]) -> None:
    """
    Test handler that called when stage is mouse upped.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace('Stage is mouse upped!')
    assert_equal(expected='Hello!', actual=options['msg'])


if __name__ == '__main__':
    main()
