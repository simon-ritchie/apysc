"""Test project for bind_wheel_event_to_document interface.

Command examples:
$ python test_projects/bind_wheel_event_to_document/main.py
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


class _MsgOptions(TypedDict):
    msg: str


def main() -> None:
    """
    Entry point of this test project.
    """
    _: ap.Stage = ap.Stage(
        background_color='#111',
        stage_width=1000, stage_height=500)
    options: _MsgOptions = {'msg': 'Hello!'}
    ap.bind_wheel_event_to_document(
        handler=on_document_wheel, options=options)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_document_wheel(e: ap.WheelEvent, options: _MsgOptions) -> None:
    """
    Test handler that called when wheeled on document.

    Parameters
    ----------
    e : WheelEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('Wheeled!')
    ap.trace('delta_x:', e.delta_x)
    ap.trace('delta_y:', e.delta_y)
    ap.assert_equal(left='Hello!', right=options['msg'])


if __name__ == '__main__':
    main()
