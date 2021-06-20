"""Test project for unbind_wheel_event_all_from_document
interface.

Command examples:
$ python test_projects/unbind_wheel_event_all_from_document/main.py
$ python unbind_wheel_event_all_from_document/main.py
"""

import sys
from typing import Any
from typing import Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import Stage
from apysc import WheelEvent
from apysc import bind_wheel_event_to_document
from apysc import save_overall_html
from apysc import trace
from apysc import unbind_wheel_event_all_from_document
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
    _: Stage = Stage(
        background_color='#111',
        stage_width=1000, stage_height=500)
    bind_wheel_event_to_document(handler=on_document_wheel_1)
    bind_wheel_event_to_document(handler=on_document_wheel_2)
    unbind_wheel_event_all_from_document()

    save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_document_wheel_1(e: WheelEvent, options: Dict[str, Any]) -> None:
    """
    Test handler that called when wheeled on document.

    Parameters
    ----------
    e : WheelEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace(
        'Mouse wheel is detected. Probably unbind interface '
        'works incorrectly.')


def on_document_wheel_2(e: WheelEvent, options: Dict[str, Any]) -> None:
    """
    Test handler that called when wheeled on document.

    Parameters
    ----------
    e : WheelEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace(
        'Mouse wheel is detected. Probably unbind interface '
        'works incorrectly.')


if __name__ == '__main__':
    main()
