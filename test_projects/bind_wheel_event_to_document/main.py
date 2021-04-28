"""Test project for bind_wheel_event_to_document interface.

Command examples:
$ python test_projects/bind_wheel_event_to_document/main.py
$ python bind_wheel_event_to_document/main.py
"""

import sys
from typing import Any
from typing import Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import Event, bind_wheel_event_to_document
from apysc import Rectangle, WheelEvent
from apysc import Sprite
from apysc import Stage
from apysc import String
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
    """
    Entry point of this test project.
    """
    stage: Stage = Stage(
        background_color='#111',
        stage_width=1000, stage_height=500)
    bind_wheel_event_to_document(
        handler=on_document_wheel, options={'msg': 'Hello!'})

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


def on_document_wheel(e: WheelEvent, options: Dict[str, Any]) -> None:
    """
    Test handler that called when wheeled on document.

    Parameters
    ----------
    e : WheelEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace('Wheeled!')
    trace('delta_x:', e.delta_x)
    trace('delta_y:', e.delta_y)
    assert_equal(expected='Hello!', actual=options['msg'])


if __name__ == '__main__':
    main()
