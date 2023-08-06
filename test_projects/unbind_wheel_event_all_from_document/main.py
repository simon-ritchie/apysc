"""Test project for unbind_wheel_event_all_from_document
interface.

Command examples:
$ python test_projects/unbind_wheel_event_all_from_document/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


def main() -> None:
    """
    Entry point of this test project.
    """
    _: ap.Stage = ap.Stage(background_color=ap.Color("#111"), stage_width=1000, stage_height=500)
    ap.bind_wheel_event_to_document(handler=on_document_wheel_1)
    ap.bind_wheel_event_to_document(handler=on_document_wheel_2)
    ap.unbind_wheel_event_all_from_document()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_document_wheel_1(e: ap.WheelEvent, options: dict) -> None:
    """
    Test handler that called when wheeled on document.

    Parameters
    ----------
    e : WheelEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace("Mouse wheel is detected. Probably unbind interface " "works incorrectly.")


def on_document_wheel_2(e: ap.WheelEvent, options: dict) -> None:
    """
    Test handler that called when wheeled on document.

    Parameters
    ----------
    e : WheelEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace("Mouse wheel is detected. Probably unbind interface " "works incorrectly.")


if __name__ == "__main__":
    main()
